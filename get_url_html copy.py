# 爬取url的html工具
from flask import Flask, request, jsonify
import requests
import re

from urllib.parse import urlparse
from bs4 import BeautifulSoup


app = Flask(__name__)


#&FPIG=FDE2F0FA8CC44B01B7CC0E61206FD896&first=10&FORM=PERE

@app.route('/get_html', methods=['GET'])
def extract_html():
    # 获取 URL 参数
    target_url = request.args.get('url')
    start_marker = request.args.get('start')  # 新增开始标记
    end_marker = request.args.get('end') 
    first = request.args.get('first') 
    
    # 验证 URL 是否存在
    if not target_url:
        return jsonify({"error": "Missing 'url' parameter"}), 400
    
    # 验证 URL 格式
    try:
        parsed_url = urlparse(target_url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            return jsonify({"error": "Invalid URL format"}), 400
    except Exception as e:
        return jsonify({"error": f"URL validation failed: {str(e)}"}), 400
    
    # 设置请求头模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    
    try:
        # first 字段 循环3次，每次+10,i 从1 开始

        all_content = ""
        for i in range(2):
            first = (i+1) * 10
            # 正则替换target_url中的first参数，first=10
            target_url = re.sub(r'first=\d+', 'first=' + str(first), target_url)
        
            # 发送 HTTP 请求
            response = requests.get(
                target_url,
                headers=headers,
                timeout=10,  # 设置超时时间
                allow_redirects=True  # 允许重定向
            )
            response.raise_for_status()  # 检查 HTTP 错误

            html_content = response.text


            # # 去除 CSS 内容（<style> 标签）
            # html_content = re.sub(r'<style[\s\S]*?</style>', '', html_content)

            # # 去除 JS 内容（<script> 标签）
            # html_content = re.sub(r'<script[\s\S]*?</script>', '', html_content)

            # # 去除 <link> 标签
            # html_content = re.sub(r'<link\s+[^>]*>', '', html_content)
            # # 去除div标签,<div>
            # html_content = re.sub(r'<div[\s\S]*?</div>', '', html_content)

            
            
            # 截取逻辑
            if start_marker and end_marker:
                    # 使用正则进行模糊匹配
                    pattern = re.escape(start_marker) + r'[\s\S]*?' + re.escape(end_marker)
                    match = re.search(pattern, html_content)

                    if not match:
                        return jsonify({"error": "Start or end marker not found"}), 404

                    html_content = match.group(0)
                    html_content = re.sub(r'(?!<a.*?>|</a>)[<].*?[>]', '', html_content)
                    all_content += html_content + '\n'

        # 返回 HTML 内容
        return all_content, 200, {'Content-Type': 'text/html; charset=utf-8'}

    
    except requests.exceptions.RequestException as e:
        return jsonify({
            "error": "Failed to fetch URL",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)