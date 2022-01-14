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
wget https://github.com/HidekiHrk/br-ani-cli/releases/download/v0.1/br-ani-cli-linux-v0_1.tar.gz
```

Se você preferir utilizar **curl** ao invés de **wget**:

```sh
curl -O https://github.com/HidekiHrk/br-ani-cli/releases/download/v0.1/br-ani-cli-linux-v0_1.tar.gz
```

2. Extraia o pacote e finalize a instalação:

```
mkdir br-ani-cli-linux
tar -xzvf br-ani-cli-linux-v0_1.tar.gz -C ./br-ani-cli-linux
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
