import time

from pages.todo_page import TodoPage

def test_ac_04(driver):
    todo = TodoPage(driver)
    todo.add_todo("test automation")
    todo.click_checkbox()
    todo.click_button_clear_completed()
    
    time.sleep(5)