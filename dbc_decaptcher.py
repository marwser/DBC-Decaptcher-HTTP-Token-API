#!/usr/bin/env python
#
# Decaptcher Python API Module For DeathByCaptcha API
#
import requests


class Decaptcher:

    def __init__(self, username, password, product_id=""):
        self.__action_url = "http://api.dbcapi.me/decaptcher"
        self.__username = username
        self.__password = password
        self.__product_id = product_id

    def get_balance(self):
        data = {"function": "balance",
                "username": self.__username,
                "password": self.__password}
        request = requests.post(self.__action_url, data)
        return float(request.content)

    def solve_image(self, image_path):
        data = {"function": "picture2",
                "username": self.__username,
                "password": self.__password,
                "pict_to": "0",
                "pict_type": "0",
                "pict": open(image_path, "rb").read()}
        request = requests.post(self.__action_url, data)
        answer = request.content.split("|")[-1]
        return answer

    def solve_token(self, pageurl, googlekey, proxy="", proxytype=""):
        data = {"function": "token",
                "username": self.__username,
                "password": self.__password,
                "proxy": proxy,
                "proxytype": proxytype,
                "googlekey": googlekey,
                "pageurl": pageurl,
                "pict_to": "0",
                "pict_type": "4"}
        request = requests.post(self.__action_url, data)
        answer = str(request.content).split("|")[-1]
        return answer


if __name__ == "__main__":
    cl = Decaptcher("username-here", "password-here")
    result = cl.solve_token(
        "http://skyrock.com", "6LcTyP4SAAAAADBjv0TABENKwCOGOFe5H15-hd_4")
    print(result)
