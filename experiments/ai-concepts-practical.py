#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI × Web3 概念实践示例
演示如何在实际应用中实现这些概念
"""

from typing import Dict, List, Any
import json

class AIConceptsDemo:
    """演示 AI 概念在实际 Web3 开发中的应用"""

    def __init__(self):
        self.setup_environment()

    def setup_environment(self):
        """设置演示环境"""
        print("🚀 正在设置 AI × Web3 演示环境...")
        # 这里可以初始化必要的连接和配置
        self.wallet_connected = False
        self.contract_deployed = False

    # ==================== 1. LLM 演示 ====================
    def demonstrate_llm(self):
        """演示大型语言模型在 Web3 开发中的应用"""
        print("\n📚 1. LLM (Large Language Model) 演示")
        print("=" * 50)

        # 模拟 LLM 生成智能合约
        prompt = "创建一个安全的 NFT 合约，包含白名单和价格控制"
        contract_code = self.llm_generate_contract(prompt)

        print("Prompt:", prompt)
        print("\n生成的合约代码:")
        print("-" * 30)
        print(contract_code[:200] + "...")  # 只显示前200个字符

        # 检查常见误区
        print("\n❌ 常见误区: 认为 AI 生成的代码完全安全")
        print("✅ 正确做法: 必须经过人工审计和测试")

    def llm_generate_contract(self, prompt: str) -> str:
        """模拟 LLM 生成合约代码"""
        return f"""
// 由 AI 生成的 NFT 合约
// 基于 prompt: {prompt}

pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTCollection is ERC721, Ownable {{
    uint256 public price = 0.1 ether;
    bool public publicSaleActive = false;
    mapping(address => uint256) public whitelistMints;
    uint256 public maxMintsPerWallet = 3;

    constructor() ERC721("AI Generated NFT", "AGNFT") {{}}

    function mint(uint256 tokenId) external payable {{
        require(publicSaleActive, "Sale not active");
        require(msg.value >= price, "Insufficient payment");
        require(whitelistMints[msg.sender] < maxMintsPerWallet, "Max mints reached");

        _safeMint(msg.sender, tokenId);
        whitelistMints[msg.sender]++;
    }}

    function toggleSale() external onlyOwner {{
        publicSaleActive = !publicSaleActive;
    }}
}}
"""

    # ==================== 2. Prompt Engineering 演示 ====================
    def demonstrate_prompt_engineering(self):
        """演示提示词工程"""
        print("\n💬 2. Prompt Engineering 演示")
        print("=" * 50)

        # 不同质量的 prompt
        bad_prompt = "做个 NFT 合约"
        good_prompt = "使用 OpenZeppelin 4.x 创建一个 NFT 合约，要求：1) 支持白名单铸造 2) 有价格控制 3) 限制每个地址铸造数量 4) 包含暂停功能 5) 只能由所有者管理"

        print("❌ 差的 Prompt:")
        print(f"'{bad_prompt}'")
        print("\n✅ 好的 Prompt:")
        print(f"'{good_prompt}'")

        print("\n常见误区:")
        print("- ❌ 认为 prompt 越长越好")
        print("- ❌ 添加太多无关细节")
        print("- ✅ 保持清晰、具体、结构化")

    # ==================== 3. Context Window 演示 ====================
    def demonstrate_context_window(self):
        """演示上下文窗口的使用"""
        print("\n🪟 3. Context Window 演示")
        print("=" * 50)

        # 构建完整的上下文
        context = self.build_development_context()

        print("Context 内容（模拟）:")
        print(f"- 合约代码: {len(context['contract_code'])} 字符")
        print(f"- 测试用例: {len(context['test_cases'])} 字符")
        print(f"- 安全文档: {len(context['security_docs'])} 字符")
        print(f"- 需求文档: {len(context['requirements'])} 字符")

        print("\nAI 基于完整上下文的建议:")
        suggestions = self.get_context_suggestions(context)
        for suggestion in suggestions:
            print(f"- {suggestion}")

        print("\n常见误区:")
        print("- ❌ 一次性提供所有历史记录")
        print("- ❌ 忽视上下文的优先级")
        print("- ✅ 合理组织和优先级排序信息")

    def build_development_context(self) -> Dict[str, str]:
        """构建开发上下文"""
        return {
            "contract_code": """
// Uniswap V3 流动性提供者
contract LiquidityProvider {
    function addLiquidity() external payable {
        // 实现细节
    }
}
""",
            "test_cases": """
describe("LiquidityProvider", () => {
    it("Should add liquidity correctly", async () => {
        // 测试实现
    });
});
""",
            "security_docs": """
安全注意事项：
1. 重入攻击防护
2. 滑点保护
3. 访问控制
""",
            "requirements": """
