/**
 * AI × Web3 概念实践示例
 *
 * 这个文件展示了如何在实际 Web3 开发中应用 AI 概念
 */

// ================== 1. LLM + Web3 ==================
/**
 * 大型语言模型在 Web3 开发中的应用
 * LLM 可以帮助理解复杂的智能合约逻辑和生成代码
 */
const llmWeb3Example = {
    // 使用 Claude 生成智能合约代码
    generateSmartContract: (prompt) => {
        // 示例 Prompt:
        // "创建一个安全的 NFT 铸造合约，包含以下功能：
        // 1. 限制每个地址最大铸造数量
        // 2. 支持白名单预铸
        // 3. 包含所有必要的安全检查"

        // AI 会生成类似这样的合约结构
        return `
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract NFTCollection is ERC721, Ownable {
    uint256 public maxPerAddress;
    uint256 public maxSupply;
    bytes32 public merkleRoot;
    mapping(address => uint256) public mintedPerAddress;

    constructor() ERC721("MyNFT", "MNFT") {
        maxPerAddress = 10;
        maxSupply = 10000;
    }

    function mint(address to, uint256 tokenId, bytes32[] calldata proof)
        external
        onlyWhenNotPaused
    {
        require(mintedPerAddress[to] < maxPerAddress, "Max per address reached");
        require(_totalMinted() < maxSupply, "Max supply reached");

        bool isValid = MerkleProof.verify(proof, merkleRoot, keccak256(abi.encodePacked(to)));
        require(isValid, "Invalid proof");

        _safeMint(to, tokenId);
        mintedPerAddress[to]++;
    }

    // 其他必要的函数...
}
        `;
    }
};

// ================== 2. Prompt Engineering ==================
/**
 * 在 Web3 开发中使用提示词工程
 * 精确的 Prompt 能获得更好的代码输出
 */
const promptEngineeringExample = {
    // 好的 Prompt 示例
    goodPrompt: "使用 React + TypeScript + ethers v6 创建一个简单的 NFT 铸造页面，包含：1) 显示当前代币信息 2) 铸造按钮 3) 铸造数量选择 4) 连接钱包功能 5) 显示铸造状态",

    // 差的 Prompt 示例
    badPrompt: "帮我做个 NFT 页面",

    // 改进后的 Prompt
    improvedPrompt: "创建一个 React 组件，用于 NFT 铸造。要求：
- 使用 ethers v6 连接区块链
- 实现钱包连接功能（使用 wagmi）
- 显示当前 NFT 名称和图片
- 添加数量选择器（1-10个）
- 实现铸造功能，包含价格计算
- 显示加载状态和错误提示
- 添加交易确认弹窗
- 使用 TypeScript 类型定义"
};

// ================== 3. Context Window + DeFi ==================
/**
 * 在复杂的 DeFi 协议开发中利用 Context Window
 * 将合约代码、测试用例、安全文档一起分析
 */
const contextWindowExample = {
    // 一次性提供给 AI 的完整上下文
    completeContext: {
        contractCode: `
            // Uniswap V3 流动性提供者合约
            contract LiquidityProvider {
                // 合约实现...
            }
        `,
        testCases: `
            // 测试文件...
        `,
        securityDocs: `
            // 安全注意事项：
            // 1. 滑点保护
            // 2. 重入攻击防护
            // 3. 价格预言机安全
        `,
        requirements: `
            // 需求文档：
            // 1. 支持多种代币对
            // 2. 动态调整手续费
            // 3. 提供流动性挖矿奖励
        `
    },

    // AI 基于完整上下文提供的改进建议
    aiSuggestions: {
        improvements: [
            "添加紧急停止功能以防极端市场波动",
            "实现手续费优化算法",
            "增加流动性奖励分配机制"
        ],
        securityChecks: [
            "验证价格预言机来源",
            "添加访问控制修饰符",
            "实现闪电贷防护"
        ]
    }
};

// ================== 4. Workflow + NFT Launch ==================
/**
 * NFT 项目发布的工作流设计
 * 将多个 AI 能力组合成完整流程
 */
const nftWorkflow = {
    steps: [
        {
            phase: "概念设计",
            aiTools: ["DALL-E", "Midjourney"],
            humanTasks: ["创意构思", "风格选择"],
            output: "艺术风格参考和概念图"
        },
        {
            phase: "生成素材",
            aiTools: ["Stable Diffusion", "Runway"],
            humanTasks: ["生成筛选", "质量把控"],
            output: "NFT 图片集合"
        },
        {
            phase: "合约开发",
            aiTools: ["Claude", "ChatGPT"],
            humanTasks: ["安全审计", "功能确认"],
            output: "经过审计的智能合约"
        },
        {
            phase: "前端开发",
            aiTools: ["Claude", "Copilot"],
            humanTasks: ["UI 设计", "用户体验优化"],
            output: "铸造网站和 DApp"
        },
        {
            phase: "测试部署",
            aiTools: ["Hardhat", "Truffle"],
            humanTasks: ["测试部署", "用户测试"],
            output: "生产环境就绪"
        },
        {
            phase: "营销推广",
            aiTools: ["AI 写手", "数据分析师"],
            humanTasks: ["策略制定", "社区运营"],
            output: "完整的营销方案"
        }
    ],

    guardrails: {
        contentSafety: "确保 NFT 内容符合平台政策",
        legalCompliance: "检查版权和知识产权问题",
    },

    humanInLoop: [
        "最终设计确认",
        "合约部署授权",
        "价格策略决定",
        "社区活动策划"
    ]
};

