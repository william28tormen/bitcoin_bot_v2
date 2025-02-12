import json
import websocket
import bitstamp.client
import secretpass

def cliente():
    return bitstamp.client.Trading(username=secretpass.USERNAME, key=secretpass.KEY, secret=secretpass.SECRET)

def ao_abrir(ws):
    print('Bitcoin BOT - n0body v1.1.2')
    print('----------------------------')
    print('-----> Conexão estabelecida!')
    print('----------------------------')

    json_subscribe = """    
{
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}
"""
    ws.send(json_subscribe)

def comprar():
    trading_client = cliente()
    trading_client.buy_market_order(quantidade)

def vender():
    trading_client = cliente()
    trading_client.sell_market_order(quantidade)

def ao_fechar(ws):
    print('----------------------------')
    print('Conexão encerrada!')

def erro(ws, erro):
        print('----------------------------')
        #print('Algo deu errado!')
        #print(erro)

def ao_receber_mensagem(ws, mensagem):
    mensagem = json.loads(mensagem)
    price = mensagem["data"]["price"]
    print('BTC cotanto em: ${} USD.'.format(price))

    if price > 86829:
        vender()
    elif price < 85829:
        comprar()
    else:
        print('Aguardar!')

if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net/",
                                on_open=ao_abrir,
                                on_message=ao_receber_mensagem,
                                on_error=erro,
                                on_close=ao_fechar
                                )
    ws.run_forever()