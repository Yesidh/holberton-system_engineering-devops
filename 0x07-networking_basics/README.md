<p>
<img width="260" height="170" src="https://davidjohncoleman.com/wp-djc/wp-content/uploads/2017/06/HBTN-Borderless-CMYK-Logo-Vertical-Color-Black@1200ppi-300x236.png" align="right" >
</p>





# :colombia: DevOps -Networking basics #0                                       
- OSI Model
  - What it is
  - How many layers it has
  - How it is organized
- What is a LAN
  - Typical usage
  - Typical geographical size
-What is a WAN
  - Typical usage
  - Typical geographical size
- What is the Internet
  - What is an IP address
  - What are the 2 types of IP address
  - What is localhost
  - What is a subnet
  - Why IPv6 was created
- TCP/UDP
  - What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
  - What is the main difference between TCP and UDP
  - What is a port
  - Memorize SSH, HTTP and HTTPS port numbers
  - What tool/protocol is often used to check if a device is connected to a network
## Examples
Bash script that:
- Accepts a string as an argument
- Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
- Ping the IP 5 times
the input:
```
./5-is_the_host_on_the_network 8.8.8.8
```
the output
```
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=12.9 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=63 time=13.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=63 time=7.83 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=63 time=11.3 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=63 time=7.57 ms
```
for more information see the example 5-is_the_host_on_the_network
## Prerequisites
8 lecture hours about OSI model
## Installing
for have the code in your local machine you only need download the code files and put it into a directory.
## Built With
All the code was write under ubuntu 14.04                                 
## Contributing
-- Yesid Gutierrez - Holberton Student                                          
## Versioning
for my learning in Holberton School
## Authors
---Yesid Gutierrez  944@holbertonshcool.com                                    
                                                                               
## Files

|             File               |             Description                  |
|--------------------------------| ---------------------------------------- |
|**0-OSI_model**| What is the OSI model?,How is the OSI model organized?|
|**1-types_of_network**| What type of network are Holberton iMacs connected to?, What type of network could connect an office in one building to another office in a building a few streets away?, What network do you use when you browse www.holbertonschool.com from your smartphone (not connected to the Wifi)?|
|**2-MAC_and_IP_address**| What is a MAC address?, What is an IP address?|
|**3-UDP_and_TCP**| TCP and UDP statements|
|**4-TCP_and_UDP_ports**| bash script for print listening sockets and PID|
|**5-is_the_host_on_the_network**| Bash script Accepts a string as an argument Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed Ping the IP 5 times|