// ================== 5. Agent + DeFi Trading ==================
/**
 * DeFi 交易代理的智能体设计
 * 展示 Agent 如何自主执行复杂任务
 */
const defiAgent = {
    // Agent 的核心能力
    capabilities: {
        monitoring: "实时监控多个 DeFi 协议",
        analysis: "识别套利机会和异常",
        execution: "执行跨链交易",
        riskManagement: "动态调整风险参数",
        reporting: "生成交易报告和分析"
    },

    // 工具使用示例
    tools: {
        uniswapV3: {
            name: "Uniswap V3",
            functions: ["getPool", "swapExactInputSingle", "swapExactOutputSingle"]
        },
        aave: {
            name: "Aave",
            functions: ["deposit", "withdraw", "borrow"]
        },
        chainlink: {
            name: "Chainlink Price Feeds",
            functions: ["getLatestPrice", "getHistoricalPrices"]
        },
        ethers: {
            name: "Ethers.js",
            functions: ["sendTransaction", "estimateGas", "getBalance"]
        }
    },

    // 工作流程
    workflow: {
        1: "获取所有协议的最新价格和流动性数据",
        2: "计算潜在的套利利润",
        3: "评估风险（滑点、gas 费、MEV 保护）",
        4: "执行交易或进入监控状态",
        5: "更新持仓和风险参数"
    },

    // 安全限制
    constraints: {
        maxSlippage: "0.5%",
        maxGasPrice: "50 gwei",
        maxExposure: "10% of portfolio",
        prohibitedTokens: ["blacklisted addresses"]
    }
};

// ================== 6. Tool Use + Chain Interaction ==================
/**
 * AI 在 Web3 开发中的实际工具使用
 * 展示如何调用各种区块链工具
 */
const web3ToolUsage = {
    // 使用 ethers.js 调用区块链
    chainInteraction: async () => {
        const provider = new ethers.providers.JsonRpcProvider("https://polygon-rpc.com");

        // 获取余额
        const balance = await provider.getBalance("0x...");

        // 获取交易收据
        const receipt = await provider.getTransactionReceipt("0x...");

        // 监听事件
        contract.on("Transfer", (from, to, amount) => {
            console.log(`${from} sent ${amount} to ${to}`);
        });
    },

    // 使用 Hardhat 进行测试
    testing: async () => {
        const { run } = require("hardhat");

        // 运行测试
        await run("test", {
            files: ["test/token.test.js"]
        });
    },

    // 使用 IPFS 存储元数据
    ipfsStorage: async () => {
        const { create } = require("ipfs-http-client");
        const ipfs = create({ url: "https://ipfs.infura.io:5001" });

        // 上传元数据
        const result = await ipfs.add({
            path: "metadata.json",
            content: JSON.stringify({
                name: "My NFT",
                description: "Description",
                image: "ipfs://..."
            })
        });

        return result.path;
    }
};

// ================== 7. AI Coding + Smart Contract ==================
/**
 * AI 辅助智能合约开发示例
 * 展示如何用 AI 加速合约开发
 */
const aiCodingExample = {
    // AI 生成的代币合约
    aiGeneratedToken: `
// AI 生成的 ERC20 代币合约
// 包含：标准接口、安全检查、权限控制
contract MyToken is ERC20, Ownable {
    uint256 private constant _initialSupply = 1000000 * 10**18;

    constructor() ERC20("MyToken", "MTK") {
        _mint(msg.sender, _initialSupply);
    }

    // 安全的 mint 函数
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "ERC20: mint to the zero address");
        require(amount > 0, "Amount must be greater than 0");

        _mint(to, amount);
    }

    // 紧急停止功能
    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }
}
    `,

    // AI 生成的测试用例
    aiGeneratedTests: `
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("MyToken", function () {
    let token;
    let owner;
    let addr1;

    beforeEach(async function () {
        [owner, addr1] = await ethers.getSigners();
        const MyToken = await ethers.getContractFactory("MyToken");
        token = await MyToken.deploy();
    });

    it("Should have correct initial supply", async function () {
        expect(await token.totalSupply()).to.equal(1000000 * 10**18);
    });

    it("Should allow owner to mint", async function () {
        await token.mint(addr1.address, 100);
        expect(await token.balanceOf(addr1.address)).to.equal(100);
    });
});
    `
};

