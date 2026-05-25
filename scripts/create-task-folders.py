#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI × Web3 School - 任务文件夹创建脚本
使用模拟数据创建任务文件夹
"""

import json
import os
import sys
from pathlib import Path
import shutil

# 设置 UTF-8 编码
sys.stdout.reconfigure(encoding='utf-8')

class TaskFolderCreator:
    """任务文件夹创建器"""

    def __init__(self):
        self.mock_tasks_file = Path(__file__).parent / "mock-tasks.json"
        self.base_path = Path(__file__).parent.parent / "tasks"

    def load_mock_tasks(self):
        """加载模拟任务数据"""
        with open(self.mock_tasks_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def create_task_folders(self):
        """创建任务文件夹"""
        print("🚀 开始创建任务文件夹...")

        # 加载任务数据
        data = self.load_mock_tasks()
        tasks = data.get('tasks', [])

        # 确保任务目录存在
        self.base_path.mkdir(parents=True, exist_ok=True)

        created_folders = []
        existing_folders = []

        for task in tasks:
            task_name = task.get('title', 'Unknown Task')
            folder_name = self.clean_folder_name(task_name)
            folder_path = self.base_path / folder_name

            # 检查文件夹是否已存在
            if folder_path.exists():
                print(f"📁 文件夹已存在: {folder_name}")
                existing_folders.append({
                    'name': task_name,
                    'path': str(folder_path)
                })
            else:
                # 创建文件夹
                folder_path.mkdir(parents=True, exist_ok=True)
                print(f"📁 创建文件夹: {folder_name}")

                # 创建 README 文件
                self.create_task_readme(task, folder_path)

                # 创建其他子文件夹
                self.create_subfolders(folder_path)

                created_folders.append({
                    'name': task_name,
                    'path': str(folder_path)
                })

        return created_folders, existing_folders

    def clean_folder_name(self, name):
        """清理文件名"""
        import re
        name = re.sub(r'[^\w\s-]', '_', name)
        name = re.sub(r'[_]+', '_', name)
        name = name.strip('_')
        if len(name) > 50:
            name = name[:50]
        return name

    def create_task_readme(self, task_info, folder_path):
        """创建任务 README 文件"""
        readme_content = f"""# {task_info.get('title', 'Task')}

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

## 学习笔记
- [ ]
- [ ]
- [ ]

## 代码实验
- [ ]
- [ ]

---

*创建时间: {task_info.get('created_at', '未知')}*
*任务ID: {task_info.get('id', '未知')}*
*更新时间: {self.get_current_time()}*
"""

        readme_path = folder_path / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)

    def create_subfolders(self, folder_path):
        """创建子文件夹结构"""
        subfolders = ['notes', 'experiments', 'resources', 'submissions']

        for subfolder in subfolders:
            sub_path = folder_path / subfolder
            sub_path.mkdir(exist_ok=True)
            print(f"  📁 创建子文件夹: {subfolder}")

    def format_requirements(self, requirements):
        """格式化任务要求"""
        if not requirements:
            return '暂无具体要求'

        formatted = []
        for req in requirements:
            formatted.append(f"- {req}")
        return '\n'.join(formatted)

    def format_resources(self, resources):
        """格式化相关资源"""
        if not resources:
            return '暂无相关资源'

        formatted = []
        for resource in resources:
            name = resource.get('name', 'Unknown Resource')
            url = resource.get('url', '#')
            formatted.append(f"- [{name}]({url})")
        return '\n'.join(formatted)

    def get_current_time(self):
        """获取当前时间"""
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def create_summary_report(self, created_folders, existing_folders):
        """创建总结报告"""
        report_content = f"""# AI × Web3 School 任务文件夹创建报告

## 📊 创建统计
- 总任务数: {len(created_folders) + len(existing_folders)}
- 新建文件夹: {len(created_folders)}
- 已存在文件夹: {len(existing_folders)}

## 📁 新建任务文件夹
"""
        for folder in created_folders:
            report_content += f"- {folder['name']}\n"

        report_content += "\n## 📋 已存在任务文件夹\n"
        for folder in existing_folders:
            report_content += f"- {folder['name']}\n"

        report_content += f"""

## ✅ 创建时间
{self.get_current_time()}

---

*报告生成工具: TaskFolderCreator*
"""

        # 保存报告
        report_path = self.base_path.parent / "task-folders-report.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)

        print(f"📊 生成报告: {report_path}")
        return report_path

    def run(self):
        """运行创建器"""
        created, existing = self.create_task_folders()
        self.create_summary_report(created, existing)

        print("\n✅ 任务文件夹创建完成!")
        print(f"📊 新建: {len(created)} 个")
        print(f"📋 已存在: {len(existing)} 个")

if __name__ == "__main__":
    creator = TaskFolderCreator()
    creator.run()