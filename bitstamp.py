import websocket
import json

def ao_abrir(ws):
    print('Conexão estabelecida com sucesso!')

    json_subscribe = """    
{
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}
"""

    ws.send(json_subscribe)

def ao_fechar(ws):
    print('Conexão encerrada!')

def erro(ws, erro):
    print('---------------------------------')
    print('Algo deu errado!')
    print('---------------------------------')


def ao_receber_mensagem(ws, mensagem):
    mensagem = json.loads(mensagem)
    price = mensagem["data"]["price"]
    print(price)

    if price > 500000:
        vender()
    elif price < 300000:
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