# Q3. Count Number of Unique IPs Making Requests
# Task: Count how many unique IP addresses accessed the server.


log_file="access.log"
unique_ips = set()


with open("access.log") as f:
    for line in f:
        ip = line.split()[0]
        unique_ips.add(ip)

print(len(unique_ips))