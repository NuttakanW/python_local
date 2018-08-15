from netaddr import *
import pprint
import sys

def start():
    ip_input = input('Insert IP Address : ')
    print(ip_input)
    if ((' ' in ip_input) == True):
        ip_input2 = ip_input.split(' ')
        submask = str(IPAddress(ip_input2[1]).netmask_bits())
        ip_input = ip_input2[0]


    elif (('/' in ip_input) == True):
        ip_input2 = ip_input.split('/')
        submask = ip_input2[1]
        ip_input = ip_input2[0]
    
    try:
        ipv = IPAddress(ip_input).version

        if(ipv == 4):
            ipv4(ipv, ip_input, submask)
        elif(ipv == 6):
            ipv6(ipv, ip_input, submask)
        else:
            print('Please Insert IP Address again!!')
            start()
    except:
        print('Insert IP Address again')
        start()


def ask_user(quest):
    check = str(input("%s (Y/N): " %quest)).lower().strip()
    try:
        if check[0] == 'y':
            return True
        elif check[0] == 'n':
            return False
        else:
            print('Invalid Input')
            return ask_user(quest)
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return ask_user(quest)

def write_file(operate_name, ipsub, ip_input, submask):
    try:
        with open('/home/nuttakan/Documents/Python_local/ipaddress_prac/genip/'+operate_name+'.txt', 'a') as f:
            for ip in IPNetwork(ipsub):
                f.write(operate_name)
                f.write('\t')
                f.write(str(ip)+'\n')
            f.close() 
            return True
    except Exception as error:
        print(error)
        start()
    

def ipv4 (ipv, ip_input, submask):
    ip = IPAddress(ip_input)
    ipsub = IPNetwork(ip_input+'/'+submask)
    print('Your IP Address version is IPv%s' %ipv)
    print('This IP Address has %s IP' %ipsub.size)
    if (ask_user('Do you want to generate IP Address')):
        operate_name = input('Enter Operation Name : ')
        
        if(write_file(operate_name, ipsub, ip_input, submask)):
            print('Write Finished')
            start()
    
    else:
        print(ip_input+'_'+submask+'Just This Right?')
        start()

def ipv6 (ipv, ip_input, submask):
    ip = IPAddress(ip_input)
    ipsub = IPNetwork(ip_input+'/'+submask)
    print('Your IP Address version is IPv%s' %ipv)
    print('This IP Address has %s IP' %ipsub.size)
    if (ask_user('Do you want to generate IP Address')):
        operate_name = input('Enter Operation Name : ')
        
        if(write_file(operate_name, ipsub, ip_input, submask)):
            print('Write Finished')
            start()
    
    else:
        print(ip_input+'_'+submask+'Just This Right?')
        start()


start()
