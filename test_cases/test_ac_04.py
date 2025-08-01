from pages.todo_page import TodoPage

def test_ac_04(driver):
    todo = TodoPage(driver)

    for i in range(2):
        todo.add_todo(f"test automation {i}")

    todo.click_checkbox()
    todo.click_button_clear_completed()
    all_tasks_count = todo.get_all_todo_count()

    assert all_tasks_count == 1, f"Expected 1 tasks todos, but got {all_tasks_count}"