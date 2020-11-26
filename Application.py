from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(r'./chromedriver.exe')  ## webdriver 경로 설정
# time.sleep(5)
driver.implicitly_wait(3)  ## 암시적 대기?

driver.get('https://www.naver.com')  ## 네이버 접속
print(driver.title)


#개봉영화 검색
elm = driver.find_elements(By.ID, 'query')[0]
elm.send_keys('개봉영화')

btn_elm = driver.find_elements(By.ID, 'search_btn')[0]
btn_elm.click()


# 두번째탭
driver.execute_script(
    "(function() { " +
    "window.open('https://www.naver.com', 'second');" +
    "})();"
)

driver.switch_to.window("second")
elm = driver.find_elements(By.ID, 'query')[0]
elm.send_keys('개봉예정영화')

btn_elm = driver.find_elements(By.ID, 'search_btn')[0]
btn_elm.click()


# 세번째 탭에서 클립보드에 있는것을 검색
driver.execute_script(
    "(function() { " +
    "window.open('https://www.naver.com', 'third');" +
    "})();"
)

driver.switch_to.window("third")

actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys('v').perform()

btn_elm = driver.find_elements(By.ID, 'search_btn')[0]
btn_elm.click()


# 네번째 탭에서 클립보드에 있는것을 검색
driver.execute_script(
    "(function() { " +
    "window.open('https://section.blog.naver.com', 'fourth');" +
    "})();"
)
driver.switch_to.window("fourth")
select_box = Select(driver.find_element(By.CLASS_NAME, 'selected_option'))
select_box.select_by_visible_text("블로그")


sleep(10)

driver.quit()
