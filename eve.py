from parser.models import UnifyParser
import argparse

# Создание экземпляра объекта парсера аргументов командной строки
parser = argparse.ArgumentParser(description="Parser for Binance and Bybit")

# Добавление аргументов краткий вызов, полный вызов, справки, тип данных, значение по умолчанию
parser.add_argument("-e", "--exchange", help="Exchange name", type=str, default="binance")

# Добавление аргументов краткий вызов, полный вызов, справка, действие
parser.add_argument("-l", "--list", help="List of exchanges", action="store_true")

# Получение объекта с аргументами
# args.exchange - значение аргумента exchange (тип данных str)
# args.list - значение аргумента list (из-за действия store_true, значение True или False)
args = parser.parse_args()

# binance, bybit, coinsbit, bitfinex, mexc, kucoin, bitget, lbank, crypto, bkex, bitmart
dict_exchanges = {
    "binance": UnifyParser(url="https://api.binance.com/api/v3/ticker/price", exchange="binance"),
    "bybit": UnifyParser(url="https://api.bybit.com/v2/public/tickers", exchange="bybit"),
    'coinsbit': UnifyParser(url="https://api.coinsbit.io/api/v1/public/tickers", exchange="coinsbit"),
    'bitfinex': UnifyParser(url="https://api-pub.bitfinex.com/v2/tickers?symbols=ALL", exchange="bitfinex"),
    'okx': UnifyParser(url="https://www.okx.com/api/v5/market/tickers?instType=SPOT", exchange="okx"),
    'mexc': UnifyParser(url="https://api.mexc.com/api/v3/ticker/price?symbols=all", exchange="mexc"),
    'kucoin': UnifyParser(url="https://api.kucoin.com/api/v1/market/allTickers", exchange="kucoin"),
    'bitget': UnifyParser(url="https://api.bitget.com/api/spot/v1/market/tickers", exchange="bitget"),
    'lbank': UnifyParser(url="https://api.lbkex.com/v2/ticker/24hr.do?symbol=all", exchange="lbank"),
    #'crypto': UnifyParser(url="https://api.crypto.com/v1/ticker/price", exchange="crypto", headers={'accept': 'application/json', 'content-type': 'application/json'}),
    'bkex': UnifyParser(url="https://api.bkex.com/v2/q/ticker/price", exchange="bkex"),
    'bitmart': UnifyParser(url="https://api-cloud.bitmart.com/spot/v2/ticker", exchange="bitmart"),
    'upbit': UnifyParser(url="https://api.upbit.com/v1/ticker", exchange="upbit", headers={'accept': 'application/json', 'content-type': 'application/json'}),
    'probit': UnifyParser(url="https://api.probit.com/api/exchange/v1/ticker", exchange="probit"),
    #'bitrue': UnifyParser(url="https://www.bitrue.com/api/v1/ticker/allPrices", exchange="bitrue"),
    'bittrex': UnifyParser(url="https://api.bittrex.com/v3/markets/tickers", exchange="bittrex"),
    #'bigone': UnifyParser(url="https://big.one/api/v2/tickers", exchange="bigone"),
    'okcoin': UnifyParser(url="https://www.okcoin.com/api/v5/market/tickers?instType=SPOT", exchange="okcoin"),
    'poloniex': UnifyParser(url="https://api.poloniex.com/markets/ticker24h", exchange="poloniex"),
    'exmo': UnifyParser(url="https://api.exmo.com/v1.1/ticker", exchange="exmo"),

}

if __name__ == "__main__":
    exchange = dict_exchanges['exmo']
    exchange.parse()
    print(exchange.format())