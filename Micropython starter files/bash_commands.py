import os
import esp
import network

def ls():
    print(os.listdir())

def mkdir(name):
    os.mkdir(name)

def rm(name):
    os.remove(name)

def cat(name):
    file = open(name)
    print(file.read())
    file.close()

def cd(path):
    os.chdir(path)

def pwd():
    print(os.getcwd())

def rmdir(path):
    os.rmdir(path)

def rename_file(old_path, new_path):
    os.rename(old_path, new_path)

def uid():
    print(esp.flash_id)

def erase_sector(sector_id):
    esp.flash_erase(sector_id)

def wget(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break