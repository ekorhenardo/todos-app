## Project Setup

Follow these steps to set up the development environment.

### 1. Clone the Repository

```bash
git clone https://github.com/ekorhenardo/todos-app.git
cd todos-app
```

### 2. Install Python via pyenv

Make sure `pyenv` is installed and working.

Then install the required Python version:

```bash
pyenv install 3.13.5
pyenv local 3.13.5
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Acceptance Criteria

The following criteria were used to guide test case development for the `todo-app`:

1. **AC01**: User can add a new todo by typing in the input field and pressing Enter.
2. **AC02**: User can mark a todo as completed by clicking its checkbox.
3. **AC03**: User can delete a todo by clicking the "X" button.
4. **AC04**: Completed todos can be cleared using the "Clear completed" button.
5. **AC05**: The list should reflect correct count of active items.
6. **AC06**: Filters (All, Active, Completed) should change the displayed list accordingly.
7. **AC07**: User can edit a todo by double clicking the input field and save the changes by pressing Enter.
8. **AC08**: The app should preserve todos on page reload (if persistence is expected).