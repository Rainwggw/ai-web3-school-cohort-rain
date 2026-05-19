# Feedback: Repository Structure Suggestions

## Handbook Page
- URL: https://aiweb3.school/zh/handbook/ (假设页面，实际需要确认)

## Issue Type
- [x] Structure suggestion
- [ ] Missing content

## Description

基于已完成的前置准备工作，建议在 Handbook 中增加关于个人学习仓库结构的最佳实践指导。目前的课程引导创建了基础的仓库结构，但可以提供更详细的建议：

1. **文件组织最佳实践**
2. **学习笔记的标准格式**
3. **进度追踪方法**
4. **反馈提交流程**

## Suggested Improvement

建议在 Handbook 的 "前置准备" 章节中添加一个子章节 "学习仓库建设指南"，包含：

### 1. 推荐的仓库结构
```
repository-name/
├── README.md              # 项目介绍和学习目标
├── profile.md            # 个人档案和背景
├── learning-plan.md      # 详细学习计划和进度
├── daily/                # 每日学习记录
│   ├── 2026-05-19.md
│   └── ...
├── tasks/                # 任务分解和跟踪
│   ├── week1-preparation.md
│   └── ...
├── experiments/          # 代码实验和原型
├── handbook-feedback/   # 对课程内容的反馈
├── resources/            # 学习资源收集
└── templates/           # 笔记模板
    ├── daily-template.md
    └── task-template.md
```

### 2. 学习笔记标准格式
- 学习目标
- 内容摘要
- 关键收获
- 问题与 blockers
- 实践代码
- 资源链接
- 明日计划

### 3. 进度可视化建议
- 使用 GitHub Projects 管理任务
- 定期创建进度报告
- 建立 Milestone 标记关键节点

## Source / Reference

基于实际创建的 `ai-web3-school-cohort-rain` 仓库经验，发现详细的仓库结构和标准化的记录格式有助于：
- 提高学习效率
- 便于追踪进度
- 方便导师了解学习情况
- 形成完整的学习档案