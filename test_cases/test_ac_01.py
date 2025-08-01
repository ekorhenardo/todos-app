import time

from pages.todo_page import TodoPage

def test_ac_01(driver):
    todo = TodoPage(driver)
    todo.add_todo("test automation")
    
    time.sleep(5)