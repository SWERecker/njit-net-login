import time
import subprocess
import requests
import os

# 校园网登录脚本，默认选择外网
# 通过fiddler抓取登录时的POST包并用requests库发送POST请求，间隔5秒请求一次
# Usage: python login.py (控制台运行)
# 使用pythonw可以后台持续运行

ip = '****填入内网ip****'
username = '****学工号****'
password = '****密码****'
portal = '10.0.1.1:801'
login_server = '10.0.1.1'
check_connection_server = '114.114.114.114'
check_interval = 5

def login():
    _url = f"http://{portal}/eportal/?c=ACSetting&a=Login&protocol=http:&hostname={login_server}&iTermType=1&wlanuserip={ip}&wlanacip=null&wlanacname=njit_off&mac=00-00-00-00-00-00&ip={ip}&enAdvert=0&queryACIP=0&loginMethod=1 "
    _header = {
        'Host': portal,
        'Accept': 'text/html,application/xhtml+xml,image/jxr,*/*',
        'Referer': f'http://{login_server}/a70.htm?wlanuserip={ip}&wlanacip=null&wlanacname=njit_off&vlanid=0&ip={ip}&ssid=null&areaID=null&mac=00-00-00-00-00-00',
        'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip,deflate',
        'Connection': 'Keep-Alive',
        'Pragma': 'no-cache',
        'Cookie': f'program=123; vlan=0; ip={ip}; PHPSESSID=jlf72uoh4381pbvouvmgh1u8p0; ssid=null; areaID=null; ISP_select=@outnjit; md5_login2=%2C0%2C{username}@outnjit%7C{password}'
    }

    _data = {
        'DDDDD': f',0,{username}@outnjit',
        'upass': password,
        'R1': '0',
        'R2': '0',
        'R3': '0',
        'R6': '0',
        'para': '00',
        '0MKKey': '123456',
        'buttonClicked': '',
        'redirect_url': '',
        'err_flag': '',
        'username': '',
        'password': '',
        'user': '',
        'cmd': '',
        'Login': ''
    }
    res = requests.post(_url, data=_data, headers=_header)
    return res.status_code


if __name__ == '__main__':
    while True:
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        exit_code = subprocess.getstatusoutput(f'ping {check_connection_server} -n 1')
        print(f'【{time_now}】Ping result: {exit_code[0]}')
        if exit_code[0] != 0:
            print(f'【{time_now}】Failed to connect to server.')
            res = login()
            print(f'【{time_now}】Try to login, result: ', res)
            with open('log.txt', 'a', encoding='utf-8')as f:
                f.write(f'【{time_now}】Reconnect. result={res}\n')
        time.sleep(check_interval)
        

       
