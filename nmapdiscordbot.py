###nmap discord bot

import asyncio
import nmap
import re
from colorama import Fore, Back, Style
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext import commands
nmScan = nmap.PortScanner()
ports = []
addy = []
ips = []
response= "hello"
command = []
scaner =""
combo={}
load_dotenv()
TOKEN = ('INPUT YOUR TOKEN')
GUILD = ('INPUT YOUR GUILD')
scans={1:"-sS",2:"-sT",3:"-sU",4:"-sA",5:"-sW",6:"-sM",7:"-sO",8:"-sF",9:"-sN",10:"-sX"}
time_options = {
        1: ("-T0", "-T5"),
        2: ("--min-rtt-timeout", "--max-rtt-timeout", "--init-rtt-timeout"),
        3: "--host-timeout",
        4: ("--min-rate", "--max-rate"),
        5: "--max-retries",
        6: ("--min-hostgroup", "--max-hostgroup"),
        7: ("--min-parallelism", "--max-parallelism"),
        8: ("--scan-delay", "--max-scan-delay"),
    }

##########################


# def verbosity():
#     try:
#         v=int(input("would you like to include VERBOSITY? (Type 1 for yes, type 2 for increased VERBOSITY, 0 for no):"))
#         if v == 1:
#             v = '-v'
#             return v
#         if v == 2:
#             v = '-vv'
#             return v
#         else:
#             return
#     except:
#         print("not valid paramater, skipping....")

def is_valid_ip(ip):
    # Regular expression for validating an IPv4 address
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    
    # Validate the IP address
    if re.match(pattern, ip):
        # Split the IP address into octets
        octets = ip.split('.')
        
        # Check each octet is in the range 0-255
        for octet in octets:
            if not 0 <= int(octet) <= 255:
                return False
        return True
    else:
        return False
    
# ##################
# # # # # while response != "":
# # # # #     print("for all ports input ALL")
# # # # #     response = input("please input the port(s): ")
# # # # #     if response.upper() == 'ALL':
# # # # #         ports.append("-p-")
# # # # #         response = ""
# # # # #     if response.isdigit():
# # # # #         ports.append(response)

# # # # #         continue
# # # # #     if response == "":
# # # # #         exit
# # # # #     else: response = print("Not a number, try again idiot")
# # # # # ####################
# # # # # ip = "pre"
# # # # # while ip != "":
# # # # #     ip = input("please input the ip address(s):")
# # # # #     if is_valid_ip(ip) == True:
# # # # #         ips.append(ip)
# # # # #         continue
# # # # #     if ip == "":
# # # # #         exit
# # # # #     else: ip = print("Not a number, try again idiot")
# def scan():
#     while True:
#         print("Select which scan you would like to use:")
#         print(Fore.GREEN + "1. TCP SYN (Stealth) Scan (-sS)")
#         print("   - The most popular scan type, fast and stealthy, works against all functional TCP stacks.")
        
#         print(Fore.GREEN +"2. TCP Connect Scan (-sT)")
#         print("   - Uses the system call of the same name, usually used by unprivileged Unix users and against IPv6 targets.")
        
#         print(Fore.GREEN +"3. UDP Scan (-sU)")
#         print("   - Scans UDP ports which can be a source of security vulnerabilities.")
        
        
#         print(Fore.GREEN +"4. TCP ACK Scan (-sA)")
#         print("   - Used to map out firewall rulesets, distinguishing between stateful and non-stateful rules.")
        
#         print(Fore.GREEN +"5. TCP Window Scan (-sW)")
#         print("   - Similar to ACK scan, but can detect open versus closed ports on certain machines.")
        
#         print(Fore.GREEN +"6. TCP Maimon Scan (-sM)")
#         print("   - A firewall-evading scan, similar to a FIN scan but includes the ACK flag.")
    
        
#         print(Fore.GREEN +"7. IP Protocol Scan (-sO)")
#         print("   - Determines which IP protocols are supported by the target, not technically a port scan but similar in approach.")
        
         
#         print("8. TCP FIN Scan (-sF)")
#         print("   - Sends TCP packets with the FIN flag set to the target machine. Useful for evading packet filters and firewalls, as some systems don't respond to unsolicited FIN packets. However, this scan type may be less effective against certain operating systems, notably Microsoft Windows, which tend to ignore these packets.")

