from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

linkedin_url = "https://www.linkedin.com"

# for _ in range(60):
cookie='AQEDAR-5vhEAQQpxAAABjr0voAIAAAGO4TwkAk0AEBsQT-m7_AnumImlN50zqbD3LgRnQpuzEuNJVZvp4Aswy8q5ZGJv2iuawwXKHEdCZdOSkwyZtYM6imGCDmhazAwXEqrdxweXOS6BEqbvhsVfB2Ub'
driver.get(linkedin_url)
driver.set_window_size(1920, 1080)
driver.add_cookie({
                'name': 'li_at',
                'value': cookie,
                'domain': '.linkedin.com'
            })
driver.get('https://www.linkedin.com/dashboard/')

results=[]

try:
    items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "pcd-analytics-view-item"))
    )
    for item in items:
        try:
            div_element = item.find_element(By.TAG_NAME, "div")
            value_element = div_element.find_element(By.CSS_SELECTOR, "p.text-body-large-bold.t-black")
            title_element = div_element.find_element(By.CSS_SELECTOR, "p.text-body-small.t-black--light")
            span_element = item.find_element(By.TAG_NAME, "span")
            timeframe_elements = span_element.find_elements(By.TAG_NAME, "span")
            trend_element=None
            try:
                trend_element = span_element.find_element(By.TAG_NAME, "strong")
            except Exception as e:
                print(e)

            trend_type = ''
            if len(timeframe_elements)>1:
                aria_label = timeframe_elements[0].get_attribute("aria-label")
                if 'decrease' in aria_label:
                    trend_type = '-ve'
                if 'increase' in aria_label:
                    trend_type = '+ve'
                    
            results.append({
                'value': value_element.text,
                'title': title_element.text,
                'timeframe': timeframe_elements[-1].text,
                'trend_type': trend_type,
                'trend': trend_element.text if trend_element else ''
            })
        except Exception as e:
            print("Title element not found", e)
except Exception as e:
    print("An exception occurred:", str(e))

driver.quit()
