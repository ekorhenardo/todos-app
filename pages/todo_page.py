from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TodoPage:
    def __init__(self, driver):
        self.driver = driver

    def add_todo(self, text):
        field = self.driver.find_element(By.XPATH, '//*[@id="todo-input"]')
        field.send_keys(text + Keys.ENTER)

    def edit_todo(self, text):
        field = self.driver.find_element(By.XPATH, '//*[@data-testid="todo-item-label"]')
        ActionChains(self.driver).double_click(field).perform()
        edit_field = self.driver.find_element(By.XPATH, '//*[@data-testid="todo-item"]//*[@id="todo-input"]')
        edit_field.send_keys(" " + text + Keys.ENTER)

    def click_checkbox(self):
        field = self.driver.find_element(By.XPATH, '//*[@data-testid="todo-item-toggle"]')
        field.click()

    def click_delete(self):
        field = self.driver.find_element(By.XPATH, '//*[@data-testid="todo-item-label"]')
        ActionChains(self.driver).move_to_element(field).perform()

        button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@data-testid="todo-item-button"]'))
        )
        button.click()

    def click_button_clear_completed(self):
        field = self.driver.find_element(By.XPATH, '//*[@class="clear-completed"]')
        field.click()

    def get_active_todo_count(self):
        field = self.driver.find_element(By.XPATH, '//*[@class="todo-count"]')
        text = field.text
        count = int(text.split()[0]) if text else 0
        return count
    
    def click_active_filter(self):
        field = self.driver.find_element(By.XPATH, '//*[text()="Active"]')
        field.click()

    def get_active_todo_count(self):
        field = self.driver.find_elements(By.XPATH, '//*[@data-testid="todo-item" and not(contains(@class, "completed"))]')
        count = len(field)
        return count
    
    def click_completed_filter(self):
        field = self.driver.find_element(By.XPATH, '//*[text()="Completed"]')
        field.click()

    def get_completed_todo_count(self):
        field = self.driver.find_elements(By.XPATH, '//*[@class="completed"]')
        count = len(field)
        return count
    
    def get_todo_text(self):
        field = self.driver.find_element(By.XPATH, '//*[@data-testid="todo-item-label"]')
        return field.text
    
    def get_all_todo_count(self):
        field = self.driver.find_elements(By.XPATH, '//*[@data-testid="todo-item-label"]')
        count = len(field)
        return count