<div id="top"></div>

<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
 
  </a>

  <h3 align="center">Python Binance Ticker Data Project</h3>

  <p align="center">
    Ingesting and analyzing Binance ticker data 
    
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project demonstrates usage of the Binance API and data ingestion using python, MySQL, as well as data analysis using pandas.

### Part 1: Ingesting Binance data 
Two different script demonstrate ingesting Binance 1 minute ticker data for the BTCUSDT ticker.
#### Historic 
Binance has a website tha contains historic market data, so for our purposes we can use the 1 minute kline data. For example, we can find monthly files here:
https://data.binance.vision/?prefix=data/spot/monthly/klines/BTCUSDT/1m/

The data folder contains 3 monthly files that were used for the analysis (part 2).
#### Real Time

For real time data, we can use the python Binance client package: https://python-binance.readthedocs.io/en/latest/

In particular, the Websocket feature allows real time reading of data.

### Part 2: Analyzing ticker data 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
This code was tested with the following software on Ubuntu 20.04.1: 
* Python 3.8.10
* MySQL 8.0.27

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/bioniclebeastmaster/python-btc
   ```
2. Create and activate a virtual environment

2. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```
3. Create a database and user in MySQL and enter the credentials into `config.ini` under mysql section. E.g.
   ```ini
    [mysql]
    host = localhost
    user = btc_user
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>


