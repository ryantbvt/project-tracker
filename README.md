# project-tracker

# Virtual Environment
'python3 -m venv venv'

## Activating virtual environment
'source venv/bin/activate'

## Download dependencies
'pip install -r requirements.txt'

## Running code on normal virtual environment
'uvicorn app.main:app --host 127.0.0.1 --port 4460 --reload'

# Poetry
## Initializing poetry
'pip3 install poetry'

## How to run
'poetry run uvicorn app.main:app --host 127.0.0.1 --port 4460 --reload'
