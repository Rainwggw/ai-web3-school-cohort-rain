/**
 * AI × Web3 School - WCB 任务获取脚本
 * 使用 API 密钥从 web3career.build 获取课程任务
 */

const fs = require('fs');
const path = require('path');

class WCBTaskFetcher {
    constructor(apiKey) {
        this.apiKey = apiKey;
        this.baseUrl = 'https://web3career.build';
        this.headers = {
            'Authorization': `Bearer ${apiKey}`,
            'Content-Type': 'application/json'
        };
        this.tasks = [];
    }

    async getTasks() {
        try {
            // API 端点
            const url = `${this.baseUrl}/api/v1/tasks`;

            // 发送请求
            const response = await fetch(url, {
                method: 'GET',
                headers: this.headers
            });

            if (response.ok) {
                const data = await response.json();
                this.tasks = data.tasks || [];
                console.log(`✅ 成功获取 ${this.tasks.length} 个任务`);
                return this.tasks;
            } else {
                console.error(`❌ 获取任务失败: ${response.status}`);
                const errorText = await response.text();
                console.error(`错误信息: ${errorText}`);
                return [];
            }
        } catch (error) {
            console.error(`❌ 网络错误: ${error.message}`);
            return [];
        }
    }

    extractTaskNames() {
        return this.tasks.map(task => {
            return task.title || task.name || 'Unknown Task';
        });
    }

    createTaskFolders(taskNames, basePath) {
        const createdFolders = [];
        const tasksDir = path.join(basePath, 'tasks');

        // 确保任务目录存在
        if (!fs.existsSync(tasksDir)) {
            fs.mkdirSync(tasksDir, { recursive: true });
        }

        taskNames.forEach(taskName => {
            const folderName = this.cleanFolderName(taskName);
            const folderPath = path.join(tasksDir, folderName);

            // 检查文件夹是否存在
            if (!fs.existsSync(folderPath)) {
                fs.mkdirSync(folderPath, { recursive: true });
                console.log(`📁 创建文件夹: ${folderPath}`);
                createdFolders.push({
                    name: taskName,
                    path: folderPath
                });
            } else {
                console.log(`📁 文件夹已存在: ${folderPath}`);
            }
        });

        return createdFolders;
    }

    cleanFolderName(name) {
        // 清理文件名，移除特殊字符
        let cleaned = name
            .replace(/[^\w\s-]/g, '_')  // 替换特殊字符
            .replace(/[_]+/g, '_')      // 合并多个下划线
            .replace(/^_|_$/g, '')      // 去除首尾下划线
            .substring(0, 50);          // 限制长度

        return cleaned;
    }

    createTaskReadme(taskInfo, folderPath) {
        const readmeContent = `# ${taskInfo.name || 'Task'}

## 任务描述
${taskInfo.description || '暂无描述'}

## 任务要求
${this.formatRequirements(taskInfo.requirements || [])}

## 截止日期
${taskInfo.due_date || '未设定'}

## 相关资源
${this.formatResources(taskInfo.resources || [])}

## 进度跟踪
- [ ] 开始任务
- [ ] 进行中
- [ ] 提交完成
- [ ] 获得反馈

---

*创建时间: ${taskInfo.created_at || '未知'}*
*任务ID: ${taskInfo.id || '未知'}*
`;

        const readmePath = path.join(folderPath, 'README.md');
        fs.writeFileSync(readmePath, readmeContent, 'utf8');
        console.log(`📝 创建 README: ${readmePath}`);
    }

    formatRequirements(requirements) {
        if (!requirements || requirements.length === 0) {
            return '暂无具体要求';
        }

        return requirements.map(req => `- ${req}`).join('\n');
    }

    formatResources(resources) {
        if (!resources || resources.length === 0) {
            return '暂无相关资源';
        }

        return resources.map(resource => `- [${resource.name || resource.title}](${resource.url || '#'})`).join('\n');
    }

    async run() {
        try {
            // 获取任务
            const tasks = await this.getTasks();

            if (tasks.length > 0) {
                // 提取任务名称
                const taskNames = this.extractTaskNames();

                // 设置基础路径
                const basePath = path.join(__dirname, '..');

                // 创建任务文件夹
                const createdFolders = this.createTaskFolders(taskNames, basePath);

                console.log('\n📊 总结:');
                console.log(`- 总任务数: ${tasks.length}`);
                console.log(`- 新建文件夹: ${createdFolders.length}`);
                console.log(`- 已存在文件夹: ${taskNames.length - createdFolders.length}`);

                // 为每个创建的文件夹创建 README
                for (const folderInfo of createdFolders) {
                    const taskDetail = tasks.find(t =>
                        (t.title || t.name) === folderInfo.name
                    );
                    if (taskDetail) {
                        this.createTaskReadme(taskDetail, folderInfo.path);
                    }
                }
            } else {
                console.log('❌ 未能获取到任务信息');
            }
        } catch (error) {
            console.error('❌ 执行出错:', error.message);
        }
    }
}

// 主函数
async function main() {
    const apiKey = 'w3cb_sk_m-TCyb71gQeg-xh1La_L_Rq0ViFvkh7m';

    const fetcher = new WCBTaskFetcher(apiKey);
    await fetcher.run();
}

// 运行主函数
if (require.main === module) {
    main();
}

module.exports = WCBTaskFetcher;