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