#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI × Web3 School - WCB 任务获取脚本
使用 API 密钥从 web3career.build 获取课程任务
"""

import requests
import json
import os
from pathlib import Path

class WCBTaskFetcher:
    """WCB 任务获取器"""

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://web3career.build"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.tasks = []

    def get_tasks(self):
        """获取 AI × Web3 School 的所有任务"""
        try:
            # API 端点（基于之前的搜索结果）
            url = f"{self.base_url}/api/v1/tasks"

            # 发送 GET 请求
            response = requests.get(url, headers=self.headers)

            if response.status_code == 200:
                data = response.json()
                self.tasks = data.get('tasks', [])
                print(f"✅ 成功获取 {len(self.tasks)} 个任务")
                return self.tasks
            else:
                print(f"❌ 获取任务失败: {response.status_code}")
                print(f"错误信息: {response.text}")
                return []

        except requests.exceptions.RequestException as e:
            print(f"❌ 网络错误: {e}")
            return []

    def extract_task_names(self):
        """提取任务名称"""
        task_names = []
        for task in self.task:
            # 根据任务结构提取名称
            name = task.get('title', task.get('name', 'Unknown Task'))
            task_names.append(name)
        return task_names

    def create_task_folders(self, task_names, base_path):
        """根据任务名称创建文件夹"""
        created_folders = []

        for task_name in task_names:
            # 清理任务名称，使其成为有效的文件夹名
            folder_name = self.clean_folder_name(task_name)
            folder_path = Path(base_path) / folder_name

            # 检查文件夹是否已存在
            if not folder_path.exists():
                folder_path.mkdir(parents=True, exist_ok=True)
                print(f"📁 创建文件夹: {folder_path}")
                created_folders.append({
                    'name': task_name,
                    'path': str(folder_path)
                })
            else:
                print(f"📁 文件夹已存在: {folder_path}")

        return created_folders

    def clean_folder_name(self, name):
        """清理文件名，移除特殊字符"""
        # 替换特殊字符为下划线
        import re
        name = re.sub(r'[^\w\s-]', '_', name)
        # 替换多个下划线为单个
        name = re.sub(r'[_]+', '_', name)
        # 去除首尾下划线
        name = name.strip('_')
        # 限制长度
        if len(name) > 50:
            name = name[:50]
        return name

    def create_task_readme(self, task_info, folder_path):
        """为每个任务创建 README 文件"""
        readme_content = f"""# {task_info.get('name', 'Task')}

## 任务描述
{task_info.get('description', '暂无描述')}

## 任务要求
{self.format_requirements(task_info.get('requirements', []))}

## 截止日期
{task_info.get('due_date', '未设定')}

## 相关资源
{self.format_resources(task_info.get('resources', []))}

## 进度跟踪
- [ ] 开始任务
- [ ] 进行中
- [ ] 提交完成
- [ ] 获得反馈

---

*创建时间: {task_info.get('created_at', '未知')}*
*任务ID: {task_info.get('id', '未知')}*
"""

        readme_path = Path(folder_path) / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print(f"📝 创建 README: {readme_path}")

def main():
    """主函数"""
    # API 密钥
    api_key = "w3cb_sk_m-TCyb71gQeg-xh1La_L_Rq0ViFvkh7m"

    # 初始化任务获取器
    fetcher = WCBTaskFetcher(api_key)

    # 获取任务
    tasks = fetcher.get_tasks()

    if tasks:
        # 提取任务名称
        task_names = fetcher.extract_task_names()

        # 设置基础路径
        base_path = Path("/e/Ethereum/AI x Web3 School/ai-web3-school-cohort-rain/tasks")

        # 创建任务文件夹
        created_folders = fetcher.create_task_folders(task_names, base_path)

        print(f"\n📊 总结:")
        print(f"- 总任务数: {len(tasks)}")
        print(f"- 新建文件夹: {len(created_folders)}")
        print(f"- 已存在文件夹: {len(task_names) - len(created_folders)}")

        # 为每个创建的文件夹创建 README
        for folder_info in created_folders:
            # 找到对应的任务详情
            task_detail = next((t for t in tasks if t.get('title') == folder_info['name']), None)
            if task_detail:
                fetcher.create_task_readme(task_detail, folder_info['path'])
    else:
        print("❌ 未能获取到任务信息")

if __name__ == "__main__":
    main()