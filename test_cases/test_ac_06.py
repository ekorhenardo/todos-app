import time

from pages.todo_page import TodoPage

def test_ac_06(driver):
    todo = TodoPage(driver)

    for i in range(3):
        todo.add_todo("test automation")

    todo.click_checkbox()
    todo.click_active_filter()
    active_tasks_count = todo.get_active_todo_count()
    assert active_tasks_count == 2, f"Expected 2 active todos, but got {active_tasks_count}"
    time.sleep(3)

    todo.click_completed_filter()
    completed_tasks_count = todo.get_completed_todo_count()
    assert completed_tasks_count == 1, f"Expected 1 completed todo, but got {completed_tasks_count}"
    time.sleep(3)