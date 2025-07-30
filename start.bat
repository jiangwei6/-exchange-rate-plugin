@echo off
echo 正在启动汇率查询插件服务器...
echo.

REM 检查是否存在.env文件，如果不存在则复制示例文件
if not exist ".env" (
    echo 创建环境变量配置文件...
    copy env.example .env
)

echo 安装依赖...
pip install -r requirements.txt

echo.
echo 启动服务器...
python server.py

pause 