#         print("9. TCP NULL Scan (-sN)")
#         print("   - Sends a TCP packet with no flags set (a 'null' packet). Like the FIN scan, this is used for stealth and firewall evasion. Systems conforming to the TCP standard should ignore such packets, but some systems might respond, revealing information about open ports. Again, certain operating systems like Windows might not provide useful responses.")

#         print("10. TCP Xmas Scan (-sX)")
#         print( "   - Sends a TCP packet with the FIN, PSH, and URG flags set, lighting the packet up 'like a Christmas tree.' It's used for stealth and to elicit responses from ports in a way similar to the FIN and NULL scans. However, its effectiveness depends on the specific behavior of the target's TCP stack, and it may be easily detected by modern intrusion detection systems."+ Fore.RESET )

#         scan_selection = input("Enter your choice (1-10): ")
#         if scan_selection.isdigit():
           
#             scan_selection = int(scan_selection)
#             scan_selection = scans[scan_selection]
#             scaner = scan_selection
#             return scaner
            
            
#         else:
#             print("Please enter a valid number (1-10).")
        
# def times_options():
    
#         print("Select which Nmap option you would like to learn more about:")
#         print("1. Timing Templates (-T0 through -T5)")
#         print("   - These templates adjust Nmap speed, ranging from very slow (-T0) to extremely aggressive (-T5). They affect many scan variables, and more granular options take precedence if combined with these templates.")

#         print("2. RTT Timeouts (--min-rtt-timeout, --max-rtt-timeout, --initial-rtt-timeout)")
#         print("   - These options define the minimum, maximum, and initial round-trip time (RTT) that Nmap will wait for a response to a port scan probe.")

#         print("3. Host Timeout (--host-timeout)")
#         print("   - Determines the maximum amount of time Nmap will spend scanning a single host before giving up.")

#         print("4. Rate Limits (--min-rate, --max-rate)")
#         print("   - Set the lower and upper limits for the number of probe packets Nmap sends per second.")

#         print("5. Maximum Retries (--max-retries)")
#         print("   - Specifies the maximum number of times Nmap will retransmit a probe to a single port when no response is received.")

#         print("6. Hostgroup Sizes (--min-hostgroup, --max-hostgroup)")
#         print("   - Configures the minimum and maximum number of hosts that Nmap will scan in parallel.")

#         print("7. Parallelism (--min-parallelism, --max-parallelism)")
#         print("   - Sets limits on the minimum or maximum number of concurrent scan probes across all hosts.")

#         print("8. Scan Delays (--scan-delay, --max-scan-delay)")
#         print("   - Directs Nmap to wait a specified minimum time between sending probes to an individual host, with an option to set a maximum delay to accommodate packet loss detection.")

#         print("Enter 'back' to return to the main menu.")
#         t=0
#         while t != 1:
#             option_selection = (input("Enter your choice (1-8) if you would like to use a timing template, type template:"))
#             if option_selection == "template":
#                 print(" paranoid|sneaky|polite|normal|aggressive|insane (Set a timing template)")
#                 print("paranoid (0), sneaky (1), polite (2), normal (3), aggressive (4), and insane (5). The first two are for IDS evasion. Polite mode slows down the scan to use less bandwidth and target machine resources. Normal mode is the default and so -T3 does nothing. Aggressive mode speeds scans up by making the assumption that you are on a reasonably fast and reliable network. Finally insane mode assumes that you are on an extraordinarily fast network or are willing to sacrifice some accuracy for speed.")
#                 template_selection=input("please enter a valid number 0-5:")
#                 if template_selection.isdigit():
#                     template = ("-T"+template_selection)
#                     return template
#             else:
#                 print("not valid")
         
        
                
            
#             #if option_selection.isdigit():
#                 #### ADD NUMBER INPUT AFTER VALUE IS RECIEVED#####
#             try:
#                 option_selection=int(option_selection)
#                 if option_selection in time_options:
#                     opt_selection = time_options[option_selection]
#                     t=0
#                     while t != 1:
#                         if isinstance(opt_selection, tuple):
#                             min_max_choice = input("Do you want 'min', 'max', or 'both' options? (min/max/both): ").lower()
#                             #### ADD NUMBER INPUT AFTER VALUE IS RECIEVED#####
#                             if min_max_choice == 'min':
#                                 min_choice=input("input value: ")
#                                 solo=opt_selection[0]
#                                 combo=(solo+" "+min_choice)
#                                 return combo
#                             elif min_max_choice == 'max':
#                                 max_choice=input("input value: ")
#                                 solo=opt_selection[0]
#                                 combo=(solo+" "+max_choice)
#                                 return combo
#                             elif min_max_choice == 'both':
#                                 min=input("type min:")
#                                 max=input("type max:")
                            
