from pages.todo_page import TodoPage

def test_ac_02(driver):
    todo = TodoPage(driver)
    todo.add_todo("test automation")
    todo.click_checkbox()
    completed = todo.get_completed_todo_count()
    
    assert completed == 1, f"Expected 1 completed todo, but got {completed}"