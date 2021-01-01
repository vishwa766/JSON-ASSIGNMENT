import os
import json
import time
from sys import getsizeof
from Functions import ttldict


def ifFileExistes(FileName):
    return os.path.exists(FileName)
    
def create(dic,fi):
        
            count=0
            while count<1:
                    k=input("Enter the key: ")
                    if len(k)<32:
                        if k not in dic:
                                v=input("Enter the value:")
                                if (getsizeof(v)/1000)<16:
                                    dic[k]=v
                                    count+=1
                                else:
                                    print("Size of value exceeds 16 KB,cannot insert the key value pair")
                        else:
                                print("key already exists")
                    else:
                        print("Length of key should be at most 32")
        

def delete(dic):
        if len(dic)>0:
                k=input("Enter the key to be deleted: ")
                if k in dic:
                        del dic[k]
                        print(f"The key {k} is deleted")
                else:
                        print("No key value pair exist")
        else:
                print("Json file is empty")

def read(dic):
        if len(dic)>0:
                k=input("Enter the key: ")
                if k in dic:
                        print(f'The value for {k} is {dic[k]}')          
                else:
                        print("No key value pair exist")
        else:
                print("Json file is empty")

def display(dic,fi):
    print("Choose from the given option")
    print("1.Create")
    print("2.Read")
    print("3.Delete")
    print("4.Exit")
    k=input("Enter Your option: ")
    if k=='1':
        create(dic,fi)
        display(dic,fi)
    elif k=='2':
        read(dic)
        display(dic,fi)
    elif k=='3':
        delete(dic)
        display(dic,fi)
    elif k=='4':
        with open(fi,'w') as f:
            json.dump(dic,f,indent=2)       
    else:
        print("Enter a Valid option ")
        display(dic)

def main():
    check=input("Do You want to open an existing JSON file? If yes press Y , else press N \n")
    if check == 'Y' or check=='y':

        FileName=input("Enter the JSON file name\n")
        FileName=FileName+'.json'
        flag=ifFileExistes(FileName)

        if flag==True:
            fi=os.getcwd()+"\\"+FileName
            if os.path.exists(fi):
                size = os.path.getsize(fi)/1073741824
                if size<1:
                    try:
                        os.rename(fi, fi)
                        with open(FileName) as f:
                            dic=json.load(f)
                        display(dic,FileName)
                    except OSError as e:
                        print("File is currently being used by another process")
                else:
                    print("The file you are trying to open is more than 1 GB,cannot open")
            
        else:
            txt=input("Do you want to have time to live foe the JSON file? If yes press Y,else press N: ")
            if txt == 'Y' or txt == 'y':
                t=int(input("Enter the time to live in seconds: "))
                dic=ttldict.TTLDict(ttl=t)
            else:
                dic={}
            display(dic,FileName)
    else:
        txt=input("Do you want to have time to live for the JSON file? If yes press Y,else press N: ")
        if txt == 'Y' or txt == 'y':
            t=int(input("Enter the time to live in seconds: "))
            dic=ttldict.TTLDict(ttl=t)
        else:
            dic={}
        FileName=input("Enter the file name to save\n")
        FileName=FileName+'.json'
        display(dic,FileName)

        
