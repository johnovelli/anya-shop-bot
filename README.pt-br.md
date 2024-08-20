# Anya Shop Bot - Em fase final de desenvolvimento

O propósito deste projeto é compartilhar os conhecimentos que aprendi
durante o desenvolvimento deste bot. Quero inspirar
outras pessoas a embarcarem nessa jornada e descobrirem que programação é 
acessível a todos que tiverem vontade de aprender e buscar informações.

Minha motivação foi realizar meu sonho de desenvolver um bot,
algo que desejei desde meus primeiros contatos com bots e programação há 22
anos atrás. Recentemente, concluí um curso de desenvolvedor
full-stack e mesmo que não tenha aprendido os conhecimentos para isso,
decidi tentar realizar o que achava impossível e consegui =)

## Instalação e Pré-Requisitos
Antes de usar o bot é necessário garantir que algumas ferramentas 
estejam instaladas em seu sistema:

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

**Windows -** Durante a instalação do Tesseract você precisará escolher o diretório, como mostrado na imagem:

![Instalação do Tesseract](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/tesseract-windows.jpg)

Por padrão, o diretório será C:\Program Files\Tesseract-OCR copie este caminho e 
mantenha salvo.

**Linux or macOS -**  Após instalar o Tesseract, execute o seguinte comando em seu terminal:
```bash
which tesseract
```
Este comando retornará o caminho para o executável do Tesseract. Por exemplo:
```bash 
/usr/bin/tesseract
```
ou
```bash 
/usr/local/bin/tesseract
```
Em seguida, copie o caminho que é retornado, mas certifique-se de remover /tesseract do final.
Portanto, se o comando retornar /usr/bin/tesseract, você copiara apenas /usr/bin como o caminho.
O resultado final será:
```bash 
/usr/bin/
```