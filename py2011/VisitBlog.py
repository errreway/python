#! /usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created on 2011-04-06
@description: use multithreading to visist some of my blog pages
@author: http://smilejay.com/
'''

import sys
import threading
import urllib.request

urls = ['kvm_theory_practice/',
        'about/',
        'i_will_laugh_at_the_world/'
        ]

visitTimesPerPage = 10


def usage():
    print('Usage:', sys.argv[0], 'host')


def main(argv):
    host = argv[1]
    if host == '':
        usage()
        sys.exit(2)


class VisitPageThread(threading.Thread):

    def __init__(self, threadName, host, url):
        threading.Thread.__init__(self, name=threadName)
        self.host = host
        self.url = url

    def run(self):
        url = self.host + self.url
        req = urllib.request.Request(url)
        req.set_proxy('companyname.com:911', 'http')
        # you may set you proxy here.
   

if __name__ == '__main__':
    sys.argv.append('http://smilejay.com/')
    main(sys.argv)
