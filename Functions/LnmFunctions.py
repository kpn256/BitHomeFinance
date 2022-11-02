
from curses.ascii import isdigit
import json
from lnmarkets import rest
# from lnmarkets import websockets


class User(rest.LNMarketsRest):

    def __init__(self, key, secret, passphrase):
        super().app_configuration

        self.key = key
        self.secret = secret
        self.passphrase = passphrase

        self.options = {
                'key': f'{self.key}',
                'secret': f'{self.secret}',
                'passphrase': f'{self.passphrase}'
                }

        self.status = False

        self.lnm = rest.LNMarketsRest(**self.options)
        self.lnm.futures_get_ticker()

    def login(self):

        self.status = True

    def logout(self):
        if self.status:
            self.status = False
        else:
            "go to login"

    def show_status(self):
        if self.status:
            return "user online"
        else:
            return "user offline"


class Trading(User):

    def __init__(self, key, secret, passphrase):
        super().__init__(key, secret, passphrase)

        self.margin = 500
        self.leverage = 50
        self.entryPrice = ""

    def long(self, type, margin, leverage, entry_price):

        if type == "m":
            peticion = self.lnm.futures_new_position({
                'type': type,
                'side': 'b',
                'margin': margin,
                'leverage': leverage,
            })
            self.response(peticion)

        elif type == 'l':

            peticion = self.lnm.futures_new_position({
                'type': type,
                'side': 'b',
                'margin': margin,
                'leverage': leverage,
                'price': entry_price,
            })
            self.response(peticion)

    def long_tp_sl(self, type, margin, leverage, sl, tp):
        peticion = self.lnm.futures_new_position({
            'type': type,
            'side': 'b',
            'margin': margin,
            'leverage': leverage,
            'stoploss': int(sl),
            'takeprofit': int(tp),
        })
        self.response(peticion)

    def long_sl(self, type, margin, leverage, sl):

        peticion = self.lnm.futures_new_position({
            'type': type,
            'side': 'b',
            'margin': margin,
            'leverage': leverage,
            'stoploss': int(sl),
        })
        self.response(peticion)

    def long_tp(self, type, margin, leverage, tp):

        peticion = self.lnm.futures_new_position({
            'type': type,
            'side': 'b',
            'margin': margin,
            'leverage': leverage,
            'takeprofit': int(tp),
        })
        self.response(peticion)

    def Short(self, type, margin, leverage, entry_price):
        if type == 'm':
            peticion = self.lnm.futures_new_position({
                    'type': type,
                    'side': 's',
                    'margin': margin,
                    'leverage': leverage,
                    })
            self.response(peticion)

        elif type == 'l':
            entry_price = int(input("set the limit price: "))
            peticion = self.lnm.futures_new_position({
                    'type': type,
                    'side': 's',
                    'margin': margin,
                    'leverage': leverage,
                    'price': entry_price,
                    })
            self.response(peticion)

    def Short_tp_sl(self, type, margin, leverage, sl, tp):

        if sl == isdigit and tp == isdigit:
            peticion = self.lnm.futures_new_position({
                'type': type,
                'side': 's',
                'margin': margin,
                'leverage': leverage,
                'stoploss': int(sl),
                'takeprofit': int(tp),
            })
            self.response(peticion)

        elif (sl == isdigit) and (not tp == isdigit):
            self.peticion = self.lnm.futures_new_position({
                'type': type,
                'side': 's',
                'margin': margin,
                'leverage': leverage,
                'stoploss': int(sl),
            })
            self.response(peticion)

        elif (tp == isdigit) and (not sl == isdigit):
            peticion = self.nm.futures_new_position({
                'type': type,
                'side': 's',
                'margin': margin,
                'leverage': leverage,
                'takeprofit': int(tp),
            })
            self.response(peticion)

    def close_run_p(self):
        pid = input("paste your position id: ")
        close = self.lnm.futures_cancel_position({
            'pid': f'{pid}'
            })
        return close

    def close_limit_P(self):
        cancelP = self.lnm.futures_cancel_all_positions()()
        print(cancelP)

    def close_all(self):
        closeP = self.lnm.futures_close_all_positions()
        return closeP

    def show_open_p(self):

        open_p = self.lnm.futures_get_positions({
                'type': 'open'
                })
        info_open = json.loads(open_p)
        result = []
        counter = 0
        for i in info_open:
            position = []
            counter += 1
            position.append(f"posicion {counter}")
            position.append(f"price: {i['price']}")
            position.append(f"margin: {i['margin']}")
            position.append(f"liquidation: {i['liquidation']}")
            result.append(position)
            del position

        string = str(result)
        characters = "[]',"
        for x in range(len(characters)):
            string = string.replace(characters[x], "")
        return string

    def show_running_p(self):
        running_p = self.lnm.futures_get_positions({
                'type': 'running'
                })
        info_running = json.loads(running_p)
        result = []
        counter = 0
        for i in info_running:
            position = []
            counter += 1
            position.append(f"\nposicion {counter}")
            position.append(f"price: {i['price']}")
            position.append(f"margin: {i['margin']}")
            position.append(f"liquidation: {i['liquidation']}")
            result.append(position)
            del position

        string = str(result)
        characters = "[]'"
        for x in range(len(characters)):
            string = string.replace(characters[x], "")

        return string

    def response(self, peticion):

        info = json.loads(peticion)
        position_info = info["position"]
        pid = position_info["pid"]
        liquidation = position_info["liquidation"]
        price = position_info["price"]
        leverage = position_info["leverage"]
        take_p = position_info['takeprofit']
        stop_l = position_info['stoploss']
        p_info = print(
                f"position ID: {pid}\n liquidation: {liquidation}\n"
                f"entry price: {price}\n stoploss: {stop_l}\n takeprofit: {take_p}")
        return p_info, pid, liquidation, price, leverage, stop_l, take_p

    def price_btc(self):

        index_price = self.lnm.futures_index_history({
            'limit': 2
        })
        bid_price = self.lnm.futures_bid_offer_history({
            'limit': 2
        })
        price_requests = json.loads(index_price)
        bidOffer = json.loads(bid_price)
        price_index1 = price_requests[1]
        bid_offer1 = bidOffer[1]
        index = price_index1["index"]
        bid = bid_offer1["bid"]
        offer = bid_offer1["offer"]

        return f"index:{str(index)} bid:{str(bid)} offer:{str(offer)}"


'''
user1 = Trading(
    key="tJlOA0pSR8PRTZksov3iqGhRbqaYktS4F5tbYK+dDQ8=",
    secret="I6d2pLEZln+yGHPXZzlGvN5XFCxsnDRQnllikA4JNTADPNct/3zMr7nLFJ593YUzCuKAsqfKZCXWGAkJrHdQ9w==",
    passphrase="9d0hb89h1e4e6")

user1.login()
# print(user1.key)
# print(user1.show_open_p())
# print(user1.showop())
# print(user1.long("m",500,50,""))
# print(user1.longtPsL("m",500,30,20000,23000))
# print(user1.priceBtc())
# print(user1.price_btc())'''
