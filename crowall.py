# coding:utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#    __author__ = '郭 璞'
#    __date__ = '2016/10/24'
#    __Desc__ = 翻墙助手， 默认会先备份一下当前的hosts文件，防止出现意外，另外可以跨平台使用

import platform
import os
import urllib2

def downloadHosts(url):
    file = open('./hosts.txt', 'wb')
    data = urllib2.urlopen(url).readlines()
    file.writelines(data)
    file.close()



def crosswall(systemtype='Window'):
    try:
        if systemtype == 'Windows':
            os.system('copy %SystemRoot%\System32\drivers\etc\hosts  %SystemRoot%\System32\drivers\etc\hosts_bak')
            os.system('copy hosts.txt %SystemRoot%\System32\drivers\etc\hosts')
            os.system('ipconfig /flushdns')
            os.system('pause')
            print 'It\'s done on Windows! And Try your browser!'
        elif systemtype == "Linux":
            os.system('cp /etc/hosts.txt /etc/hosts_bak')
            os.system('mv ./hosts /etc/hosts')
            os.system('pause')
            os.system('sudo /etc/init.d/networking restart ')
            print 'It\'s done on Linux! And Try your browser!'
        elif systemtype == "Darwin":
            os.system('sudo cp /etc/hosts /etc/host_bak')
            os.system('sudo mv ./hosts.txt /etc/hosts')
            os.system('sudo ifconfig en0 down && sudo ifconfig en0 up')
            print 'It\'s done on Mac! And Try your browser!'
    except Exception as e:
        print e



if __name__ == '__main__':

    url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
    downloadHosts(url=url)
    print 'Hosts update success!'
    crosswall(platform.system())
    print 'Hosts replaced success! Try to cross the wall!'
