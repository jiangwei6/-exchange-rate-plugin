#!/usr/bin/env python3
"""
汇率插件测试脚本
"""

import requests
import json

def test_exchange_rate():
    """测试汇率查询功能"""
    base_url = "http://localhost:8081"
    
    print("测试汇率查询插件...")
    print("=" * 50)
    
    # 测试汇率查询
    test_params = {
        "from_currency": "USD",
        "to_currency": "CNY",
        "amount": 100
    }
    
    try:
        response = requests.get(f"{base_url}/get_exchange_rate", params=test_params)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print("✅ 汇率查询成功")
                print(f"   汇率: 1 {data['from_currency']} = {data['rate']} {data['to_currency']}")
                print(f"   转换: {data['amount']} {data['from_currency']} = {data['converted_amount']} {data['to_currency']}")
                print(f"   更新时间: {data['last_updated']}")
            else:
                print(f"❌ 查询失败: {data.get('error', '未知错误')}")
        else:
            print(f"❌ HTTP错误: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ 连接错误: 请确保服务器正在运行")
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")

def test_supported_currencies():
    """测试支持的货币列表"""
    base_url = "http://localhost:8081"
    
    print("\n测试支持的货币列表...")
    print("=" * 50)
    
    try:
        response = requests.get(f"{base_url}/get_supported_currencies")
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                currencies = data.get('currencies', {})
                print(f"✅ 成功获取支持的货币列表，共 {len(currencies)} 种货币")
                print("支持的货币:")
                for code, name in list(currencies.items())[:10]:  # 显示前10个
                    print(f"    {code}: {name}")
                if len(currencies) > 10:
                    print(f"    ... 还有 {len(currencies) - 10} 种货币")
            else:
                print(f"❌ 获取失败: {data.get('error', '未知错误')}")
        else:
            print(f"❌ HTTP错误: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ 连接错误: 请确保服务器正在运行")
    except Exception as e:
        print(f"❌ 测试失败: {str(e)}")

if __name__ == "__main__":
    print("汇率插件测试工具")
    print("请确保服务器正在运行在 http://localhost:8081")
    print("=" * 50)
    
    test_exchange_rate()
    test_supported_currencies()
    
    print("\n测试完成!") 