# coding:utf-8
import requests as re,os,platform

def downloadHosts(url):
    file = open('.\hosts.txt', 'wb')
    data = re.get(url)
    file.writelines(data)
    file.close()

def crosswall(systemtype='Window'):
    try:
        if systemtype == 'Windows':
            os.system('copy %SystemRoot%\System32\drivers\etc\hosts %SystemRoot%\System32\drivers\etc\hosts_bak')
            os.system('copy hosts.txt %SystemRoot%\System32\drivers\etc\hosts')
            os.system('ipconfig /flushdns')
            os.system('pause')
			print('It\'s done on Window! And Try your browser!')
        elif systemtype == "Linux":
            os.system('cp /etc/hosts.txt /etc/hosts_bak')
            os.system('mv ./hosts /etc/hosts')
            os.system('pause')
            os.system('sudo /etc/init.d/networking restart ')
			print('It\'s done on Linux! And Try your browser!')
        elif systemtype == "Darwin":
            os.system('sudo cp /etc/hosts /etc/host_bak')
            os.system('sudo mv ./hosts.txt /etc/hosts')
            os.system('sudo ifconfig en0 down && sudo ifconfig en0 up')
			print('It\'s done on Mac! And Try your browser!')
    except Exception as e:
        print(e)

url = 'https://raw.githubusercontent.com/googlehosts/hosts/master/hosts-files/hosts'
downloadHosts(url=url)
crosswall(platform.system())
print('Hosts replaced success! Try to cross the wall!')