功能需求：
1. 支持多种代币
2. 动态手续费
3. 流动性挖矿
"""
        }

    def get_context_suggestions(self, context: Dict) -> List[str]:
        """基于上下文获取建议"""
        return [
            "添加紧急停止功能",
            "实现价格预言机验证",
            "增加流动性奖励分配"
        ]

    # ==================== 4. Workflow 演示 ====================
    def demonstrate_workflow(self):
        """演示工作流程设计"""
        print("\n🔄 4. Workflow 演示")
        print("=" * 50)

        workflow = self.create_nft_workflow()

        print("NFT 发布工作流程:")
        for i, phase in enumerate(workflow['phases'], 1):
            print(f"{i}. {phase['name']}")
            print(f"   AI 工具: {', '.join(phase['ai_tools'])}")
            print(f"   人工任务: {', '.join(phase['human_tasks'])}")
            print()

        print("Guardrails:")
        for guard in workflow['guardrails']:
            print(f"- {guard}")

        print("\nHuman-in-the-Loop 节点:")
        for node in workflow['human_in_loop']:
            print(f"- {node}")

    def create_nft_workflow(self) -> Dict:
        """创建 NFT 工作流程"""
        return {
            "phases": [
                {
                    "name": "概念设计",
                    "ai_tools": ["DALL-E", "Midjourney"],
                    "human_tasks": ["创意构思", "风格选择"]
                },
                {
                    "name": "合约开发",
                    "ai_tools": ["Claude", "ChatGPT"],
                    "human_tasks": ["安全审计", "功能测试"]
                },
                {
                    "name": "前端开发",
                    "ai_tools": ["React", "Tailwind"],
                    "human_tasks": ["UI 设计", "用户体验"]
                }
            ],
            "guardrails": [
                "内容安全检查",
                "版权验证",
                "合规性审查"
            ],
            "human_in_loop": [
                "最终设计确认",
                "合约部署授权",
                "价格策略决定"
            ]
        }

    # ==================== 5. Agent 演示 ====================
    def demonstrate_agent(self):
        """演示 AI Agent"""
        print("\n🤖 5. Agent 演示")
        print("=" * 50)

        agent = self.create_defi_agent()

        print("DeFi 交易 Agent 能力:")
        for ability, desc in agent['capabilities'].items():
            print(f"- {ability}: {desc}")

        print("\n工具使用示例:")
        for tool, functions in agent['tools'].items():
            print(f"🛠️ {tool}:")
            for func in functions:
                print(f"  - {func}")

        print("\n工作流程:")
        for i, step in enumerate(agent['workflow'].items(), 1):
            print(f"{i}. {step}")

        print("\n安全限制:")
        for constraint, value in agent['constraints'].items():
            print(f"- {constraint}: {value}")

        print("\n⚠️  重要提醒: Agent 需要严格的安全监控")

    def create_defi_agent(self) -> Dict:
        """创建 DeFi Agent"""
        return {
            "capabilities": {
                "monitoring": "实时监控多个 DeFi 协议",
                "analysis": "识别套利机会",
                "execution": "执行交易",
                "risk_management": "风险管理"
            },
            "tools": {
                "uniswap": ["getPool", "swap"],
                "aave": ["deposit", "withdraw"],
                "chainlink": ["getPrice", "getHistorical"],
                "ethers": ["sendTransaction", "estimateGas"]
            },
            "workflow": {
                1: "获取市场数据",
                2: "分析机会",
                3: "风险评估",
                4: "执行交易",
                5: "更新策略"
            },
            "constraints": {
                "max_slippage": "0.5%",
                "max_gas": "50 gwei",
                "max_exposure": "10%"
            }
        }

    # ==================== 6. Tool Use 演示 ====================
    def demonstrate_tool_use(self):
        """演示工具使用"""
        print("\n🔧 6. Tool Use 演示")
        print("=" * 50)

        # 模拟工具调用
        print("模拟工具调用过程:")
        print("1. 获取 Uniswap V3 池数据...")
        pool_data = self.simulate_tool_call("uniswap", "getPool", "ETH/USDC")
        print(f"   池数据: {pool_data}")

        print("2. 获取 Chainlink 价格...")
        price_data = self.simulate_tool_call("chainlink", "getPrice", "ETH/USD")
        print(f"   价格: ${price_data}")

        print("3. 执行交易...")
        tx_result = self.simulate_tool_call("ethers", "sendTransaction", {
            "to": "0x...",
            "value": "0.1 ether"
        })
        print(f"   交易哈希: {tx_result}")

        print("\n❌ 常见误区: 不验证工具调用结果")
        print("✅ 正确做法: 验证结果、处理异常、重试机制")

    def simulate_tool_call(self, tool: str, function: str, params: Any) -> Any:
        """模拟工具调用"""
        import random

        if tool == "uniswap":
            return {"liquidity": random.randint(1000, 10000)}
        elif tool == "chainlink":
            return random.uniform(1800, 2200)
        elif tool == "ethers":
            return "0x" + hex(random.randint(1000000, 9999999))[2:]
        return None

    # ==================== 7. AI Coding 演示 ====================
    def demonstrate_ai_coding(self):
        """演示 AI 编程"""
        print("\n💻 7. AI Coding 演示")
        print("=" * 50)

        # 生成测试用例
        print("AI 生成的测试用例:")
        test_cases = self.generate_test_cases()
        for test in test_cases:
            print(f"- {test['description']}")
            print(f"  代码: {test['code']}")
            print()

        print("❌ 常见误区: 依赖 AI 生成所有代码")
        print("✅ 正确做法: AI 作为助手，关键逻辑需要人工编写")

    def generate_test_cases(self) -> List[Dict]:
        """生成测试用例"""
        return [
            {
                "description": "测试代币转账",
                "code": "it('should transfer tokens', async () => {\n    await token.transfer(addr1, 100);\n    expect(await token.balanceOf(addr1)).to.equal(100);\n});"
            },
            {
                "description": "测试代币余额",
                "code": "it('should return correct balance', async () => {\n    expect(await token.balanceOf(owner)).to.equal(1000000);\n});"
            }
        ]

    # ==================== 8. Guardrails 演示 ====================
    def demonstrate_guardrails(self):
        """演示安全边界"""
        print("\n🛡️ 8. Guardrails 演示")
        print("=" * 50)

        guardrails = {
            "交易前": [
                "最大金额检查",
                "白名单验证",
                "滑点保护"
            ],
            "运行时": [
                "紧急停止",
                "频率限制",
                "异常监控"
            ],
            "用户保护": [
                "冷静期",
                "损失限制",
                "教育要求"
            ]
        }

        for category, protections in guardrails.items():
            print(f"{category}:")
            for protection in protections:
                print(f"  - {protection}")
            print()

        print("❌ 常见误区: Guardrails 可以阻止所有风险")
        print("✅ 正确做法: 多层防护 + 持续监控")

    # ==================== 9. Tracing 演示 ====================
    def demonstrate_tracing(self):
        """演示追踪技术"""
        print("\n🔍 9. Tracing 演示")
        print("=" * 50)

        # 模拟跨链桥追踪
        print("跨链桥交易追踪:")
        trace_steps = [
            {"time": "10:00:00", "action": "发起转账", "status": "pending"},
            {"time": "10:00:15", "action": "链上确认", "status": "confirmed"},
            {"time": "10:01:00", "action": "中继开始", "status": "processing"},
            {"time": "10:02:00", "action": "到达目标链", "status": "completed"}
        ]

        for step in trace_steps:
            print(f"{step['time']} - {step['action']} [{step['status']}]")

        print("\n追踪的价值:")
        print("- 审计追踪")
        print("- 性能优化")
        print("- 故障诊断")
        print("- 合规证明")

    # ==================== 10. Human-in-the-Loop 演示 ====================
    def demonstrate_human_in_loop(self):
        """演示人工监督"""
        print("\n👥 10. Human-in-the-Loop 演示")
        print("=" * 50)

        decision_points = [
            {"decision": "合约部署", "reason": "安全验证需要人工判断"},
            {"decision": "价格设置", "reason": "市场策略需要人工经验"},
            {"decision": "危机处理", "reason": "情感智慧无法替代"}
        ]

        print("需要人工决策的关键节点:")
        for point in decision_points:
            print(f"- {point['decision']}: {point['reason']}")

        print("\n🤝 平衡 AI 和人类智慧:")
        print("AI 处理: 重复性任务、数据分析、模式识别")
        print("人类处理: 战略决策、道德判断、创新思维")

    # ==================== 运行所有演示 ====================
    def run_all_demos(self):
        """运行所有演示"""
        print("🎯 AI × Web3 概念实践演示")
        print("=" * 60)

        demonstrations = [
            ("LLM", self.demonstrate_llm),
            ("Prompt Engineering", self.demonstrate_prompt_engineering),
            ("Context Window", self.demonstrate_context_window),
            ("Workflow", self.demonstrate_workflow),
            ("Agent", self.demonstrate_agent),
            ("Tool Use", self.demonstrate_tool_use),
            ("AI Coding", self.demonstrate_ai_coding),
            ("Guardrails", self.demonstrate_guardrails),
            ("Tracing", self.demonstrate_tracing),
            ("Human-in-the-Loop", self.demonstrate_human_in_loop)
        ]

        for name, demo_func in demonstrations:
            demo_func()
            input("\n按 Enter 键继续下一个演示...")
            print("\n" + "=" * 60 + "\n")

        print("\n✅ 所有演示完成!")
        print("\n记住:")
        print("- AI 是强大的助手，不是替代品")
        print("- 安全永远是第一位的")
        print("- 人类的判断不可或缺")
        print("- 持续学习和改进是关键")

# ==================== 主程序 ====================
if __name__ == "__main__":
    demo = AIConceptsDemo()
    demo.run_all_demos()