// ================== 8. Guardrails + DeFi Security ==================
/**
 * DeFi 应用中的安全边界设计
 * 展示如何设置各种保护机制
 */
const defiGuardrails = {
    // 交易前检查
    preTransactionChecks: {
        maxAmount: "限制单笔交易金额",
        tokenWhitelist: "只允许交易白名单代币",
        slippageProtection: "滑点保护",
        deadline: "交易过期时间",
        blacklistCheck: "地址黑名单检查"
    },

    // 运行时监控
    runtimeMonitoring: {
        liquidationProtection: "防止清算机器人攻击",
        flashLoanProtection: "闪电贷攻击防护",
        oracleValidation: "预言机数据验证",
        gasLimitProtection: "Gas 限制保护"
    },

    // 应急机制
    emergencyControls: {
        circuitBreaker: "断路器功能",
        freezeAll: "紧急冻结",
        emergencyWithdraw: "紧急提取",
        rateLimiting: "频率限制"
    },

    // 用户保护
    userProtection: {
        cooldownPeriod: "冷静期",
        approvalLimits: "授权限制",
        lossProtection: "损失保护",
        educationRequired: "必要教育"
    }
};

// ================== 9. Tracing + Cross-Chain Bridge ==================
/**
 * 跨链桥操作的完整追踪记录
 * 展示如何记录每一步操作
 */
const crossChainTracing = {
    // 交易追踪记录
    trace: {
        step1: {
            action: "发现套利机会",
            details: "ETH 在链A价格$2000，链B价格$2050",
            timestamp: "2026-05-20T10:30:00Z",
            decision: "执行套利"
        },
        step2: {
            action: "计算最优路径",
            details: "通过中继桥X，预计利润$40，gas费$5",
            timestamp: "2026-05-20T10:30:15Z",
            decision: "确认可行"
        },
        step3: {
            action: "批准转账",
            details: "在链A批准100 ETH给桥合约",
            timestamp: "2026-05-20T10:30:30Z",
            txHash: "0x...",
            status: "confirmed"
        },
        step4: {
            action: "跨链转账",
            details: "桥合约执行跨链操作",
            timestamp: "2026-05-20T10:31:00Z",
            status: "pending"
        },
        step5: {
            action: "接收确认",
            details: "在链B收到100 ETH",
            timestamp: "2026-05-20T10:32:00Z",
            status: "confirmed"
        },
        step6: {
            action: "套利执行",
            details: "在链B以$2050出售获利",
            timestamp: "2026-05-20T10:32:30Z",
            profit: "$35",
            status: "completed"
        }
    },

    // 分析报告
    analysis: {
        totalTime: "2分钟",
        gasCost: "$5",
        profit: "$35",
        roi: "700%",
        riskLevel: "低",
        lessons: "下次可考虑优化gas策略"
    }
};

// ================== 10. Human-in-the-Loop + NFT Launch ==================
/**
 * NFT 发行中的人工参与环节
 * 展示哪些步骤需要人工决策
 */
const humanInLoopExample = {
    // 需要人工决策的关键节点
    decisionPoints: {
        creativeDirection: {
            description: "艺术风格和主题确定",
            aiInput: "生成3种风格的概念图",
            humanDecision: "选择最终风格",
            reason: "确保符合品牌调性"
        },
        contractSecurity: {
            description: "智能合约安全审核",
            aiInput: "生成合约代码和安全检查",
            humanDecision: "审核并批准部署",
            reason: "金融安全不可妥协"
        },
        pricingStrategy: {
            description: "铸造价格策略",
            aiInput: "分析市场数据和建议价格区间",
            humanDecision: "确定最终价格",
            reason: "需要考虑市场反应"
        },
        communityManagement: {
            description: "社区活动策划",
            aiInput: "生成活动方案和宣传文案",
            humanDecision: "执行特定活动",
            reason: "需要人工情感连接"
        },
        crisisResponse: {
            description: "危机公关处理",
            aiInput: "监测异常和生成应对建议",
            humanDecision: "最终响应方案",
            reason: "需要人工判断和情感智慧"
        }
    },

    // 人工审核的流程
    reviewProcess: {
        initialReview: "概念和设计草稿",
        detailedReview: "技术实现细节",
        finalApproval: "发布前最终确认",
        postLaunchReview: "效果评估和调整"
    }
};

// ================== 导出示例 ==================
module.exports = {
    llmWeb3Example,
    promptEngineeringExample,
    contextWindowExample,
    nftWorkflow,
    defiAgent,
    web3ToolUsage,
    aiCodingExample,
    defiGuardrails,
    crossChainTracing,
    humanInLoopExample
};

/*
使用示例：
const examples = require('./ai-concepts-examples.js');
console.log(examples.defiAgent.capabilities);
*/