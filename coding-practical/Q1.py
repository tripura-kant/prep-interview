'''
Q1. Find Top 10 IPs by Frequency
Log Type: Nginx / Apache access log
 192.168.1.10 - - [24/May/2025:10:21:05 +0000] "GET /index.html HTTP/1.1" 200 1024
 Task: Extract the top 10 IP addresses by number of requests.
'''

log_file="/Users/tripurakant/Documents/code/My_git/prep-int/coding-practical/access.log"
ip_count = {}

with open(log_file) as file:
    for line in file:
        ip = line.split()[0]
        ip_count[ip] = ip_count.get(ip, 0) + 1

sorted_ips = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)

for ip, count in sorted_ips[:10]:
    print(f"{ip}: {count}")