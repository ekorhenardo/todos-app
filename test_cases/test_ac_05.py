from pages.todo_page import TodoPage

def test_ac_05(driver):
    todo = TodoPage(driver)

    for i in range(3):
        todo.add_todo("test automation {i}")

    todo.click_checkbox()
    count = todo.get_active_todo_count()
    
    assert count == 2, f"Expected 2 active todos, but got {count}"