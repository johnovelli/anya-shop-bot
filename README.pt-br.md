# Anya Shop Bot

<br>

Anya Shop Bot é uma ferramenta projetada para automatizar o processo de verificação e compra de itens 
específicos em ***Diablo 2 Resurrected***, com foco no estudo da randomização de itens do jogo. Este bot é 
destinado apenas para uso **OFFLINE**, servindo exclusivamente fins educativos e experimentais.

O objetivo deste projeto é compartilhar o conhecimento que adquiri durante o desenvolvimento. Espero inspirar 
outras pessoas a embarcarem nesta jornada e descobrirem que a programação é acessível a todos que estão dispostos a 
aprender e buscar informações.

Minha motivação foi realizar o sonho de desenvolver um bot, algo que desejo desde meu primeiro contato com bots e 
programação há 22 anos.
## Índice

1. [O Que Faz o Anya Shop Bot?](#o-que-faz-o-anya-shop-bot-)
2. [Instalação e Pré-Requisitos](#instalação-e-pré-requisitos)
   - [Python](#1-python)
   - [Tesseract](#2-tesseract)
   - [Configuração do Jogo e da Tela](#1-idioma)
3. [Baixando e Configurando o Bot](#baixando-e-configurando-o-bot)
   - [Baixando os Arquivos](#1-faça-download-dos-arquivos)
   - [Instalando as Dependências](#2-instalando-as-dependências)
   - [Configurando o Bot](#3-configurando-o-bot)
4. [Executando o Bot](#executando-o-bot)
   - [Prepare o Jogo](#1-prepare-o-jogo)
   - [Abra o Bot Runner](#2-abra-o-bot-runner)
   - [Inicie o Bot](#3-inicie-o-bot)
5. [Lançamentos](#lançamentos)
   - [Primeira Versão](#primeira-versão)

## O Que Faz o Anya Shop Bot ?

O bot automatiza o processo de verificação e compra de itens usando Reconhecimento Óptico de Caracteres (OCR). 
Ele interage com o NPC Anya, procurando por itens específicos que correspondam aos atributos fornecidos.

Ele procura especificamente por:

- **Armaduras** com o sufixo "The Whale" que contêm vida e engastes.
- **Garras de Armadilha** com habilidades de assassina ou para armadilhas e habilidades de lighting sentry.

Você pode definir os parâmetros exatos que o bot buscará::

- **Percentual mínimo de vida** e **número mínimo de engastes** para armaduras.

- **Habilidades mínimas de assassina ou para armadilhas** e **habilidades mínimas de lighting sentry** para garras.

Se um item atender aos seus critérios, o bot o comprará automaticamente.

Após interagir com Anya, o bot sairá e retornará à cidade através do portal vermelho, atualizando o inventário dela. 
Em seguida, repetirá o processo até que o bot seja pausado.


Esta ferramenta pode economizar inúmeras horas de verificação manual. Além disso, analisar o log de imagens para itens 
que atenderam a pelo menos um critério pode ser fascinante, oferecendo insights sobre a randomização de itens no jogo.
<br>

## Instalação e Pré-Requisitos

##### Antes de usar o bot, é necessário garantir que algumas ferramentas estejam instaladas no seu sistema. Todos os links fornecidos abaixo direcionarão você para as páginas oficiais de download de cada ferramenta:

### 1) Python
O Anya Shop Bot é desenvolvido em Python, que é necessário para executar o programa.
- [Python para Windows](https://www.python.org/downloads/windows/)
- [Python para Linux](https://www.python.org/downloads/source/)
- [Python para macOS](https://www.python.org/downloads/macos/)

### 2) Tesseract
OCR (Reconhecimento Óptico de Caracteres) que permite ao bot converter imagens em texto. 
É essencial instalá-lo para que o programa funcione corretamente.
- [Tesseract para Windows](https://github.com/UB-Mannheim/tesseract/wiki)
- [Tesseract para Linux ou macOS](https://tesseract-ocr.github.io/tessdoc/Installation.html)

Mais adiante na configuração você precisara ter o caminho de diretório aonde o Tesseract 
foi instalado copiado, siga as instruções abaixo:

**Windows -** Durante a instalação do Tesseract você precisará escolher o diretório, 
como mostrado na imagem:

![Instalação do Tesseract](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/tesseract-windows.jpg)

Por padrão, o diretório será *C:\Program Files\Tesseract-OCR*. Se o diretório de instalação for diferente,
certifique-se de copiar o caminho da sua instalação específica e manter salvo.

<br>

**Linux or macOS -**  Após instalar o Tesseract, execute o seguinte comando em seu terminal:
```markdown
which tesseract
```
Este comando retornará o caminho para o executável do Tesseract. Por exemplo:
```markdown
/usr/bin/tesseract
```
Em seguida copie o caminho que é retornado, mas certifique-se de remover /tesseract do final.
Portanto, se o comando retornar /usr/bin/tesseract, você copiara apenas /usr/bin como o caminho.
O resultado final será:
```markdown
/usr/bin
```
#
#### Para garantir o funcionamento correto do bot, configure o jogo e a tela conforme as seguintes especificações:

### 1) Idioma

- Diablo 2 Resurrected deve estar em Inglês.

### 2) Resolução e Modo de Exibição

- A resolução deve ser configurada para 1280x720.
- O jogo deve estar no Modo Janela.

![Resolução e Modo de Exibição](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/display_settings.jpg)

### 4) Gráficos

- O Predefinição Gráfica deve estar configurada como "Médio".

![Predefinição Gráfica](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/graphic_preset.jpg)

### 3) Configurações de Jogabilidade

- Em acessibilidade o Modo de Fonte Grande deve estar habilitado.

![Configurações de Jogabilidade](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/large_mode_settings.jpg)

<br>

## Baixando e configurando o Bot

### 1) Faça download dos Arquivos

Escolha um dos arquivos abaixo para baixar o Anya Shop Bot com base no seu 
sistema operacional:

- [**anya-shop-bot-0.1.zip**](https://github.com/johnovelli/anya-shop-bot/releases/download/v0.1/anya-shop-bot-0.1.zip) para sistemas que usam arquivos ZIP (Windows).
- [**anya-shop-bot.tar.gz**](https://github.com/johnovelli/anya-shop-bot/releases/download/v0.1/anya-shop-bot-0.1.tar) para sistemas que usam arquivos TAR files (Linux or macOS).

### 2) Instalando as Dependências

Após baixar e extrair a pasta do bot:
1. Certifique-se de que o Python está instalado no seu sistema.
2. Navegue até a pasta onde você extraiu a pasta do bot e abra-a.
3. Localize o arquivo chamado `install_requirements.py`.
4. Clique duas vezes em `install_requirements.py` para executá-lo. 
5. Isso instalará todas as dependências necessárias.

### 3) Configurando o Bot

**Localize e edite o Arquivo de Configuração:**

Na pasta onde você extraiu o bot, encontre o arquivo chamado
`config.ini` e abra-o usando um editor de texto de sua escolha, por exemplo: 
(Bloco de Notas no Windows, TextEdit no macOS, etc.).

**1- Configuração do Caminho do Tesseract**

Dentro da seção [tesseract], você precisa especificar o caminho onde
o Tesseract OCR está instalado, o qual você copiou anteriormente durante o
processo de instalação.

Se você não souber onde o Tesseract está instalado, role até os passos de instalação no início do documento 
para encontrar instruções sobre como localizar o caminho.

- **Windows:**

  Se o Tesseract estiver instalado no diretório padrão
  `C:\Program Files\Tesseract-OCR`, nenhuma alteração é necessária.

  Se estiver instalado em outro local, especifique o caminho completo para o executável do Tesseract e formate-o corretamente:

  - adicione uma barra invertida extra (` \ `) em cada segmento do caminho. Por exemplo:

  ```ini
  [tesseract]
  pytesseract_path = C:\\Seu\\Caminho\\Personalizado\\Para\\Tesseract-OCR
  ```

- **Linux ou macOS:**

  Cole o caminho copiado anteriormente. Por exemplo:
  ```ini
  [tesseract]
  pytesseract_path = /usr/local/bin
  ```

<br>

**2- Configurando os Parâmetros dos Itens**

**Armadura:**

- **min_life:**  Define o percentual mínimo de vida que um item de armadura deve ter para ser considerado pelo bot. 
Este valor deve estar entre 1 e 99.
- **min_sockets:** Especifica o número mínimo de engastes que a armadura deve ter para ser considerada. 
Este valor deve estar entre 1 e 4.

  Exemplo:
  ```ini
  [params]
  min_life = 90
  min_sockets = 4
  ```
  *Armadura comprada pelo bot usando esses parâmetros:*

  ![Gameplay Settings](https://github.com/johnovelli/anya-shop-bot/blob/main/imgs/config/armor_example.jpg?raw=true)

**Garra:**
- **min_skill:** Define o número mínimo de habilidades de assassino ou de armadilhas que um item deve ter. 
Este valor deve estar entre 1 e 3.
- **min_has_skill:**  Especifica o número mínimo de habilidades de sentinela de relâmpago que um item deve ter. 
Este valor também deve estar entre 1 e 3.

  Exemplo:
  ```ini
  [params]
  min_skill = 2
  min_has_skill = 2
  ```

  *Garra comprada pelo bot usando esses parâmetros:*

  ![Gameplay Settings](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/claw_example.jpg)

<br>

## Executando o Bot

### 1) Prepare o Jogo:

- Certifique-se de que o jogo esteja aberto e configurado de acordo com as
  instruções fornecidas acima, neste documento.
- Seu personagem deve estar posicionado perto da Anya e do portal,
  como mostrado na imagem abaixo:

  ![posição do personagem](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/character_position.jpg)

### 2) Abra o Bot Runner:

- Navegue até a pasta onde você extraiu os arquivos do bot.
- Localize o arquivo `run.py` dentro desta pasta.
- Dê um clique duplo no arquivo `run.py` para abrir o bot.
- Uma janela como esta será aberta:

  ![Bot Runner](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/bot_runner.jpg)

### 3) Inicie o Bot:

- Após abrir o Bot Runner, siga as instruções fornecidas na janela para iniciar o bot.
- Antes de executar o bot, certifique-se de que a janela do Bot Runner esteja sobreposta à janela do Diablo 2 Resurrected, 
como mostrado na imagem abaixo:

  ![posição da janela](https://raw.githubusercontent.com/johnovelli/anya-shop-bot/main/imgs/config/window_position.jpg)

<br>

## Lançamentos

### Primeira Versão
[Versão 0.1 - Lançamento Inicial](https://github.com/johnovelli/anya-shop-bot/releases/tag/v0.1)

Esta é a primeira versão do bot. Ela inclui funcionalidades básicas e ainda há espaço para melhorias. Mais recursos e aprimoramentos serão adicionados em futuras atualizações.

**Links para Download:**
- [anya-shop-bot-0.1.zip](https://github.com/johnovelli/anya-shop-bot/releases/download/v0.1/anya-shop-bot-0.1.zip)
- [anya-shop-bot-0.1.tar.gz](https://github.com/johnovelli/anya-shop-bot/releases/download/v0.1/anya-shop-bot-0.1.tar)