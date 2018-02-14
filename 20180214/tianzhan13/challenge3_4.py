# coding: utf-8

import re
from datetime import datetime

def open_parser(filename):
    with open(filename) as logfile:
        pattern = (r''
                   '(\d+.\d+.\d+.\d+)\s-\s-\s'   # IP
                   '\[(.+)\]\s'                  # time  
                   '"GET\s(.+)\s\w+/.+"\s'       # url
                   '(\d+)\s'                     # code
                   '(\d+)\s'                     # length
                   '"(.+)"\s'                    # request header
                   '"(.+)"')                     # client info
        parsers = re.findall(pattern, logfile.read())
    return parsers

def main():
    logs = open_parser('nginx.log')
    ip_dict = {}
    url_dict = {}
    for i in logs:
        if '11/Jan/2017' in i[1]:        
            ip = ip_dict.get(i[0])
            if ip is None:
                ip_dict[i[0]] = 1
            else:
                ip_dict[i[0]] +=1
        if '404' in i[3]:    
            url = url_dict.get(i[2])
            if url is None:
                url_dict[i[2]] = 1
            else:
                url_dict[i[2]] += 1
    max_ip = max(zip(ip_dict.values(), ip_dict.keys()))
    max_url = max(zip(url_dict.values(), url_dict.keys()))
    new_max_ip = {}
    new_max_url = {}
    new_max_ip[max_ip[1]] = max_ip[0]
    new_max_url[max_url[1]] = max_url[0]
    return new_max_ip, new_max_url

if __name__ == '__main__':
    ip_dict, url_dict = main()
    print(ip_dict, url_dict)

