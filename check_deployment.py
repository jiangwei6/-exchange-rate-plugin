#!/usr/bin/env python3
"""
部署检查脚本 - 验证Railway部署配置
"""

import os
import sys

def check_files():
    """检查必要的文件是否存在"""
    required_files = [
        'server.py',
        'requirements.txt',
        'Procfile',
        'runtime.txt',
        '.well-known/ai-plugin.json',
        '.well-known/openapi.yaml',
        'example.yaml',
        'logo.png'
    ]
    
    print("检查必要文件...")
    missing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - 缺失")
            missing_files.append(file)
    
    return len(missing_files) == 0

def check_server_code():
    """检查服务器代码"""
    print("\n检查服务器代码...")
    
    try:
        with open('server.py', 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 检查必要的导入
        required_imports = ['flask', 'flask_cors', 'requests', 'os']
        missing_imports = []
        
        for imp in required_imports:
            if imp not in content:
                missing_imports.append(imp)
        
        if missing_imports:
            print(f"❌ 缺少导入: {missing_imports}")
            return False
        else:
            print("✅ 导入检查通过")
        
        # 检查环境变量处理
        if 'os.environ.get' in content:
            print("✅ 环境变量处理正确")
        else:
            print("❌ 环境变量处理可能有问题")
            return False
        
        # 检查端口配置
        if 'PORT' in content:
            print("✅ 端口配置正确")
        else:
            print("❌ 端口配置可能有问题")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ 读取服务器代码失败: {str(e)}")
        return False

def check_requirements():
    """检查依赖文件"""
    print("\n检查依赖文件...")
    
    try:
        with open('requirements.txt', 'r') as f:
            content = f.read()
            
        required_packages = ['flask', 'flask-cors', 'requests']
        missing_packages = []
        
        for pkg in required_packages:
            if pkg not in content:
                missing_packages.append(pkg)
        
        if missing_packages:
            print(f"❌ 缺少依赖: {missing_packages}")
            return False
        else:
            print("✅ 依赖检查通过")
            return True
            
    except Exception as e:
        print(f"❌ 读取依赖文件失败: {str(e)}")
        return False

def main():
    print("Railway部署配置检查工具")
    print("=" * 50)
    
    files_ok = check_files()
    server_ok = check_server_code()
    requirements_ok = check_requirements()
    
    print("\n" + "=" * 50)
    print("检查结果:")
    
    if files_ok and server_ok and requirements_ok:
        print("✅ 所有检查通过！可以部署到Railway")
        print("\n部署步骤:")
        print("1. 推送代码到GitHub")
        print("2. 在Railway中连接GitHub仓库")
        print("3. Railway会自动检测并部署")
        print("4. 获取Railway域名并注册到百度智能体平台")
    else:
        print("❌ 存在问题，请修复后再部署")
        if not files_ok:
            print("  - 缺少必要文件")
        if not server_ok:
            print("  - 服务器代码有问题")
        if not requirements_ok:
            print("  - 依赖配置有问题")

if __name__ == "__main__":
    main() 