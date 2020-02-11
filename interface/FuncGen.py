import requests

global r

class FuncGen(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, _method, _url, _data, _headers):
        print "hello, i am  %s." % self.name
        self.common_requests(_method, _url, _data, _headers)

    def common_requests(self, _method, _url, _data, _headers):
        global r
        if _method == 'get':
            r = requests.get(url=_url, params=_data, headers=_headers)
        elif _method == 'post':
            r = requests.post(url=_url, json=_data, headers=_headers)
        elif _method == 'patch':
            r = requests.patch(url=_url, json=_data, headers=_headers)
        else:
            return False
        return True

    def get_r(self):
        global r
        return r


if __name__ == "__main__":
    lista = ["funca", "funcb", "funcc"]

    dictf = {}
    for a in lista:
        dictf.update({a: FuncGen(a)})

    for a in lista:
        dictf[a](a)