# br-ani-cli

Anime Watching Interface for BRASILEIROS

Dependências:

- MPV
- python (apenas caso você queira buildar pela source)
- pipenv (apenas caso você queira buildar pela source)

### Instalação (LINUX):

1. Baixe o pacote tar:

```sh
cd ~/Downloads
wget https://github.com/HidekiHrk/br-ani-cli/releases/latest/download/br-ani-cli-linux.tar.gz
```

Se você preferir utilizar **curl** ao invés de **wget**:

```sh
curl -OL https://github.com/HidekiHrk/br-ani-cli/releases/latest/download/br-ani-cli-linux.tar.gz
```

2. Extraia o pacote e finalize a instalação:

```
mkdir br-ani-cli-linux
tar -xzvf br-ani-cli-linux.tar.gz -C ./br-ani-cli-linux
cd br-ani-cli-linux
sudo ./install.sh
```

### Buildar pela source (LINUX):

```bash
git clone https://github.com/HidekiHrk/br-ani-cli.git
cd br-ani-cli/
pipenv install
make build
make create-build-release
cd dist
sudo ./install.sh
```
