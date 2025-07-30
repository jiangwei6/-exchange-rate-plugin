# 汇率查询插件

这是一个基于百度智能体平台的汇率查询插件，可以帮助用户查询实时汇率信息并进行货币转换。

## 功能特性

- 支持20种常用货币的汇率查询
- 实时获取最新汇率数据
- 支持货币转换计算
- 使用免费的汇率API，无需注册
- **动态URL配置**：自动根据部署环境生成正确的URL

## 支持的货币

- USD (美元)
- CNY (人民币)
- EUR (欧元)
- GBP (英镑)
- JPY (日元)
- KRW (韩元)
- HKD (港币)
- AUD (澳元)
- CAD (加元)
- CHF (瑞士法郎)
- SGD (新加坡元)
- THB (泰铢)
- MYR (马来西亚林吉特)
- IDR (印尼盾)
- PHP (菲律宾比索)
- VND (越南盾)
- INR (印度卢比)
- BRL (巴西雷亚尔)
- RUB (俄罗斯卢布)
- ZAR (南非兰特)

## 本地开发

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 配置环境变量
复制环境变量示例文件：
```bash
cp env.example .env
```

编辑 `.env` 文件，设置本地开发环境：
```
BASE_URL=http://localhost:8081
PORT=8081
```

### 3. 启动服务器
```bash
python server.py
```

服务器将在 http://localhost:8081 启动

### 4. 测试插件
运行测试脚本：
```bash
python test_plugin.py
```

运行配置测试：
```bash
python test_config.py
```

运行部署检查：
```bash
python check_deployment.py
```

或手动测试：
- 汇率查询：http://localhost:8081/get_exchange_rate?from_currency=USD&to_currency=CNY&amount=100
- 支持的货币：http://localhost:8081/get_supported_currencies
- 插件配置：http://localhost:8081/.well-known/ai-plugin.json

## 部署到Railway

### 1. 部署前检查
运行部署检查脚本确保所有配置正确：
```bash
python check_deployment.py
```

### 2. 准备文件
确保以下文件都已准备好：
- `server.py` - 服务器代码
- `requirements.txt` - 依赖文件
- `Procfile` - Railway启动命令
- `runtime.txt` - Python版本
- `railway.json` - Railway配置
- `.well-known/ai-plugin.json` - 插件配置
- `.well-known/openapi.yaml` - OpenAPI规范
- `example.yaml` - 示例文件
- `logo.png` - 插件图标

### 3. 部署步骤
1. 将代码推送到GitHub
2. 在Railway中连接GitHub仓库
3. Railway会自动检测Python项目并部署
4. 获取Railway提供的域名

### 4. 环境变量配置
Railway会自动设置以下环境变量：
- `PORT`: 服务器端口
- `BASE_URL`: 你的Railway域名

插件会自动根据环境变量生成正确的URL，无需手动修改配置文件。

### 5. 故障排除

如果部署失败，请检查：

#### 常见错误：No start command could be found
**解决方案**：
- 确保 `Procfile` 文件存在且内容为 `web: python server.py`
- 确保 `server.py` 文件在根目录
- 确保 `requirements.txt` 文件存在

#### 常见错误：Build failed
**解决方案**：
- 检查 `requirements.txt` 中的依赖是否正确
- 确保 `runtime.txt` 指定了正确的Python版本
- 检查代码语法是否正确

#### 常见错误：Port already in use
**解决方案**：
- 确保代码中使用 `os.environ.get('PORT', 8081)` 获取端口
- Railway会自动分配端口

## 使用示例

用户可以通过以下方式使用插件：

1. "查询美元兑人民币的汇率"
2. "100美元等于多少人民币？"
3. "欧元兑日元的汇率是多少？"
4. "帮我转换500欧元到美元"
5. "支持哪些货币？"

## 动态URL配置

本插件使用动态URL配置，会根据部署环境自动生成正确的URL：

### 本地开发
- 环境变量：`BASE_URL=http://localhost:8081`
- 自动生成：`http://localhost:8081/.well-known/openapi.yaml`

### Railway部署
- 环境变量：`BASE_URL=https://your-app-name.railway.app`
- 自动生成：`https://your-app-name.railway.app/.well-known/openapi.yaml`

### 配置文件
- `ai-plugin.json` 中的 `PLUGIN_HOST` 会被自动替换
- `openapi.yaml` 中的 `PLUGIN_HOST` 会被自动替换
- 无需手动修改任何配置文件

## 文件结构

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
├── test_plugin.py             # 功能测试脚本
├── test_config.py             # 配置测试脚本
├── check_deployment.py        # 部署检查脚本
├── railway.json               # Railway配置
├── Procfile                   # Railway启动命令
├── runtime.txt                # Python版本
├── env.example                # 环境变量示例
├── start.bat                  # Windows启动脚本
├── README.md                  # 说明文档
├── DEPLOYMENT_GUIDE.md        # 详细部署指南
└── QUICK_START.md            # 快速开始指南
```

## 注意事项

- 汇率数据来源于免费的ExchangeRate-API
- 汇率数据会定期更新
- 建议在生产环境中使用付费API以获得更稳定的服务
- **无需手动修改URL配置**：插件会自动处理
- 部署前请运行 `python check_deployment.py` 检查配置 