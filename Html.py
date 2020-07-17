# -*- coding: utf-8 -*-
# author: luo xu
# create time: 2020/6/22 19:31
import requests
import time


class GetHTML(object):
    def __init__(self, session=False, timeout=(60, 90)):
        self.session_judge = session
        self.timeout = timeout
        self.times = 5
        if session:
            self.session = requests.session()

    def get(self, url, params=None, headers=None, **kwargs):
        cou_i = 1
        while True:
            try:
                if self.session_judge:
                    res = self.session.get(url, params=params, timeout=self.timeout, headers=headers, **kwargs)
                else:
                    res = requests.get(url=url, params=params, timeout=self.timeout, headers=headers, **kwargs)
                break
            except Exception:
                if cou_i < self.times:
                    time.sleep(1)
                else:
                    res = None
                    break
        return res

    def post(self, url, params=None, data=None, json=None, headers=None, **kwargs):
        cou_i = 1
        while True:
            try:
                if self.session_judge:
                    res = self.session.post(url, params=params, data=data, json=json, timeout=self.timeout,
                                            headers=headers, **kwargs)
                else:
                    res = requests.post(url, params=params, data=data, json=json, timeout=self.timeout, headers=headers,
                                        **kwargs)
                break
            except Exception:
                if cou_i < self.times:
                    time.sleep(1)
                else:
                    res = None
                    break
        return res
