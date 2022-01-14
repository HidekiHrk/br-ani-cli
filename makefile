start:
	pipenv run python main.py

build:
	pipenv run pyinstaller --name="br-ani-cli" --onefile main.py

install:
	cp ./dist/br-ani-cli /usr/bin

uninstall:
	rm /usr/bin/br-ani-cli

create-build-release:
	echo "#!/bin/bash" | cat > dist/install.sh; \
	echo "cp ./br-ani-cli /usr/bin" | cat >> dist/install.sh; \
	chmod +x dist/install.sh; \
	cd dist; \
	tar -czvf br-ani-cli.tar.gz ./br-ani-cli ./install.sh; \
	cd ..
