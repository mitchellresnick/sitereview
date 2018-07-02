from __future__ import print_function

from argparse import ArgumentParser
from bs4 import BeautifulSoup
import json
import requests
import sys
import time

class SiteReview(object):
    def __init__(self):
        self.baseurl = "http://sitereview.bluecoat.com/resource/lookup"
        self.headers = {"User-Agent": "Mozilla/5.0", "Content-Type": "application/json"}

    def sitereview(self, url):
        payload = {"url": url, "captcha":""}
        
        try:
            self.req = requests.post(
                self.baseurl,
                headers=self.headers,
                data=json.dumps(payload),
                verify=False,
            )
        except requests.ConnectionError:
            sys.exit("[-] ConnectionError: " \
                     "A connection error occurred")

        return json.loads(self.req.content.decode("UTF-8"))

    def check_response(self, response):
        if self.req.status_code != 200:
            sys.exit("[-] HTTP {} Returned".format(req.status_code))
        else:
            self.category = response["categorization"][0]["name"]
            self.date = response["translatedRateDates"][0]["text"][0:35]
            self.url = response["url"]
            try:
                self.category2 = response["categorization"][1]["name"]
            except IndexError:
                pass
            



def main():

    f = open("url.txt")
    o = open("output.txt", 'a+')

    for url in f:
        time.sleep(5)
        s = SiteReview()
        response = s.sitereview(url)
        try:
            s.check_response(response)
        except NameError:
            print("URL FORMAT ERROR")
            o.write("URL FORMAT ERROR" + "\n")
            continue
        try:
            print(s.url + "," + s.category + "," + s.category2)
            o.write(s.url + "," + s.category + "," + s.category2 + "\n")
        except AttributeError:
            print(s.url + "," + s.category)
            o.write(s.url + "," + s.category + "\n")


    f.close()
    o.close()
    
if __name__ == "__main__":
    main()
