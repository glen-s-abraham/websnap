import sys,getopt
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

opts =Options()
opts.headless = True
print("Initializing Driver...")
browser = webdriver.Firefox(options=opts)
argumentList = sys.argv[1:] 
optionlist=options = "hi:"
longoptionlist = ["Help", "infile"]

try:
  arguments, values = getopt.getopt(argumentList, optionlist, longoptionlist)
  for currentArgument, currentValue in arguments: 
  
        if currentArgument in ("-h", "--Help"): 
              print("python -i <file>")
              
        elif currentArgument in ("-i", "--infile"): 
              print("opening ",currentValue,"....")
              try:
                infile=open(currentValue,'r')
                for host in infile.readlines():
                  print("Connecting to ",host.strip(),"....")
                  try:
                    browser.get(host)
                  except Exception:
                    continue
                  if not os.path.exists('outputs'):
                    os.makedirs('outputs')
                  bad_char=[':','/','.']
                  for i in bad_char:
                    host=host.replace(i,'')   
                  ofile="outputs//"+host.strip()+".png"
                  print("Saving image to ",ofile,"....")
                  browser.save_screenshot(ofile)
              except Exception:
                  print('File not found')
except getopt.error as err: 
    print (str(err)) 