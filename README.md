# project_eve

## Description
A parser for cryptocurrency exchange APIs to get all tickers is a software tool designed to extract and process ticker data from the APIs of various cryptocurrency exchanges. Tickers refer to the latest market prices and trading information for different cryptocurrencies.

## Installation
### Requirements
- Python 3.10 or higher
- requests

### Installation
```bash
pip install project_eve <- Not worked yet
```

## Usage
### Arguments
```bash
usage: eve.py [-h] [-e EXCHANGE] [-l]

Parser for Binance and Bybit

options:
  -h, --help            show this help message and exit
  -e EXCHANGE, --exchange EXCHANGE
                        Exchange name
  -l, --list            List of exchanges
```

### Examples
```bash
python3 -m project_eve -h # Help
python3 -m project_eve -e binance # Get tickers from binance
python3 -m project_eve -l # List all exchanges
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Authors
- [**@ran_mao**](https://t.me/ran_mao)
- [**@JonNash495**](https://t.me/JonNash495)

## Acknowledgements
- [**@JonNash495**](https://t.me/JonNash495) - For the idea and the help with the code
- [**@ran_mao**](https://t.me/ran_mao) - For the idea and the help with the code
