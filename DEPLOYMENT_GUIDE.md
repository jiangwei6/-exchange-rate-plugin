# 汇率插件部署指南

## 本地开发测试

### 1. 环境准备
确保你的系统已安装：
- Python 3.7 或更高版本
- pip 包管理器

### 2. 安装依赖
```bash
cd exchange_rate_plugin
pip install -r requirements.txt
```

### 3. 配置环境变量
复制环境变量示例文件：
```bash
cp env.example .env
```

编辑 `.env` 文件，设置本地开发环境：
```
BASE_URL=http://localhost:8081
PORT=8081
```

### 4. 启动服务器
```bash
python server.py
```

服务器将在 http://localhost:8081 启动

### 5. 测试插件
运行测试脚本：
```bash
python test_plugin.py
```

或手动测试：
- 汇率查询：http://localhost:8081/get_exchange_rate?from_currency=USD&to_currency=CNY&amount=100
- 支持的货币：http://localhost:8081/get_supported_currencies

## 部署到GitHub

### 1. 创建GitHub仓库
1. 在GitHub上创建新仓库
2. 将代码推送到仓库：
```bash
cd exchange_rate_plugin
git init
git add .
git commit -m "Initial commit: Exchange Rate Plugin"
git branch -M main
git remote add origin https://github.com/your-username/your-repo-name.git
git push -u origin main
```

### 2. 设置GitHub Secrets
在GitHub仓库设置中添加Railway Token：
1. 进入仓库 Settings > Secrets and variables > Actions
2. 添加新的secret：`RAILWAY_TOKEN`
3. 值从Railway获取（见下文）

## 部署到Railway

### 1. 创建Railway项目
1. 访问 [Railway](https://railway.app/)
2. 使用GitHub账号登录
3. 点击 "New Project"
4. 选择 "Deploy from GitHub repo"
5. 选择你的GitHub仓库

### 2. 获取Railway Token
1. 在Railway项目中，进入Settings
2. 找到 "Tokens" 部分
3. 创建新的token
4. 复制token值并添加到GitHub Secrets

### 3. 配置环境变量
在Railway项目设置中添加环境变量：
- `PORT`: 8081（Railway会自动设置）
- `BASE_URL`: 部署后会自动设置为你的Railway域名

### 4. 部署
Railway会自动检测Python项目并部署。部署完成后，你会获得一个域名，类似：
`https://your-app-name.railway.app`

## 环境变量配置

### 本地开发
创建 `.env` 文件：
```
BASE_URL=http://localhost:8081
PORT=8081
```

### Railway部署
Railway会自动设置以下环境变量：
- `PORT`: 服务器端口
- `BASE_URL`: 你的Railway域名

你可以在Railway项目设置中手动添加或修改环境变量。

## 注册到百度智能体平台

### 1. 准备文件
插件会自动根据环境变量生成正确的URL，无需手动修改配置文件。

### 2. 上传插件
1. 访问 [百度智能体平台](https://agents.baidu.com/)
2. 点击「创建插件」
3. 上传以下文件：
   - `ai-plugin.json`（从你的Railway域名获取）
   - `openapi.yaml`（从你的Railway域名获取）
   - `logo.png`

### 3. 获取插件配置文件
访问以下URL获取配置文件：
- `https://your-app-name.railway.app/.well-known/ai-plugin.json`
- `https://your-app-name.railway.app/.well-known/openapi.yaml`

### 4. 测试插件
在平台上测试以下查询：
- "查询美元兑人民币的汇率"
- "100美元等于多少人民币？"
- "欧元兑日元的汇率是多少？"
- "支持哪些货币？"

## 故障排除

### 常见问题

1. **部署失败**
   - 检查 `requirements.txt` 是否正确
   - 确保所有依赖都已列出
   - 查看Railway部署日志

2. **插件无法访问**
   - 检查Railway域名是否正确
   - 确认服务正在运行
   - 测试健康检查端点

3. **汇率API错误**
   - 检查网络连接
   - 确认汇率API服务正常
   - 查看服务器日志

4. **环境变量问题**
   - 检查Railway环境变量设置
   - 确认 `BASE_URL` 是否正确
   - 查看服务器日志中的环境变量

### 日志查看
- Railway: 在项目页面查看部署日志
- 本地: 查看控制台输出
- 服务器: 访问 `/` 端点测试

## 维护和更新

### 1. 代码更新
```bash
git add .
git commit -m "Update plugin"
git push origin main
```
Railway会自动重新部署。

### 2. 监控服务
- 定期检查Railway项目状态
- 监控API响应时间
- 查看错误日志

### 3. 备份配置
- 保存所有配置文件
- 备份环境变量
- 记录部署步骤

## 性能优化

1. **添加缓存**
   - 对汇率数据进行缓存
   - 设置合理的缓存过期时间

2. **错误处理**
   - 添加重试机制
   - 实现降级策略

3. **监控告警**
   - 添加健康检查
   - 设置性能监控 