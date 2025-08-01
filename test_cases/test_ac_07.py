import time

from pages.todo_page import TodoPage

def test_ac_07(driver):
    todo = TodoPage(driver)
    todo.add_todo("test automation")
    todo.edit_todo("edited")
    edited_text = todo.get_todo_text()
    assert edited_text == "test automation edited", f"Expected todo text to be 'test automation edited', but got '{edited_text}'"
    
    time.sleep(5)