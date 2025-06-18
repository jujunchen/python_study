# 爬取url的html
from flask import Flask, request, jsonify
import requests
import re
import xml.etree.ElementTree as ET
import time
from urllib.parse import urlparse
from bs4 import BeautifulSoup


app = Flask(__name__)

def parse_wechat_message(xml_data):
    """解析微信服务器发来的 XML 消息"""
    root = ET.fromstring(xml_data)
    msg = {
        'ToUserName': root.find('ToUserName').text,
        'FromUserName': root.find('FromUserName').text,
        'CreateTime': root.find('CreateTime').text,
        'MsgType': root.find('MsgType').text,
        'Content': root.find('Content').text if root.find('Content') is not None else '',
        'MsgId': root.find('MsgId').text if root.find('MsgId') is not None else '',
        'Event': root.find('Event').text if root.find('Event') is not None else ''
    }
    return msg

@app.route('/wechat/index.html', methods=['GET', 'POST'])
def handle_wechat():
    if request.method == 'GET':
        # 微信验证服务器地址有效性
        echostr = request.args.get('echostr')
        return echostr or ''
    elif request.method == 'POST':
        # 处理微信推送的消息
        xml_data = request.data.decode('utf-8')
        msg = parse_wechat_message(xml_data)

        if msg['MsgType'] == 'text':
            content = msg['Content']
            # 构造请求 extract_html 的 URL
            target_url = f'https://cn.bing.com/search?q={content}电影在线免费观看&FPIG=FE0C3D532F5C4525B53F89AE74671D6A&first=1&FORM=PERE'
            # 执行次数
            result_html = extract_html(target_url, 0)

            if len(result_html) == 0:
                # 获取html内容
                result_html = extract_html(target_url, 2)
            
            
            result_text = f"为您从互联网找到以下电影资源：{result_html}";
        elif msg['MsgType'] == 'event':
            if msg['Event'] == 'subscribe':
                result_text = "欢迎关注，请输入电影名称 获取电影资源"
            else:
                result_text = "暂不支持该功能"
        else:

            result_text = "暂不支持该功能"

        # 返回微信要求的 XML 格式响应
        reply_xml = f"""
        <xml>
          <ToUserName><![CDATA[{msg['FromUserName']}]]></ToUserName>
          <FromUserName><![CDATA[{msg['ToUserName']}]]></FromUserName>
          <CreateTime>{int(time.time())}</CreateTime>
          <MsgType><![CDATA[text]]></MsgType>
          <Content><![CDATA[{result_text}]]></Content>
        </xml>
        """
        return reply_xml


def extract_html(target_url, size):
    # 设置请求头模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    
    try:
        all_content = ""
        for i in range(2):
            first = (i+size+1) * 10
            # 正则替换target_url中的first参数，first=10
            target_url = re.sub(r'first=\d+', 'first=' + str(first), target_url)
            # 发送 HTTP 请求
            response = requests.get(
                target_url,
                headers=headers,
                timeout=10,  # 设置超时时间
                allow_redirects=False  # 允许重定向
            )
            response.raise_for_status()  # 检查 HTTP 错误

            html_content = response.text

            pattern = r'<a\s+target\s*=\s*["\']_blank["\']\s+target\s*=\s*["\']_blank["\'][^>]*>(?:.|\n)*?</a>'
            matches = re.findall(pattern, html_content)
            # 拼接成字符串
            links = '\n'.join(matches)

            #生成数组对象
            soup = BeautifulSoup(links, 'html.parser')
            #拼接成a 标签的字符串,\n 分割，过滤掉url 是doubai, zhihu 的链接
            links = '\n'.join([f"URL:{a_tag.get('href')} 名称:{a_tag.get_text(strip=True)}" for a_tag in soup.find_all('a') if any(k in a_tag.get_text(strip=True) for k in ('在线观看', '电影观看'))])
            all_content += links
            # all_content的长度超过600，截取范围内的完整内容，并跳出循环
            if len(all_content) > 1200:
                all_content = all_content[all_content.rfind('\n', 0, 600):]
                break
        return all_content

    except requests.exceptions.RequestException as e:
        return jsonify({
            "error": "Failed to fetch URL",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)