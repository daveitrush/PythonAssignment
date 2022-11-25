import os


def hostblacklist(hostname):

    hosts = open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'r')

    content = hosts.read()

    if hostname in content:

        response = input("The host already exists in the hosts file. Would you like to direct requests to 0.0.0.0? y/n")
        while response != "y" and response != "n":
            response = input("Please select y or n")
        if response == "n":
            return print("Hosts file was not updated, host already exists in the hosts file")

    hosts.close()
    hosts = open("C:\\Windows\\System32\\drivers\\etc\\hosts", mode='a', encoding='cp1252')
    hosts.write("0.0.0.0 " + hostname + "\n")
    hosts.close()

    return print("Hosts file was updated and pointed " + hostname + " to 0.0.0.0")




