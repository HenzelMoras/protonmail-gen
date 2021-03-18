import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def inject_input(driver, keys, xpath=None, id=None, css_selector=None):
    if xpath:
        input_box = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
    elif id:
        input_box = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.ID, id)))
    else:
        input_box = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))
    for i in keys:
        input_box.send_keys(i)
        time.sleep(.1)
    time.sleep(.9)

def scroll_click_element(driver, xpath):
    scroll_element = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
                            (By.XPATH, xpath)))

    driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)
    driver.find_element_by_xpath(xpath).click()
    time.sleep(0.4)

def switch_frame(driver, tag_name=None, class_name=None):
    if tag_name:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.TAG_NAME, tag_name)))
        driver.switch_to.frame(driver.find_element_by_tag_name(tag_name))
    else:
        WebDriverWait(driver, 60).until(EC.visibility_of_element_located(
            (By.CLASS_NAME, class_name)))
        driver.switch_to.frame(driver.find_element_by_class_name(class_name))
    time.sleep(.5)

def click_element(driver, xpath):
    
    WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.XPATH, xpath)))

    driver.find_element_by_xpath(xpath).click()   
    time.sleep(.5)