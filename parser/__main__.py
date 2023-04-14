from .models import UnifyParser
import argparse

parser = argparse.ArgumentParser(description="Parser for Binance and Bybit")
parser.add_argument("-e", "--exchange", help="Exchange name", type=str, default="binance")
parser.add_argument("-l", "--list", help="List of exchanges", action="store_true")
args = parser.parse_args()

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
    'gateio': UnifyParser(url="https://api.gateio.ws/api/v4/spot/tickers", exchange="gateio", headers={'accept': 'application/json', 'content-type': 'application/json'}),

}

if __name__ == "__main__":
    if args.list:
        for key in dict_exchanges:
            print(key)
        exit()
    if args.exchange in dict_exchanges:
        exchange = dict_exchanges[args.exchange]
        exchange.parse()
        print(exchange.format())
    else:
        print("Exchange not found")