#                                 if option_selection == 2:
#                                     init = input("input inital:")
#                                 if min.isdigit() and max.isdigit() or min.isdigit() and max.isdigit() and init.isdigit():
#                                     minVal= opt_selection[0]
#                                     maxVal=opt_selection[1]
#                                     try:
#                                         initVal=opt_selection[2]
#                                         combo=(minVal +" "+min, maxVal +" "+max, initVal+" "+init)
#                                     except:
#                                         combo=(minVal +" "+min, maxVal +" "+max)

#                                     return combo
#                                 else: print("try again")
#                                 combo=(minVal + " "+min, maxVal +" "+max)
#                                 return combo
#                             else: print("try again")
#                 else: print("try again")
#             except:
#                 t=0
#                 print("doesn't work")
        
#         combo=opt_selection
#         return combo
# Call the scan_options function to display the menu
# verb=verbosity()
# os=os_scan()
# svc_scan=service_scan()
# time=times_options()
# #print(ips)
# scaner = scan()
# # # command=["nmap ", svc_scan,verb,os,ports,scaner,time,ips]
# # # print(command)

async def service_scan(ctx, check):
    await ctx.send(f"would you like to include SERVICE AND VERSION SCAN? (Type 1 for yes, 0 for no):")
    
    while True:
        msg=await bot.wait_for("message",check=check)
        svc=msg.content.strip()
        try:
            if svc == "1":
                
                return "-sV"
            elif svc == "0":
                return ""
            else: await ctx.send("Not a valid input, try again.")
        except Exception as e:
            
            return f"Error:{e}"   
async def os_scan(ctx, check):
    await ctx.send(f"would you like to include OPERATING SYSTEM ENUMERATION? (Type 1 for yes, 0 for no):")
    
    while True:
        msg=await bot.wait_for("message",check=check)
        os=msg.content.strip()
        try:
            
            if os == "1":
                
                return "-o"
            elif os == "0":
                return ""
            else: await ctx.send("Not a valid input, try again.")
        except Exception as e:
            
            return f"Error:{e}"
async def verbosity(ctx, check):
    await ctx.send(f"would you like to include VERBOSITY? (Type 1 for yes, type 2 for increased VERBOSITY, 0 for no):")
    while True:
        msg=await bot.wait_for("message",check=check)
        v = msg.content.strip()
        try:
            
            if v == "1":
                
                return "-v"
            elif v == "2":
                
                return "-vv"
            elif v == "0":
                return ""
            else: await ctx.send("Not a valid input, try again.")
                
        except Exception as e:
            
            return f"Error:{e}"
##################
async def ports_selection(ctx, check):
    ports = []
    await ctx.send("For all ports input ALL, input ports one by one, type 'done' when finished:")
    
    while True:
        msg = await bot.wait_for("message", check=check)
        response = msg.content.strip()

        if response.upper() == 'ALL':
            return "-p-"
        elif response.isdigit():
            ports.append(response)
            await ctx.send(f"Port {response} added. Add more ports or type 'done'.")
        elif response.upper() == 'DONE':
            return ','.join(ports)
        else:
            await ctx.send("Not a valid input, try again.")

