import json
import requests

class UnifyParser:

    def __init__(self, url, exchange, params={}, headers={}):
        # params example: {'json_head_param': 'items', 'items_params': ['symbol', 'last_price']}
        self.url = url
        self.exchange = exchange
        self.params = params
        self.headers = headers

    def parse_upbit(self, count_try=0):
        count_try = count_try + 1
        if count_try > 3:
            self.data = None
            return None
        markets = requests.get(url="https://api.upbit.com/v1/market/all", params=self.params, headers=self.headers)
        if markets.status_code == 200:
            markets = json.loads(markets.text)
            markets = [item['market'] for item in markets]
            self.params['markets'] = ','.join(markets)
            req = requests.get(url=self.url, params=self.params, headers=self.headers)
            if req.status_code == 200:
                self.data = json.loads(req.text)
                return self.data
            else:
                return self.parse_upbit(count_try=count_try)
        else:
            return self.parse_upbit(count_try=count_try)

    def parse(self, count_try=0):
        match self.exchange:
            case 'upbit':
                return self.parse_upbit(count_try=count_try)
            case _:
                count_try = count_try + 1
                if count_try > 3:
                    self.data = None
                    return None
                req = requests.get(url=self.url, params=self.params, headers=self.headers)
                if req.status_code == 200:
                    self.data = json.loads(req.text)
                    return self.data
                else:
                    return self.parse(count_try=count_try)
    
    def format(self):
        output = []
        if self.data is None:
            return output
        match self.exchange:
            case 'binance':
                for item in self.data:
                    output.append({key: item[key] for key in ['symbol', 'price']})
            case 'bybit':
                for item in self.data['result']:
                    output.append({key: item[key] for key in ['symbol', 'last_price']})
            case 'coinsbit':
                for item in self.data['result']:
                    output.append({key: self.data['result'][item]['ticker'][key] for key in ['name', 'last']})
            case 'bitfinex':
                for item in self.data:
                    output.append({'symbol': item[0], 'last_price': item[7]})
            case 'mexc':
                for item in self.data:
                    output.append({key: item[key] for key in ['symbol', 'price']})
            case 'kucoin':
                for item in self.data['data']['ticker']:
                    output.append({key: item[key] for key in ['symbol', 'last']})
            case 'bitget':
                for item in self.data['data']:
                    output.append({key: item[key] for key in ['symbol', 'close']})
            case 'lbank':
                for item in self.data['data']:
                    data = {}
                    data['symbol'] = item['symbol']
                    data['last_price'] = item['ticker']['latest']
                    output.append(data)
            case 'crypto':
                for item in self.data['ticker']:
                    output.append({key: item[key] for key in ['symbol', 'last']})
            case 'bkex':
                for item in self.data['data']:
                    output.append({key: item[key] for key in ['symbol', 'price']})
            case 'bitmart':
                for item in self.data['data']['tickers']:
                    output.append({key: item[key] for key in ['symbol', 'last_price']})
            case 'upbit':
                for item in self.data:
                    output.append({key: item[key] for key in ['market', 'trade_price']})
            case 'probit':
                for item in self.data['data']:
                    output.append({key: item[key] for key in ['market_id', 'last']})
            case 'bittrex':
                for item in self.data:
                    output.append({key: item[key] for key in ['symbol', 'lastTradeRate']})
            case 'okcoin':
                for item in self.data['data']:
                    output.append({key: item[key] for key in ['instId', 'last']})
            case 'okx':
                for item in self.data['data']:
                    output.append({key: item[key] for key in ['instId', 'last']})
            case 'poloniex':
                for item in self.data:
                    output.append({key: item[key] for key in ['symbol', 'close']})
            case 'exmo':
                for item in self.data:
                    data = {}
                    data['symbol'] = item
                    data['last_price'] = self.data[item]['last_trade']
                    output.append(data)
            case 'gateio':
                for item in self.data:
                    output.append({key: item[key] for key in ['currency_pair', 'last']})
            case 'coinw':
                for item in self.data['data']:
                    output.append({key: item[key] for key in ['symbol', 'latestDealPrice']})
            case 'huobi':
                for item in self.data['data']:
                    output.append({key: item[key] for key in ['symbol', 'close']})

        return output