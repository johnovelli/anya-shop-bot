# Anya Shop Bot - 

O propósito deste projeto é compartilhar os conhecimentos que aprendi
durante o desenvolvimento deste bot. Quero inspirar
outras pessoas a embarcarem nessa jornada e descobrirem que programação é 
acessível a todos que tiverem vontade de aprender e buscar informações.

Minha motivação foi realizar meu sonho de desenvolver um bot,
algo que desejei desde meus primeiros contatos com bots e programação há 22
anos atrás. Recentemente, concluí um curso de desenvolvedor
full-stack e mesmo que não tenha aprendido os conhecimentos para isso,
decidi tentar realizar o que achava impossível e consegui =)

<br>

## O Que Faz o Anya Shop Bot?

O Anya Shop Bot automatiza o processo de verificação de itens em Diablo 2 Resurrected 
usando Reconhecimento Óptico de Caracteres (OCR). Ele procura especificamente por:

- **Armaduras** com o sufixo "The Whale" que possuem vida e sejam socketed
- **Trap Claws** com assassin ou trap skills e lighting sentry skills.

Você pode definir os parâmetros exatos que o bot irá buscar, incluindo:

- Percentual mínimo de vida e número mínimo de sockets para armaduras.

- Mínimo de assassin oo trap skills e mínimo de lighting sentry skills para garras.

Quando um item atende aos seus critérios, o bot o comprará automaticamente.

Essa ferramenta pode economizar inúmeras horas de verificação manual, permitindo que 
você se concentre nas partes divertidas do jogo enquanto o bot lida com as tarefas 
repetitivas. Além disso, analisar o log de imagens de itens que atenderam a pelo menos 
um critério pode ser fascinante, oferecendo insights sobre a randomização de itens 
no jogo.

<br>

## Instalação e Pré-Requisitos
##### Antes de usar o bot é necessário garantir que algumas ferramentas estejam instaladas em seu sistema:

### 1) Python
O Anya Shop Bot é desenvolvido em Python, que é necessário para rodar o 
programa.
- [Python para Windows](https://www.python.org/downloads/windows/)
- [Python para Linux](https://www.python.org/downloads/source/)
- [Python para macOS](https://www.python.org/downloads/macos/)

### 2) Tesseract
Este é um OCR (Optical Character Recognition) que permite o bot converter 
imagens em texto. É essencial instalar para que o programa funcione corretamente.
- [Tesseract para Windows](https://github.com/UB-Mannheim/tesseract/wiki)
- [Tesseract para Linux ou macOS](https://tesseract-ocr.github.io/tessdoc/Installation.html)

Mais adiante na configuração você precisara ter o caminho de diretório aonde o Tesseract 
foi instalado copiado, siga as instruções abaixo:

**Windows -** Durante a instalação do Tesseract você precisará escolher o diretório, 
como mostrado na imagem:

![Instalação do Tesseract](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/tesseract-windows.jpg)

Por padrão, o diretório será C:\Program Files\Tesseract-OCR copie este caminho e 
mantenha salvo.

<br>

**Linux or macOS -**  Após instalar o Tesseract, execute o seguinte comando em seu terminal:
```bash
which tesseract
```
Este comando retornará o caminho para o executável do Tesseract. Por exemplo:
```bash 
/usr/bin/tesseract
```
Em seguida copie o caminho que é retornado, mas certifique-se de remover /tesseract do final.
Portanto, se o comando retornar /usr/bin/tesseract, você copiara apenas /usr/bin como o caminho.
O resultado final será:
```bash 
/usr/bin/
```
#
#### Para garantir o funcionamento correto do bot, configure o jogo e a tela conforme as seguintes especificações:

### 1) Idioma

- Diablo 2 Resurrected deve estar em Inglês.

### 2) Resolução e Modo de Exibição

- A resolução deve ser configurada para 1280x720.
- O jogo deve estar no Modo Janela.

![Resolução e Modo de Exibição](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/display_settings.jpg)

### 3) Configurações de Jogabilidade

- Em acessibility o Modo de Fonte Grande deve estar habilitado.

![Configurações de Jogabilidade](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/large_mode_settings.jpg)

<br>

## Downloading and Configuring the Bot

### 1) Baixar os Arquivos

Escolha um dos arquivos abaixo para baixar o Anya Shop Bot com base no seu 
sistema operacional:

- [**anya-shop-bot-0.1.zip**](https://github.com/johnovelli/anya-shop-bot/releases/download/v0.1/anya-shop-bot-0.1.zip) for systems that use ZIP files (Windows).
- [**anya-shop-bot.tar.gz**](https://github.com/johnovelli/anya-shop-bot/releases/download/v0.1/anya-shop-bot-0.1.tar) for systems that use TAR files (Linux or macOS).

### 2) Installing Dependencies

Após baixar e extrair a pasta do bot:
1. Certifique-se de que o Python está instalado no seu sistema.
2. Navegue até a pasta onde você extraiu o bot e abra-a.
3. Localize o arquivo chamado install_requirements.py.
4. Dê um duplo clique em install_requirements.py para executá-lo. 
Isso instalará todas as dependências necessárias.

### 3) Configurando o Bot

**Localize e Edite o Arquivo de Config**

1- **Configuração do Caminho do Tesseract**

Dentro da seção [tesseract], você precisa especificar o caminho onde o Tesseract OCR 
está instalado, que você copiou anteriormente durante o processo de instalação.

Se você não souber onde o Tesseract está instalado, role até as etapas de instalação no 
início do documento para encontrar instruções sobre como localizar o caminho.

- **Windows:**



## Primeira Versão
[Version 0.1 - Initial Release](https://github.com/johnovelli/anya-shop-bot/releases/tag/v0.1)

Esta é a primeira versão do bot. Ela inclui funcionalidades básicas, ainda há espaço
para melhorias. Mais recursos e aprimoramentos serão adicionados em futuras atualizações.

**Links para Download:**
- [anya-shop-bot.zip](https://github.com/johnovelli/anya-shop-bot/releases/download/v0.1/anya-shop-bot-main.zip)
- [anya-shop-bot.tar.gz](https://github.com/johnovelli/anya-shop-bot/archive/refs/tags/v0.1.tar.gz)

