#!/usr/bin/python
import sys
import requests
import textwrap

ussd_api = 'https://api.wow-q.com/api/ussd/v3.gateway.php'
post_params = {'sessionid': 'wbe48930', 'dialstring': '*120*8800*5100#', 'request': '*120*8800*5100#'}

def my_special_text_wrap(txt):
    parts = txt.split('\n')
    for i in range (len(parts)):
        print textwrap.fill(parts[i], 70)

def make_that_request ():
    print "POST data: ", post_params
    ussd = requests.request("POST", ussd_api, data=post_params)
    response = ussd.json()

    while True:
        if response['session'] == 1:
            print "-"*70
            my_special_text_wrap(response['text'])
            print "-"*70
            request = raw_input("\nEnter your response: ")
            post_params['request'] = request
            print "\nPOST data: ", post_params
            ussd = requests.request("POST", ussd_api, data=post_params)
            response = ussd.json()
        else:
            print "*"*70
            print "Session was terminated"
            print "-"*70
            my_special_text_wrap(response['text'])
            print "*"*70
            print "Exit (see above)"
            break

if __name__ == '__main__':
    try:
        post_params['msisdn'] = sys.argv[1]
        make_that_request()
    except IndexError:
        print "*"*80
        print "Missing 'msisdn'"
        print "Usage: {} <mobile number in international format>".format(sys.argv[0])
        print "Example: {} 358504824392".format(sys.argv[0])
        print "*"*80
