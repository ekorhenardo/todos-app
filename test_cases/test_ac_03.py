from pages.todo_page import TodoPage

def test_ac_03(driver):
    todo = TodoPage(driver)
    todo.add_todo("test automation")
    todo.click_delete()
    all_todo_count = todo.get_all_todo_count()

    assert all_todo_count == 0, f"Expected 0 todos, but found {all_todo_count}"