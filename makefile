start:
	pipenv run python main.py

build:
	pipenv run pyinstaller --name="br-ani-cli" --onefile main.py

install:
	cp ./dist/br-ani-cli /usr/bin

uninstall:
	rm /usr/bin/br-ani-cli
