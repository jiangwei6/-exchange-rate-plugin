#!/usr/env python3
# -*- coding: UTF-8 -*-

from flask import Flask, request, send_file, make_response
from flask_cors import CORS
import json
import requests
from datetime import datetime
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://agents.baidu.com"}})

# 使用免费的汇率API (ExchangeRate-API)
EXCHANGE_API_BASE_URL = "https://open.er-api.com/v6/latest"

# 支持的货币代码映射
CURRENCY_NAMES = {
    "USD": "美元",
    "CNY": "人民币",
    "EUR": "欧元",
    "GBP": "英镑",
    "JPY": "日元",
    "KRW": "韩元",
    "HKD": "港币",
    "AUD": "澳元",
    "CAD": "加元",
    "CHF": "瑞士法郎",
    "SGD": "新加坡元",
    "THB": "泰铢",
    "MYR": "马来西亚林吉特",
    "IDR": "印尼盾",
    "PHP": "菲律宾比索",
    "VND": "越南盾",
    "INR": "印度卢比",
    "BRL": "巴西雷亚尔",
    "RUB": "俄罗斯卢布",
    "ZAR": "南非兰特"
}

def make_json_response(data, status_code=200):
    response = make_response(json.dumps(data), status_code)
    response.headers["Content-Type"] = "application/json"
    return response

def get_exchange_rate(from_currency, to_currency):
    """
    获取汇率信息
    使用免费的ExchangeRate-API
    """
    try:
        # 构建API请求URL
        url = f"{EXCHANGE_API_BASE_URL}/{from_currency}"
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get("result") == "success":
            rates = data.get("conversion_rates", {})
            
            if to_currency in rates:
                rate = rates[to_currency]
                return {
                    "success": True,
                    "rate": rate,
                    "last_updated": data.get("time_last_update_utc", "")
                }
            else:
                return {
                    "success": False,
                    "error": f"不支持的目标货币: {to_currency}"
                }
        else:
            return {
                "success": False,
                "error": "获取汇率数据失败"
            }
            
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": f"网络请求错误: {str(e)}"
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"处理请求时发生错误: {str(e)}"
        }

@app.route("/get_exchange_rate")
async def get_exchange_rate_api():
    """
    汇率查询接口
    """
    from_currency = request.args.get('from_currency', '').upper()
    to_currency = request.args.get('to_currency', '').upper()
    amount = float(request.args.get('amount', 1))
    
    # 参数验证
    if not from_currency or not to_currency:
        return make_json_response({
            "success": False,
            "error": "请提供源货币和目标货币代码"
        }, 400)
    
    if from_currency not in CURRENCY_NAMES:
        return make_json_response({
            "success": False,
            "error": f"不支持的源货币: {from_currency}"
        }, 400)
    
    if to_currency not in CURRENCY_NAMES:
        return make_json_response({
            "success": False,
            "error": f"不支持的目标货币: {to_currency}"
        }, 400)
    
    # 获取汇率
    result = get_exchange_rate(from_currency, to_currency)
    
    if result["success"]:
        rate = result["rate"]
        converted_amount = amount * rate
        
        response_data = {
            "success": True,
            "from_currency": from_currency,
            "to_currency": to_currency,
            "rate": rate,
            "amount": amount,
            "converted_amount": round(converted_amount, 2),
            "last_updated": result["last_updated"],
            "from_currency_name": CURRENCY_NAMES.get(from_currency, from_currency),
            "to_currency_name": CURRENCY_NAMES.get(to_currency, to_currency)
        }
        
        return make_json_response(response_data)
    else:
        return make_json_response({
            "success": False,
            "error": result["error"]
        }, 500)

@app.route("/get_supported_currencies")
async def get_supported_currencies():
    """
    获取支持的货币列表
    """
    return make_json_response({
        "success": True,
        "currencies": CURRENCY_NAMES
    })

@app.route("/logo.png")
async def plugin_logo():
    """
    注册用的：返回插件的 logo，要求 48 x 48 大小的 png 文件.
    注意：API路由是固定的，事先约定的。
    """
    return send_file('logo.png', mimetype='image/png')

@app.route("/.well-known/ai-plugin.json")
async def plugin_manifest():
    """
    注册用的：返回插件的描述文件，描述了插件是什么等信息。
    注意：API 路由是固定的，事先约定的。
    """
    # 使用环境变量获取域名，如果没有则使用请求的域名
    base_url = os.environ.get('BASE_URL', request.host_url.rstrip('/'))
    with open(".well-known/ai-plugin.json", encoding="utf-8") as f:
        text = f.read().replace("PLUGIN_HOST", base_url)
        return text, 200, {"Content-Type": "application/json"}

@app.route("/.well-known/openapi.yaml")
async def openapi_spec():
    """
    注册用的：返回插件所依赖的插件服务的API接口描述，参照 openapi 规范编写。
    注意：API 路由是固定的，事先约定的。
    """
    # 使用环境变量获取域名，如果没有则使用请求的域名
    base_url = os.environ.get('BASE_URL', request.host_url.rstrip('/'))
    with open(".well-known/openapi.yaml", encoding="utf-8") as f:
        text = f.read().replace("PLUGIN_HOST", base_url)
        return text, 200, {"Content-Type": "text/yaml"}

@app.route("/example.yaml")
async def exampleSpec():
    with open("example.yaml") as f:
        text = f.read()
        return text, 200, {"Content-Type": "text/yaml"}

@app.route('/')
def index():
    return 'Welcome to Exchange Rate Plugin!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8081))
    app.run(debug=True, host='0.0.0.0', port=port) 