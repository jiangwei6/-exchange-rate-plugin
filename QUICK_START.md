# 汇率查询插件 - 快速开始

## 🚀 快速部署

### 1. 本地测试
```bash
cd exchange_rate_plugin
pip install -r requirements.txt
python server.py
```

### 2. 部署到GitHub + Railway
1. 创建GitHub仓库并推送代码
2. 在Railway中连接GitHub仓库
3. 获取Railway域名
4. 更新配置文件中的URL
5. 注册到百度智能体平台

## 📁 文件结构
```
exchange_rate_plugin/
├── .well-known/
│   ├── ai-plugin.json          # 插件配置文件
│   └── openapi.yaml           # OpenAPI规范文件
├── .github/workflows/
│   └── deploy.yml             # GitHub Actions部署配置
├── server.py                   # 服务器代码
├── requirements.txt            # 依赖文件
├── example.yaml               # 示例文件
├── logo.png                   # 插件图标
├── test_plugin.py             # 测试脚本
├── railway.json               # Railway配置
├── README.md                  # 说明文档
├── DEPLOYMENT_GUIDE.md        # 详细部署指南
└── QUICK_START.md            # 快速开始指南
```

## 🔧 主要功能

### 支持的API
- `GET /get_exchange_rate` - 汇率查询
- `GET /get_supported_currencies` - 获取支持的货币列表

### 支持的货币
- USD (美元), CNY (人民币), EUR (欧元), GBP (英镑)
- JPY (日元), KRW (韩元), HKD (港币), AUD (澳元)
- CAD (加元), CHF (瑞士法郎), SGD (新加坡元)
- 以及更多...

## 🧪 测试

### 本地测试
```bash
python test_plugin.py
```

### API测试
- 汇率查询：`http://localhost:8081/get_exchange_rate?from_currency=USD&to_currency=CNY&amount=100`
- 支持的货币：`http://localhost:8081/get_supported_currencies`

## 📝 使用示例

用户可以通过以下方式使用插件：
1. "查询美元兑人民币的汇率"
2. "100美元等于多少人民币？"
3. "欧元兑日元的汇率是多少？"
4. "帮我转换500欧元到美元"
5. "支持哪些货币？"

## ⚙️ 配置说明

### 汇率API
使用免费的ExchangeRate-API，无需注册：
- 基础URL：`https://open.er-api.com/v6/latest`
- 支持实时汇率查询
- 有请求频率限制

### 服务器配置
- 端口：8081（本地）/ Railway自动分配
- 框架：Flask + Flask-CORS
- 支持百度智能体平台CORS

## 🔄 部署流程

1. **本地开发** → 测试功能
2. **GitHub** → 代码托管
3. **Railway** → 自动部署
4. **百度智能体平台** → 插件注册

## 📚 详细文档

- [README.md](README.md) - 完整功能说明
- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - 详细部署指南
- [百度智能体平台文档](https://agents.baidu.com/docs/develop/plugin/ability-plugin/basic/quick_pass/)

## 🛠️ 技术栈

- **后端**: Python + Flask
- **API**: ExchangeRate-API (免费)
- **部署**: Railway
- **CI/CD**: GitHub Actions
- **平台**: 百度智能体平台

## 📞 支持

如有问题，请查看：
1. [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) 中的故障排除部分
2. Railway部署日志
3. 服务器控制台输出 