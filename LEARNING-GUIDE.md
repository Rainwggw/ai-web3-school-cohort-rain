# AI × Web3 School 学习指南

## 📖 概述

本指南帮助你高效使用个人学习仓库，系统性地完成 AI × Web3 School 的学习任务。

## 🗂️ 文件结构说明

```
ai-web3-school-cohort-rain/
├── README.md              # 项目介绍和链接
├── profile.md             # 个人档案和学习目标
├── learning-plan.md       # 详细学习计划和进度跟踪
├── LEARNING-GUIDE.md     # 本指南文件
├── daily/                 # 每日学习记录
│   ├── 2026-05-19-learning-note.md
│   └── ...
├── tasks/                 # 任务分解和跟踪
│   ├── week1-preparation.md
│   └── ...
├── experiments/           # 代码实验和原型
├── handbook-feedback/     # 对课程内容的反馈
│   ├── 2026-05-19-repository-suggestion.md
│   └── ...
├── submissions/          # 课程提交作品
└── templates/            # 笔记和工具模板
    ├── daily-note.md      # 详细每日笔记模板
    ├── task-note.md       # 任务笔记模板
    ├── quick-daily-checkin.md  # 快速打卡模板
    └── create-daily-note.sh    # 自动创建每日笔记脚本
```

## 📅 日常学习流程

### 1. 每日开始 (9:00)
```bash
# 创建当天的学习笔记
./templates/create-daily-note.sh

# 或手动复制模板
cp templates/daily-note.md daily/YYYY-MM-DD-learning-note.md
```

### 2. 学习前规划
- 在 `daily/YYYY-MM-DD-learning-note.md` 中设置今日目标
- 参考 `learning-plan.md` 确定学习内容

### 3. 学习过程记录
- 实时记录学习内容
- 保存重要的代码片段到 `experiments/`
- 记录遇到的问题和解决方案

### 4. 每日总结 (21:00)
- 完成学习记录的各个部分
- 更新 `learning-plan.md` 的进度
- 如有必要，创建 `handbook-feedback/` 中的反馈文件

### 5. 每周回顾 (周日)
- 整理本周所有学习记录
- 更新任务进度
- 规划下周学习重点

## 🎯 学习计划使用方法

### Phase 1: AI Fundamentals
1. **LLM & Prompt** (Week 2-3)
   - 学习基础概念
   - 实践 Prompt 编写
   - 完成 5-10 个练习

2. **Context & Memory** (Week 4)
   - 理解上下文管理
   - 实现记忆机制
   - 构建对话系统

3. **RAG & Agent** (Week 5-6)
   - 学习 RAG 原理
   - 开发简单 Agent
   - 尝试部署

### Phase 2: Web3 Fundamentals
- 系统学习区块链基础知识
- 实践智能合约开发
- 理解钱包和账户管理

### Phase 3: AI × Web3 Integration
- 结合 AI 和 Web3 技术
- 开发集成应用
- 准备 Hackathon 项目

## 📝 记录最佳实践

### 每日记录要点
1. **具体目标**：使用 SMART 原则设定目标
2. **量化进度**：记录学习时长和完成度
3. **成果展示**：保存代码和作品链接
4. **问题追踪**：记录 blockers 和解决方法
5. **反思总结**：每日学习心得

### 反馈提交流程
1. 在学习过程中发现 Handbook 的问题
2. 在 `handbook-feedback/` 创建反馈文件
3. 使用标准格式：页面链接、问题描述、改进建议
4. 提交 PR 或在社群中分享

## 🔧 工具使用技巧

### Git 工作流
```bash
# 每日提交
git add daily/
git commit -m "Add daily note for YYYY-MM-DD"

# 每周整理
git add learning-plan.md
git commit -m "Update weekly progress"

# 提交作品
git add experiments/
git commit -m "New experiment: [项目名]"
```

### GitHub CLI 使用
```bash
# 查看仓库状态
gh repo view

# 创建 Issue 跟踪任务
gh issue create --title "Task name" --body "Description"

# 管理 PR
gh pr create --title "Update progress" --body "Weekly summary"
```

## 📊 进度可视化

### 使用 GitHub Projects
1. 创建 "Learning Progress" project
2. 添加列：To Do, In Progress, Review, Done
3. 将任务卡片关联到相应阶段
4. 每周更新状态

### 里程碑设置
- Week 1: ✅ Preparation Done
- Week 6: 🔄 AI Fundamentals
- Week 12: 🔄 Web3 Fundamentals  
- Week 20: 🔄 Final Project

## 💡 高效学习建议

1. **固定学习时间**：每天 19:00-23:00 专注学习
2. **番茄工作法**：25分钟专注 + 5分钟休息
3. **费曼学习法**：学完后向他人解释概念
4. **项目驱动**：通过实际项目掌握知识
5. **社群互动**：积极参与讨论和分享

## 🆘 遇到问题怎么办

1. **技术问题**：
   - 查看 `experiments/` 中的历史代码
   - 搜索 GitHub Issues
   - 在社群提问时附上详细日志

2. **学习瓶颈**：
   - 调整学习计划
   - 寻找额外资源
   - 与同学组队学习

3. **进度落后**：
   - 分析时间分配
   - 简化部分内容
   - 增加学习时长

---

*最后更新：2026-05-19*
*维护者：[@Rainwggw](https://github.com/Rainwggw)*