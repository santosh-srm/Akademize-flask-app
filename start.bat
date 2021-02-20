set FLASH_ENV=development
set FLASH_APP=src/app.py

python -m venv .venv
.venv\Scripts\activate

flask run
