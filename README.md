
# Anya Shop Bot

[Leia este documento em português.](README.pt-br.md)

Anya Shop Bot is a tool designed to automate the process of checking and purchasing specific items
in *Diablo 2 Resurrected*, focusing on studying the game item randomization. This bot is intended for 
**OFFLINE** use only, serving purely educational and experimental purposes.

The goal of this project is to share the knowledge I gained during development. 
I hope to inspire others to embark on this journey and discover that programming is accessible 
to anyone who is willing to learn and seek information.

My motivation was to fulfill my dream of developing a bot, something I have desired since my 
first contact with bots and programming 22 years ago.Recently, I decided to attempt to 
achieve what I once thought was impossible, and I succeeded =)

<br>

# Contents

1. [What Does Anya Shop Bot Do?](#what-does-anya-shop-bot-do-)
2. [Installation and Prerequisites](#installation-and-prerequisites)
   - [Python](#1-python)
   - [Tesseract](#2-tesseract)
   - [Game and Screen Configuration](#1-language)
3. [Downloading and Configuring the Bot](#downloading-and-configuring-the-bot)
   - [Downloading the Files](#1-download-the-files)
   - [Installing Dependencies](#2-installing-dependencies)
   - [Configuring the Bot](#3-configuring-the-bot)
4. [Running the Bot](#running-the-bot)
   - [Prepare the Game](#1-prepare-the-game)
   - [Open the Bot Runner](#2-open-the-bot-runner)
   - [Starting the Bot](#3-starting-the-bot)
5. [Releases](#releases)
   - [First Release](#first-release)

<br>

## What Does Anya Shop Bot Do ?

<br>

The bot automates the process of checking and purchasing items using Optical Character
Recognition (OCR).
Interact with npc Anya, looking for specific items that match the attributes given. 

It specifically searches for:

- **Armors** with the suffix "The Whale" that contain life and are socketed.
- **Trap Claws** with assassin or trap skills and lighting sentry skills.

You can define the exact parameters witch the bot will search for:

- Minimum life percentage and minimum number of sockets for armors.

- Minimum assassin or trap skills and minimum lighting sentry skills for claws.

If an item meets your criteria, the bot will automatically purchase it.

After interacting with Anya, the bot will leave and return to town through
the red portal, refreshing her inventory. Then repeat the process until the bot 
is paused.

This tool can save you countless hours of manual checking. Additionally, 
analyzing the log of images for items that met at least one criterion can be 
fascinating, offering insights into the game item randomization.

<br>

## Installation and Prerequisites

#### Before using the bot, it is necessary to ensure that some tools are installed on your system:

### 1) Python
Anya Shop Bot is developed in Python, which is necessary for running the 
program.
- [Python for Windows](https://www.python.org/downloads/windows/)
- [Python for Linux](https://www.python.org/downloads/source/)
- [Python for macOS](https://www.python.org/downloads/macos/)

### 2) Tesseract
OCR (Optical Character Recognition) that allows the bot to convert 
images into text. It is essential installing for the program to function correctly.
- [Tesseract for Windows](https://github.com/UB-Mannheim/tesseract/wiki)
- [Tesseract for Linux or macOS](https://tesseract-ocr.github.io/tessdoc/Installation.html)

Later in the setup, you will need to have the directory path where Tesseract was installed 
copied. Follow the instructions below:

**Windows:** 

During Tesseract installation, you will need to choose the directory,
as shown in the image:

![Tesseract Installation](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/tesseract-windows.jpg)

By default, the directory will be *C:\Program Files\Tesseract-OCR*. 
If your installation directory is different, make sure to copy the path of your 
specific installation and keep it saved.

**Linux or macOS:** 

After installing Tesseract, run the following command in your terminal:
```markdown
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

- Diablo 2 Resurrected must be in English.

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

Choose one of the files below to download Anya Shop 
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

**1- Tesseract Path Configuration**

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

    - add an extra backslash (` \ `) in each path segment. For example:

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

**2- Configuring the Bot Parameters**

**Armor:**

  - **min_life:** Defines the minimum life percentage an armor item must 
have to be considered by the bot. This value should be between 
1 and 99
- **min_sockets:** Specifies the minimum number of sockets that the 
armor must have to be considered. This value should be between 1 and 4.

  Example:
  ```ini
  [params]
  min_life = 90
  min_sockets = 3
  ```
**Claw:** 
- **min_skill:** Defines the minimum number of assassin or trap 
skills an item must have. This value should be between 1 and 3.
- **min_has_skill:** Specifies the minimum number of lightning
sentry skills an item must have. This value should also be 
between 1 and 3.

  Example:
  ```ini
  [params]
  min_skill = 1
  min_has_skill = 2
  ```

<br>

## Running the bot

### 1) Prepare the Game:

- Ensure that the game is open and is configured according to the 
instructions provided in the README.
- Your character is positioned near Ana and the portal,
as shown in the image below
  ![character position](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/character_position.jpg)



### 2) Open the Bot Runner:

- Navigate to the folder where you extracted the bot files.
- Locate the run.py file inside this folder.
- Double-click on the run.py file to open the bot.
- A window like this will open:

  ![Bot Runner](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/bot_runner.jpg)


### 3) Starting the Bot:

- After opening the Bot Runner, follow the instructions 
provided in the window to configure and start the bot.
- Before running the bot, ensure that the Bot Runner window 
is overlaid on top of the Diablo 2 Resurrected window, as shown in the image below:

  ![Window position](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/window_position.jpg)

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
