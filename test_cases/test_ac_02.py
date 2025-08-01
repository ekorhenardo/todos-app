from pages.todo_page import TodoPage
from selenium.webdriver.common.by import By

def test_ac_02(driver):
    todo = TodoPage(driver)
    todo.add_todo("test automation")
    todo.click_checkbox()
    
    completed = driver.find_elements(By.XPATH, '//*[@class="completed"]')
    assert len(completed) > 0, "Todo was not marked as completed"