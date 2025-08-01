import time

from pages.todo_page import TodoPage

def test_ac_03(driver):
    todo = TodoPage(driver)
    todo.add_todo("test automation")
    todo.click_delete()
    
    time.sleep(5)