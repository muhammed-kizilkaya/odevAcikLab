#!/usr/bin/python3
import os

print("PYTHON YÖNTEMİ: echo $USER komutu ile: "+ os.popen('echo $USER ').read() )

print("\\n   //////")

print("whoami "+ os.popen('whoami ').read()   )

 
 

