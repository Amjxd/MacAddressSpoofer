import subprocess # Used to run Terminal commands from python
import re # Regular Expressions (Pythex)

def prompt():
    global interface
    global new_mac
    interface = input("Interface: ")
    new_mac = input("New Mac Address: ")

def change_mac(new_mac, interface):
    print(f"[+] Changing MAC Address for {interface} to {new_mac}")
    subprocess.call(["ifconfig",interface,"down"]) # Everytime there is a space we type the next element of our command
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

# How to read the result of the system command:
    # subprocess.check_output(["write","your","program")
def check(new_mac,interface):
    result = subprocess.check_output(["ifconfig",interface])
# In order to filter what we want from the result, we need to use RegEx (Regular Expresions)
# Pythex.org
    result = result.decode('utf-8') # Decodes Bytes to String
    mac_address_sr = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",result) #re.search(r"expression",what you want to search)
    if mac_address_sr:
        print(f"[+] MAC Address has been changed to {mac_address_sr.group(0)}") # group(0) - because if there was more than one match it would be group(1),group(2)... We are only interested in the first result
    else:
        print("[-] Could not read MAC Address")
 

if __name__ == "__main__":
    prompt()
    change_mac(new_mac,interface)
    check(new_mac,interface)

