# Anya Shop Bot - In final stages of development;

[Leia este documento em português.](README.pt-br.md)

The purpose of this project is to share the knowledge I gained during development of this bot. 
I hope to inspire others to embark on this journey and discover that programming is accessible 
to anyone who is willing to learn and seek information.

My motivation was to fulfill my dream of developing a bot, something I have desired since my 
first contact with bots and programming 22 years ago. Recently, I completed a full-stack 
developer course, and even though I didn't acquire the knowledge specifically for this, I decided
to try to achieve what I once thought was impossible and I succeeded =)

## Installation and Prerequisites

#### Before using the bot, it is necessary to ensure that some tools are installed on your system:

### 1) Python
The Anya Shop Bot is developed in Python, which is necessary for running the 
program.
- [Python for Windows](https://www.python.org/downloads/windows/)
- [Python for Linux](https://www.python.org/downloads/source/)
- [Python for macOS](https://www.python.org/downloads/macos/)

### 2) Tesseract
This is an OCR (Optical Character Recognition) that allows the bot to convert 
images into text. It is essential installing for the program to function correctly.
- [Tesseract for Windows](https://github.com/UB-Mannheim/tesseract/wiki)
- [Tesseract for Linux or macOS](https://tesseract-ocr.github.io/tessdoc/Installation.html)

Later in the setup, you will need to have the directory path where Tesseract was installed 
copied. Follow the instructions below:

**Windows** 

During Tesseract installation, you will need to choose the directory,
as shown in the image:

![Tesseract Installation](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/tesseract-windows.jpg)

By default, the directory will be C:\Program Files\Tesseract-OCR copy this path and keep
it saved.

**Linux or macOS** 

After installing Tesseract, run the following command in your terminal:
```bash 
which tesseract
```
This command will return the path to the Tesseract executable. For example:
```bash 
/usr/bin/tesseract
```
Next, copy the path that is returned, but make sure to remove /tesseract from the end.
So, if the command returns /usr/bin/tesseract, you'll copy only /usr/bin as the path.
The final result will be:
```bash 
/usr/bin
```
#
#### To ensure the bot works correctly, please configure the game and screen according to the following specifications:

### 1) Language

- Diablo 2 Resurrected must be set to English.

### 2) Resolution and Display mode

- The resolution should be 1280x720.
- The game should be in Windowed Mode.

![Resolution and Display mode](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/display_settings.jpg)

### 3) Gameplay Settings

- In accessibility Large Font Mode should be enabled.

![Gameplay Settings](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/large_mode_settings.jpg)

## First Release
[Version 0.1 - Initial Release](https://github.com/johnovelli/anya-shop-bot/releases/tag/v0.1)

This is the first version of the bot. It includes basic functionality but still has room
for improvement. More features and enhancements will be added in future updates.

**Download Links:**
- [anya-shop-bot.zip](https://github.com/johnovelli/anya-shop-bot/releases/download/v0.1/anya-shop-bot-main.zip)
- [anya-shop-bot.tar.gz](https://github.com/johnovelli/anya-shop-bot/archive/refs/tags/v0.1.tar.gz)
