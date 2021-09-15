#!/usr/local/bin/python3
#########################################################################
# PURPOSE: to submit htrack data from cli                               #
# As this is a custom script, use it with your own risk.                #
# Any issue or difficulty, feel free to contact me.                     #
# @2021 - bkrisna - b.krisnamurti@gmail.com                             #
#########################################################################

import requests
import json
import urllib
import base64
import time as time_
import datetime

from datetime import datetime, timedelta
from datetime import date
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from urllib.parse import urlencode, quote_plus


#############################################################################
# function logger for show log                                              #
# parameter                                                                 #
# - operations (str)                                                        #
# - operation status (true/false).                                          #
# - data (str).                                                             #
# return items: -                                                           #
#############################################################################
def logger(ops, res, data):
    date = datetime.now();
    datestr = date.strftime("%Y/%m/%d %H:%M:%S")
    state = "success" if res else "failed"
    print ('[{0:s}][{1:<7s}][{2:^9s}][{3:s}]'.format(datestr, ops, state, data))
    return True

#####################################
# request call
# return:
# - result dict
#####################################  
def send_request( baseurl, act, urlParams=None ):
    s=requests.Session()
    s.verify=False #disables SSL certificate verification
    #baseUri='https://' + usr + ':' + paswd + '@' + hst + '/akm/?'
      
    if urlParams is not None:
        qs=urlencode(urlParams)

    reqUrl=baseurl + '/' + act + '?' + qs
    print (reqUrl)
    try:    
        r=s.get(reqUrl)
        #itms = xmltodict.parse(r.content).get('result')
        return r.json()
    except Exception as e:
        return str(e)

#############################################################################
# main program                                                              #
#############################################################################

s=requests.Session()
s.verify=False #disables SSL certificate verification
repSrv = 'healthtracking.telkomsigma.co.id'
baseUri ='https://'+ repSrv+'/api'
wdir = './bin'

#https://healthtracking.telkomsigma.co.id/api/employeehistory?nik=L201508180&date=2021-09-15

s=requests.Session()
s.verify=False #disables SSL certificate verification
repSrv = 'healthtracking.telkomsigma.co.id'
baseUri ='https://'+ repSrv+'/api'

urlParams = {
    'nik' : 'L201508180',
    'date' : '2021-09-15'
}
#q = urlencode(qs)

#encodedUrl = baseUri + '/employeehistory?' + q

res = send_request(baseUri, 'employeehistory', urlParams )

print (res)

#try:
#    r= s.get(encodedUrl)
#    print (r.json())
#except Exception as e:
#    logger ('get_employe_history', False, str(e))


logger ('misc', True, 'Get employee data')