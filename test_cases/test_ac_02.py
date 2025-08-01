import time

from pages.todo_page import TodoPage

def test_ac_02(driver):
    todo = TodoPage(driver)
    todo.add_todo("test automation")
    todo.click_checkbox()
    
    time.sleep(5)