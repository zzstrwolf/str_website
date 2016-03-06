import os

filedir = "../static/tx/"
print os.path.exists(filedir)
print os.getcwd()
print type(os.getcwd())
if not os.path.exists(filedir):
   print os.makedirs(filedir)
