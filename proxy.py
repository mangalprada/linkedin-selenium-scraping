from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.chrome import ChromeDriverManager

PROXY_HOST = 'brd.superproxy.io'
PROXY_PORT = 22225
PROXY_USERNAME = 'brd-customer-hl_3172d294-zone-residential_proxy2'
PROXY_PASSWORD = 'fdodbs86m6xt'
PROXY_COUNTRY = 'us' # Replace with the desired country code

proxy_url = f'http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{PROXY_HOST}:{PROXY_PORT}'
print(proxy_url)
# Set up proxy configuration
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_url
proxy.ssl_proxy = proxy_url

# Create desired capabilities and add proxy
capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

# Create a new Chrome WebDriver instance with the proxy settings
driver = webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=capabilities)

# Use the driver for web scraping
driver.get("http://www.tiktok.com")
# Perform scraping tasks...

# Close the browser when done
driver.quit()


