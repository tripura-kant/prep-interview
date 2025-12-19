# Q2. Filter Requests with 5xx Status Codes
# Task: Extract all lines where the HTTP status code is in the 5xx range.

log_file="access.log"


with open(log_file) as f:
    for line in f:
        status = int(line.split()[-2])
        if status >= 500:
            print(line)


            