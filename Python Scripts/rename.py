from variables_module import *
import os

newName = input("Enter new name: ")
sourceDirectory = input("Enter directory: ")

os.chdir(sourceDirectory)

def rename(name):

    count = 1

    for file in os.listdir():
        ext = os.path.splitext(file)[1]

        newFile = '{}-{}{}'.format(name, count, ext)
        print(newFile)

        os.rename(file, newFile)

        count += 1


rename(newName)