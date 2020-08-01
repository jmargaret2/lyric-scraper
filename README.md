# Lyric Scraper

A program that uses a Genius.com API to scrape lyrics from an artist, and write the lyrics to a .txt file.

<!-- TABLE OF CONTENTS -->

## Table of Contents

-   [About the Project](#about-the-project)
-   [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Installation](#installation)
-   [Usage](#usage)
-   [License](#license)
-   [Contact](#contact)

<!-- ABOUT THE PROJECT -->

## About The Project

Lyric-scraper is a small Python program built to scrape lyrics from Genius.com using Genius's API, and is distributed under the MIT license. Using an artist and number of songs input by the user, the lyrics of the songs are written into a .txt file.

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

-   Python 3
-   A Genius.com [API key](https://docs.genius.com/#/getting-started-h1): input your API key where it says "GENIUS_API_TOKEN"

### Installation

1.  Get a free API Key at <https://docs.genius.com/#/getting-started-h1>
   1. Select "New API Client on the sidebar"
   2. Fill in the information for a new API Client
   3. Generate an Access token
2.  Clone the repo

```sh
git clone https://github.com/jmargaret2/lyric-scraper.git
```

3.  Enter your API in `main.py`

```python
GENIUS_API_TOKEN = 'ENTER YOUR API'
```
## Usage

Once the program is run, you will be able to type in an artist's name and a number of songs. For example, typing the name ```Alec Benjamin``` and ```3``` songs will result in something like this:

![](https://jmargaret2.github.io/assets/images/scraperPart1.png)

We can see that the program has successfully written 3 songs (that contain a total of 190 lines) into a txt file. Looking at the txt file that was created, we can we it is titled after the artist we entered (in this case, it is alecbenjamin.txt) and contains three distinct songs. [You can view the txt file here.](https://jmargaret2.github.io/assets/txt/alecbenjamin.txt)

The three songs that Genius scraped from its database are three of Alec Benjamin's most popular songs: *Let Me Down Slowly*, *Outrunning Karma*, and *I Built a Friend*.

![](https://jmargaret2.github.io/assets/images/alecBenjaminGenius.png)

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Margaret Jagger \
margaretjagger2@gmail.com

Project Link: <https://github.com/jmargaret2/lyric-scraper>
Project webpage: <https://jmargaret2.github.io/portfolio/lyricScraper/>
