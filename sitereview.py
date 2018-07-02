from __future__ import print_function

from argparse import ArgumentParser
from bs4 import BeautifulSoup
import json
import requests
import sys
import time

urls = []
output = []

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
                     "A connection error occurred.")

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
            

def prepareExit(outputFile):
    j = open("url.txt", 'w')
    

    # print out the output list backwards so that it matches the order in which the URLs were given
    for x in range(len(output)-1,-1,-1):
        outputFile.write(output[x])

    # write the url.txt file back, less the URLs that have already been checked
    for line in urls:
        j.write(line)


    j.close()

def main():
    o = open("output.txt", 'a+')
    f = open("url.txt")

    for line in f:
        urls.append(line)

    f.close()
    
    failCount = 0

    # we have to traverse the list backwards since we are deleting elements are we go through, this requires an output list that we can reverse and print later
    for x in range(len(urls)-1,-1,-1):
        # wait 5 seconds to prevent the server from giving a CAPTCHA
        time.sleep(5)
        s = SiteReview()
        response = s.sitereview(urls[x])
        # try to analyze the URL, and if it doesn't work, it's either becuase the URL is not formatted properly (enter it into the tool to see what it says), or the server has given a CAPTCHA
        try:
            s.check_response(response)
        except NameError:
            if failCount > 3:
                print ("You may want to browse to sitereview.bluecoat.com and complete the CAPTCHA and restart the program. It seems like the server is blocking all requests from this machine.")
            if failCount > 10:
                prepareExit(o)
                sys.exit("Now exiting the program due to too many failures. Please browse to the website and complete the CAPTCHA")
            print(urls[x].rstrip() + ",URL FORMAT ERROR")
            o.write("\n" + urls[x].rstrip() + ",URL FORMAT ERROR")
            failCount += 1
            continue
        # try to print it with both categories, and if not just print one as that is all that it will have
        try:
            print(s.url + "," + s.category + "," + s.category2)
            o.append(s.url + "," + s.category + "," + s.category2 + "\n")
            failCount = 0
        except AttributeError:
            print(s.url + "," + s.category)
            output.append(s.url + "," + s.category + "\n")
            failCount = 0
        # URL has successfully been analyzed, remove it from the url.txt file as it no longer needs to be analyzed
        del urls[x]

    prepareExit(o)
    o.close()
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Abort recieved, please wait for cleanup.")
        prepareExit()
    finally:
        print("Program successfully terminated")
