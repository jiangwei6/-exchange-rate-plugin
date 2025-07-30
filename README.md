# 汇率查询插件

这是一个基于百度智能体平台的汇率查询插件，可以帮助用户查询实时汇率信息并进行货币转换。

## 功能特性

- 支持20种常用货币的汇率查询
- 实时获取最新汇率数据
- 支持货币转换计算
- 使用免费的汇率API，无需注册

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

### 2. 启动服务器
```bash
python server.py
```

服务器将在 http://localhost:8081 启动

### 3. 测试API
访问以下地址测试：
- 汇率查询：http://localhost:8081/get_exchange_rate?from_currency=USD&to_currency=CNY&amount=100
- 支持的货币：http://localhost:8081/get_supported_currencies

## 部署到Railway

### 1. 准备文件
确保以下文件都已准备好：
- `server.py`
- `requirements.txt`
- `.well-known/ai-plugin.json`
- `.well-known/openapi.yaml`
- `example.yaml`
- `logo.png`

### 2. 部署步骤
1. 将代码推送到GitHub
2. 在Railway中连接GitHub仓库
3. Railway会自动检测Python项目并部署
4. 获取Railway提供的域名

### 3. 更新配置
部署完成后，需要更新以下文件中的URL：
- `.well-known/ai-plugin.json` 中的 `PLUGIN_HOST`
- `.well-known/openapi.yaml` 中的服务器URL

## 使用示例

用户可以通过以下方式使用插件：

1. "查询美元兑人民币的汇率"
2. "100美元等于多少人民币？"
3. "欧元兑日元的汇率是多少？"
4. "帮我转换500欧元到美元"
5. "支持哪些货币？"

## 文件结构

```
exchange_rate_plugin/
├── .well-known/
│   ├── ai-plugin.json          # 插件配置文件
│   └── openapi.yaml           # OpenAPI规范文件
├── server.py                   # 服务器代码
├── requirements.txt            # 依赖文件
├── example.yaml               # 示例文件
├── logo.png                   # 插件图标
└── README.md                  # 说明文档
```

## 注意事项

- 汇率数据来源于免费的ExchangeRate-API
- 汇率数据会定期更新
- 建议在生产环境中使用付费API以获得更稳定的服务 