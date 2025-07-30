#!/usr/bin/env python3
"""
配置测试脚本 - 验证URL配置是否正确
"""

import requests
import json

def test_config():
    """测试配置文件是否正确生成"""
    base_url = "http://localhost:8081"
    
    print("测试配置文件生成...")
    print("=" * 50)
    
    # 测试ai-plugin.json
    try:
        response = requests.get(f"{base_url}/.well-known/ai-plugin.json")
        if response.status_code == 200:
            data = response.json()
            print("✅ ai-plugin.json 生成成功")
            print(f"   API URL: {data.get('api', {}).get('url', 'N/A')}")
            print(f"   Logo URL: {data.get('logo_url', 'N/A')}")
            print(f"   Examples URL: {data.get('examples', {}).get('url', 'N/A')}")
        else:
            print(f"❌ ai-plugin.json 生成失败: {response.status_code}")
    except Exception as e:
        print(f"❌ 测试ai-plugin.json失败: {str(e)}")
    
    # 测试openapi.yaml
    try:
        response = requests.get(f"{base_url}/.well-known/openapi.yaml")
        if response.status_code == 200:
            yaml_content = response.text
            print("\n✅ openapi.yaml 生成成功")
            if "PLUGIN_HOST" not in yaml_content:
                print("   ✅ URL已正确替换")
            else:
                print("   ❌ URL未正确替换")
        else:
            print(f"\n❌ openapi.yaml 生成失败: {response.status_code}")
    except Exception as e:
        print(f"\n❌ 测试openapi.yaml失败: {str(e)}")

def test_api_endpoints():
    """测试API端点"""
    base_url = "http://localhost:8081"
    
    print("\n\n测试API端点...")
    print("=" * 50)
    
    endpoints = [
        "/get_exchange_rate?from_currency=USD&to_currency=CNY&amount=100",
        "/get_supported_currencies",
        "/logo.png",
        "/example.yaml"
    ]
    
    for endpoint in endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}")
            if response.status_code == 200:
                print(f"✅ {endpoint} - 正常")
            else:
                print(f"❌ {endpoint} - 错误: {response.status_code}")
        except Exception as e:
            print(f"❌ {endpoint} - 异常: {str(e)}")

if __name__ == "__main__":
    print("汇率插件配置测试工具")
    print("请确保服务器正在运行在 http://localhost:8081")
    print("=" * 50)
    
    test_config()
    test_api_endpoints()
    
    print("\n\n测试完成!")
    print("\n如果所有测试都通过，说明配置正确！")
    print("现在可以部署到Railway并注册到百度智能体平台了。") 