from netaddr import *
import pprint

# ip_input = input('Insert IP Address :')


# print(ip.version)

# ip_sub = IPNetwork('192.0.2.0/24')
# print(ip_sub.ip)
# print(ip_sub.size)
        

# for ip in IPNetwork('192.168.1.0/24'):
#     print('%s' %ip)

# for ip in IPNetwork('fe80::bbfa:69c9:a50f:2ae5/127'):
#     print('%s' %ip)

# print(IPAddress('255.255.255.0').netmask_bits())
# 1
# ip6 = IPAddress(0, 6)
# print(ip6.version)

# ip_input = 'fe80::bbfa:69c9:a50f:2ae5/24'

# if ((' ' in ip_input) == True):
#     ip_input2 = ip_input.split(' ')
#     submask = IPAddress(str(ip_input2[1])).netmask_bits()
#     ip_input = ip_input2[0] + '/' + str(submask)

# ip_sub = IPNetwork(str(ip_input))
# print(IPAddress(ip_input).version)
# # for ip in ip_sub:
# #     print('%s' %ip)


# x = '192.168.1.2'
# if ((' ' in x) == True):
#     y = x.split(' ')
#     print('you have cidr')
#     z = y[0] +'/'+ y[1]
#     print(z)
# else:
#     print(x)
#     print(IPNetwork(x).size)

# x = '192.168.1.1 255.255.255.0'
# print(IPAddress(x))
# if(('/' in x) == True):
#     y = x.split('/')
#     print(y[0])
#     print(y[1])
#     print(IPAddress(y[0]).version)
# elif((' ' in x) == True):
#     y = x.split(' ')
#     sub = IPAddress(str(y[1])).netmask_bits()
#     print(y[0])
#     print(y[1])
#     print(sub)
#     print('Error')

ip_input = input('Insert IP Address : ')

if ((' ' in ip_input) == True):
    ip_input2 = ip_input.split(' ')
    submask = IPAddress(ip_input2[1]).netmask_bits()
    ip_input = ip_input2[0]
    print(ip_input2[0])
    print(ip_input2[1])
    print(IPAddress(ip_input2[1]).netmask_bits())
    print(IPAddress(ip_input2[0]).version)
