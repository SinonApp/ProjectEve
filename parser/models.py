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
    
    def filtering(self, data, currency=None, quantity='USDT'):
        try:
            if currency is None:
                return data
            if quantity is None:
                return data
            output = []
            for item in data:
                # Убираем слеши, тире, подчеркивания, пробелы, 1000, приводим к нижнему регистру
                symbol = item['symbol'].replace('/', '').replace('-', '').replace('_', '').replace('1000', '').replace(' ', '').lower()

                # Если подсчетная валюта в начале названия символа и необходимая валюта в конце
                if symbol.endswith(quantity.lower()) and symbol.startswith(currency.lower()):
                    # Проверяем, не осталось ли ничего лишнего, к примеру TONCOIN_USDT будет COIN после удаления USDT и TON
                    symbol = symbol.replace(quantity.lower(), '').replace(currency.lower(), '')
                    if symbol == '':
                        output.append(item)

            return output
        except Exception as e:
            print(data, self.exchange)
            print(e)

    def format(self):
        output = []
        if self.data is None:
            return output
        try:
            match self.exchange:
                case 'binance':
                    for item in self.data:
                        data = {}
                        data['symbol'] = item['symbol']
                        data['price'] = item['price']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['symbol', 'price']})

                case 'bybit':
                    for item in self.data['result']:
                        data = {}
                        data['symbol'] = item['symbol']
                        data['price'] = item['last_price']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['symbol', 'last_price']})

                case 'coinsbit':
                    for item in self.data['result']:
                        data = {}
                        data['symbol'] = self.data['result'][item]['ticker']['name']
                        data['price'] = self.data['result'][item]['ticker']['last']
                        output.append(data)
    #                        output.append({key: self.data['result'][item]['ticker'][key] for key in ['name', 'last']})

                case 'bitfinex':
                    for item in self.data:
                        data = {}
                        data['symbol'] = item[0]
                        data['price'] = item[7]
                        output.append(data)
    #                        output.append({'symbol': item[0], 'last_price': item[7]})

                case 'mexc':
                    for item in self.data:
                        data = {}
                        data['symbol'] = item['symbol']
                        data['price'] = item['price']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['symbol', 'price']})

                case 'kucoin':
                    for item in self.data['data']['ticker']:
                        data = {}
                        data['symbol'] = item['symbol']
                        data['price'] = item['last']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['symbol', 'last']})

                case 'bitget':
                    for item in self.data['data']:
                        data = {}
                        data['symbol'] = item['symbol']
                        data['price'] = item['close']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['symbol', 'close']})

                case 'lbank':
                    for item in self.data['data']:
                        data = {}
                        data['symbol'] = item['symbol']
                        data['price'] = item['ticker']['latest']
                        output.append(data)

                case 'crypto':
                    for item in self.data['ticker']:
                        data = {}
                        data['symbol'] = item['symbol']
                        data['price'] = item['last']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['symbol', 'last']})
                case 'bkex':
                    for item in self.data['data']:
                        data = {}
                        data['symbol'] = item['symbol']
                        data['price'] = item['price']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['symbol', 'price']})

                case 'bitmart':
                    for item in self.data['data']['tickers']:
                        data = {}
                        data['symbol'] = item['symbol']
                        data['price'] = item['last_price']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['symbol', 'last_price']})

                case 'upbit':
                    for item in self.data:
                        data = {}
                        data['symbol'] = item['market']
                        data['price'] = item['trade_price']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['market', 'trade_price']})

                case 'probit':
                    for item in self.data['data']:
                        data = {}
                        data['symbol'] = item['market_id']
                        data['price'] = item['last']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['market_id', 'last']})

                case 'bittrex':
                    for item in self.data:
                        data = {}
                        data['symbol'] = item['symbol']
                        data['price'] = item['lastTradeRate']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['symbol', 'lastTradeRate']})

                case 'okcoin':
                    for item in self.data['data']:
                        data = {}
                        data['symbol'] = item['instId']
                        data['price'] = item['last']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['instId', 'last']})

                case 'okx':
                    for item in self.data['data']:
                        data = {}
                        data['symbol'] = item['instId']
                        data['price'] = item['last']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['instId', 'last']})

                case 'poloniex':
                    for item in self.data:
                        data = {}
                        data['symbol'] = item['symbol']
                        data['price'] = item['close']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['symbol', 'close']})

                case 'exmo':  # exmo имеет проблему при получении данных со всех бирж
                    for item in self.data:
                        try:
                            data = {}
                            data['symbol'] = item
                            data['price'] = self.data[item]['last_trade']
                            output.append(data)
                        except:
                            print(self.data)

                case 'gateio':
                    for item in self.data:
                        data = {}
                        data['symbol'] = item['currency_pair']
                        data['price'] = item['last']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['currency_pair', 'last']})

                case 'coinw':
                    for item in self.data['data']:
                        data = {}
                        data['symbol'] = item['base-currency'] + item['quote-currency']
                        data['price'] = item['latestDealPrice']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['symbol', 'latestDealPrice']})

                case 'huobi':
                    for item in self.data['data']:
                        data = {}
                        data['symbol'] = item['symbol']
                        data['price'] = item['close']
                        output.append(data)
    #                        output.append({key: item[key] for key in ['symbol', 'close']})

        except Exception as e:
            print(f'Error in get_ticker {self.exchange}')
            print(e)

        return output