async def ips_selection(ctx, check):
    ips=[]
    await ctx.send("please input the ip address(s):")
    while True:
        msg = await bot.wait_for("message", check=check)
        ip = msg.content.strip()
        if is_valid_ip(ip) == True:
            ips.append(ip)
            await ctx.send(f"IP {ip} added. Add more ports or type 'done'.")
            
        elif ip.upper() == 'DONE':
            return ','.join(ips)
        else: await ctx.send("Not a valid input, try again.")
async def scan(ctx, check):
    while True:
        
        scan_options="""Select which scan you would like to use:
        1. TCP SYN (Stealth) Scan (-sS) - Most popular scan type, fast and stealthy, works against all functional TCP stacks.")
        2. TCP Connect Scan (-sT)" - Uses the system call of the same name, usually used by unprivileged Unix users and against IPv6 targets.")
        3. UDP Scan (-sU)") - Scans UDP ports which can be a source of security vulnerabilities.")
        4. TCP ACK Scan (-sA)") - Used to map out firewall rulesets, distinguishing between stateful and non-stateful rules.")
        5. TCP Window Scan (-sW)") - Similar to ACK scan, but can detect open versus closed ports on certain machines.")
        6. TCP Maimon Scan (-sM)") - firewall-evading scan, similar to a FIN scan but includes the ACK flag.")
        7. IP Protocol Scan (-sO) - Determines which IP protocols are supported by the target, not a port scan but similar in approach.")
        8. TCP FIN Scan (-sF)" - TCP packets with the FIN flag set to the target machine. Useful for evading packet filters and firewalls, as some systems don't respond to unsolicited FIN packets. However, this scan type may be less effective against certain operating systems, notably Microsoft Windows, which tend to ignore these packets
        9. TCP NULL Scan (-sN) - TCP packet with no flags set (a 'null' packet). Like the FIN scan, this is used for stealth and firewall evasion. Systems conforming to the TCP standard should ignore such packets, but some systems might respond, revealing information about open ports. Again
        10. TCP Xmas Scan (-sX) - TCP packet with the FIN, PSH, and URG flags set, lighting the packet up 'like a Christmas tree.' It's used for stealth and to elicit responses from ports in a way similar to the FIN and NULL scans. However, its effectiveness depends on the specific behavior of the target's TCP stack"""
        await ctx.send(scan_options)
        try:
            msg = await bot.wait_for('message', check=check, timeout=60.0)
            if msg.content.isdigit():
                scan_selection = int(msg.content)
                if scan_selection in scans:
                    return scans[scan_selection]
                else:
                    await ctx.send("Please enter a valid number (1-10).")
            else:
                await ctx.send("Invalid input. Please enter a number.")
        except asyncio.TimeoutError:
            await ctx.send("You did not respond in time.")
        #scan = msg.content.strip()
        #scan_selection = input("Enter your choice (1-10): ")
        #if scan_selection.isdigit():
           
         #   scan_selection = int(scan_selection)
          #  scan_selection = scans[scan_selection]
           # scaner = scan_selection
            #return scaner
            
            
        #else:
            #?print("Please enter a valid number (1-10).")


intents = discord.Intents.default()
intents.members = True  # For accessing member information
intents.message_content = True  # For message content access in messages

# Initialize the bot with the command prefix and the specified intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='nmap', help='Responds with quote')
#always needs ctx in arg for command
async def nmap_scan(ctx):
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    
    
    
    
    #await ctx.send(f"would you like to include OPERATING SYSTEM enumeration? (Type 1 for yes 0 for no):")
    #msg = await bot.wait_for("message",check=check)
    #os_param=os_scan(msg)
    #await ctx.send(os_param)

    svc_param=await service_scan(ctx, check)
    os_param= await os_scan(ctx, check)
    verb_param= await verbosity(ctx, check)
    port_param = await ports_selection(ctx, check)
    ips_param = await ips_selection(ctx,check)
    scan_result = await scan(ctx,check)
    command=[svc_param, os_param, verb_param, port_param,scan_result,ips_param]
    nmap_command = 'nmap ' + ' '.join(filter(None, command)).strip()
    await ctx.send(nmap_command)
    
bot.run(TOKEN) 


