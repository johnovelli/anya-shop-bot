# Anya Shop Bot - 

[Leia este documento em português.](README.pt-br.md)

The purpose of this project is to share the knowledge I gained during development of this bot. 
I hope to inspire others to embark on this journey and discover that programming is accessible 
to anyone who is willing to learn and seek information.

My motivation was to fulfill my dream of developing a bot, something I have desired since my 
first contact with bots and programming 22 years ago. Recently, I completed a full-stack 
developer course, and even though I didn't acquire the knowledge specifically for this, I decided
to try to achieve what I once thought was impossible and I succeeded =)

<br>

## What Does Anya Shop Bot Do ?

The Anya Shop Bot automates the process of checking items in Diablo 2 Resurrected 
using Optical Character Recognition (OCR). It specifically searches for:

- **Armors** with the suffix "The Whale" that contain life and are socketed.
- **Trap Claws** with assassin or trap skills and lighting sentry skills.

You can define the exact parameters witch the bot will search for:

- Minimum life percentage and minimum number of sockets for armors.

- Minimum assassin or trap skills and minimum lighting sentry skills for claws.

When an item meets your criteria, the bot will automatically
purchase it.

This tool can save you countless hours of manual checking, letting you focus on the 
fun parts of the game while the bot handles the repetitive tasks. Additionally, 
analyzing the log of images for items that met at least one criterion can be 
fascinating, offering insights into the game item randomization.



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

**Windows:** 

During Tesseract installation, you will need to choose the directory,
as shown in the image:

![Tesseract Installation](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/tesseract-windows.jpg)

By default, the directory will be C:\Program Files\Tesseract-OCR copy this path and keep
it saved.

**Linux or macOS:** 

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

<br>

## Downloading and Configuring the Bot

### 1) Download the Files

Choose one of the files below to download the Anya Shop 
Bot based on your operating system:

- [**anya-shop-bot-0.1.zip**](https://github.com/johnovelli/anya-shop-bot/releases/download/v0.1/anya-shop-bot-0.1.zip) for systems that use ZIP files (Windows).
- [**anya-shop-bot.tar.gz**](https://github.com/johnovelli/anya-shop-bot/releases/download/v0.1/anya-shop-bot-0.1.tar) for systems that use TAR files (Linux or macOS).

### 2) Installing Dependencies

After downloading and extracting the bot folder:
1. Ensure that Python is installed on your system.
2. Navigate to the folder where you extracted the bot folder and open it.
3. Locate the file named `install_requirements.py`.
4. Double-click on `install_requirements.py` to run it. This will install all 
the necessary dependencies.

### 3) Configuring the Bot

**Locate and edit the Config File**

In the folder where you extracted the bot, find the file named 
`config.ini`, and open it using a text editor of your choice, ex: (Notepad on
Windows, TextEdit on macOS, etc.).

1- **Tesseract Path Configuration**

Inside [tesseract] section, you need to specify the path where 
Tesseract OCR is installed, which you copied earlier during the 
installation process.

If you are unsure of where Tesseract is installed, scroll to the installation 
steps at the beginning of the document to find instructions on how to locate 
the path.

- **Windows:**

    If you installed Tesseract in the default
    directory `C:\Program Files\Tesseract-OCR`, you do not need to make 
    any changes.

    If installed elsewhere, specify the full path to the Tesseract executable
    and format it correctly:

    - add an extra backslash(` \ `) in each path segment. For example:
  
    ```ini
    [tesseract]
    pytesseract_path = C:\\Your\\Custom\\Path\\To\\Tesseract-OCR
    ```
  
- **Linux or macOS:**

  Paste the copied path earlier. For example:
    ```ini
    [tesseract]
    pytesseract_path = /usr/local/bin
    ```
  
<br>

2- ** **

Inside [tesseract] section, you need to specify the path where
Tesseract OCR is installed, which you copied earlier during the
installation process.

<br>

## Releases

### First Release
[Version 0.1 - Initial Release](https://github.com/johnovelli/anya-shop-bot/releases/tag/v0.1)

This is the first version of the bot. It includes basic functionality, 
still has room for improvement. More features and enhancements will be added
in future updates.

**Download Links:**
- [anya-shop-bot-0.1.zip](https://github.com/johnovelli/anya-shop-bot/releases/download/v0.1/anya-shop-bot-0.1.zip)
- [anya-shop-bot.tar-0.1.gz](https://github.com/johnovelli/anya-shop-bot/releases/download/v0.1/anya-shop-bot-0.1.tar)
