start:
	pipenv run python main.py

build:
	pipenv run pyinstaller --name="br-ani-cli" --onefile main.py