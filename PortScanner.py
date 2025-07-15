import socket
import uuid
import threading
from ipwhois import IPWhois
from geopy.geocoders import Nominatim

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    sock.close()

def scan_ports(target, start_port, end_port):
    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

def get_mac_address():
    mac_address = uuid.getnode()
    mac_address = ':'.join(("%012X" % mac_address)[i:i+2] for i in range(0, 12, 2))
    return mac_address

def get_ip_addresses(target):
    try:
        ip_addresses = socket.gethostbyname_ex(target)
        return ip_addresses[2]
    except socket.gaierror:
        return []

def get_hosting_info(ip_address):
    try:
        obj = IPWhois(ip_address)
        results = obj.lookup_whois()
        hosting_info = results['asn']
        
        # Get geolocation information
        geolocator = Nominatim(user_agent="port_scanner")
        location = geolocator.reverse(f"{results['nets'][0]['city']}, {results['nets'][0]['country']}")
        geolocation_info = f"Location: {location.address}, Coordinates: {location.latitude}, {location.longitude}"
        
        return f"{hosting_info}\n{geolocation_info}"
    except Exception as e:
        return str(e)

# User input
target = input("Enter the website or domain to scan: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))

# Scan ports
scan_ports(target, start_port, end_port)

# Retrieve MAC address
mac_address = get_mac_address()
print(f"MAC Address: {mac_address}")

# Retrieve IP addresses
ip_addresses = get_ip_addresses(target)
print(f"IP Addresses: {', '.join(ip_addresses)}")

# Retrieve hosting information
for ip_address in ip_addresses:
    hosting_info = get_hosting_info(ip_address)
    print(f"Hosting Information for {ip_address}: {hosting_info}")

# Ask the user if they want to scan again
while True:
    choice = input("Do you want to scan again? (y/n): ")
    if choice.lower() == 'y':
        target = input("Enter the website or domain to scan: ")
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
        scan_ports(target, start_port, end_port)
    else:
        print("Exiting the scanner.")
        break