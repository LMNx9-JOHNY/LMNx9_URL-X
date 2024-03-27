#!/usr/bin/python3
# Tool - LMNx9_URL-X
# Codded By - DARK LMNx9

#============================>

black="\033[1;30m"
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
blue="\033[1;34m"
pink="\033[1;35m"
sky="\033[1;36m"
white="\033[1;37m"

#============================>

import os,sys,time

try:
    import bs4
except:
    print(f"\n {pink}<\>{green} Installing Bs4...\n")
    os.system("pip install bs4")
    from bs4 import BeautifulSoup
    
try:
    import requests
except:
    print(f"\n {pink}<\> {green}Installing Requests...\n")
    os.system("pip install requests")
    import requests
    
from bs4 import BeautifulSoup
import requests

#============================>

logo=("""\033[1;35m

    ██    ██ ██████  ██            ██   ██ 
    ██    ██ ██   ██ ██             ██ ██  
    ██    ██ ██████  ██      █████   ███   
    ██    ██ ██   ██ ██             ██ ██  
     ██████  ██   ██ ███████       ██   ██
     
\033[1;35m </>\033[1;34m DEVELOPER\033[1;33m - \033[1;32mDARK LMNx9 \033[1;33m| \033[1;34mVERSION \033[1;33m- \033[1;32m1.0.1
""")

#============================>

def clr():
    os.system('clear')

def kolixa():
    print("")
    print(9*f"{sky} </> ")
    print("")
    
def jannat():
    print("")

def ex():
    clr()
    print(logo)
    kolixa()
    print(f" {pink}</> {green}THANKS FOR USING LMNx9 TOOL")
    jannat()
    time.sleep(2.5)
    sys.exit()

def help():
    os.system("xdg-open https://t.me/DARK_LMNx999")
    
#============================>

def LMNx9():
    lmnx9_url = "https://www.shorturl.at/shortener.php"
    lmnx9_headers = {
        "Host": "www.shorturl.at",
        "Content-Length": "30",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "https://www.shorturl.at",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "X-Requested-With": "mark.via",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://www.shorturl.at/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en,en-US;q=0.9",
        "Cookie": "PHPSESSID=fcada36b6ac1185f7338482b59889da5",
    }
    def lmnx9_dark_forces(lmnx9_data):
        dark_lmnx9 = requests.post(lmnx9_url, headers=lmnx9_headers, data=lmnx9_data)
        if dark_lmnx9.status_code == 200:
            dark_soup = BeautifulSoup(dark_lmnx9.text, 'html.parser')
            lmnx9_short_url_element = dark_soup.select_one('#shortenurl')

            if lmnx9_short_url_element:
                lmnx9_short_url = lmnx9_short_url_element['value']
                clr()
                print(logo)
                kolixa()
                print(f" {pink}</>{blue} YOUR LONG URL :{yellow} ", lmnx9_input)
                jannat()
                print(f" {pink}</> {yellow}GET SHORT URL :{green} ", lmnx9_short_url)
                kolixa()
                input(f" {pink}</>{green} PRESS ENTER TO BACK MAIN{pink} ==>")
                LMNx9()
            else:
                kolixa()
                print(f" {pink}</> {red}URL RESPONSE NOT FOUND ! {pink}<wrong>")
                jannat()
                input(f" {pink}</> {green}PRESS ENTER TO BACK MAIN {pink}==>")
                LMNx9()
        else:
            kolixa()
            print(f" {pink}</> {red}Failed to retrieve LMNx9 short URL : {black}", dark_lmnx9.status_code)
            jannat()
            input(f" {pink}</> {green}PRESS ENTER TO BACK MAIN {pink}==>")
            LMNx9()
            
    clr()
    print(logo)
    kolixa()
    print(f"\t{pink}</> {red}FOR EXIT{green} -> {red}INPUT{yellow} = {red}X")
    print(f"\t{pink}</> {red}FOR HELP{green} -> {red}INPUT{yellow} = {red}H")
    kolixa()
    lmnx9_input = input(f" {pink}</> {yellow}ENTER LONG URL {green}: ")
    if lmnx9_input in ["x","X"]:
        ex()
    elif lmnx9_input in ["h","H"]:
        help()
        time.sleep(2)
        LMNx9()
    else:
        lmnx9_data = {
        "u": lmnx9_input,
        }
        lmnx9_dark_forces(lmnx9_data)
    
    lmnx9_dark_forces(lmnx9_data)

#============================>

LMNx9()

