import os

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