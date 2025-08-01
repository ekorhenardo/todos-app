from pages.todo_page import TodoPage

def test_ac_01(driver):
    todo = TodoPage(driver)
    todo.add_todo("test automation")
    todo_text = todo.get_todo_text()

    assert todo_text == "test automation", "Todo text does not match expected value"