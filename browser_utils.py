from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_page_html(url, wait_for_tag='body', timeout=10):
    """
    使用 Selenium 打开指定 URL，并等待页面内容加载完成，返回完整的 HTML 源码。

    参数:
        url (str): 要访问的网页地址
        wait_for_tag (str): 要等待加载的 HTML 标签名（如 'body' 或 'div.content'）
        timeout (int): 最大等待时间（秒）

    返回:
        str: 页面的完整 HTML 源码
    """
    options = Options()
    options.add_argument("--headless")  # 无头模式
    options.add_argument("--disable-gpu")
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(url)

    try:
        # 等待指定元素加载完成
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, wait_for_tag))
        )
        return driver.page_source
    finally:
        driver.quit()