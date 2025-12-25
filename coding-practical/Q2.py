# Q2. Filter Requests with 5xx Status Codes
# Task: Extract all lines where the HTTP status code is in the 5xx range.

log_file = "/Users/tripurakant/Documents/code/My_git/prep-int/coding-practical/access.log"

with open(log_file) as f:
    for line in f:
        match = line.split()
        if len(match) < 2:
            continue
        status = match[-2]
        
        if not status.isdigit():
            continue
        status_filed = int(status)
        if status_filed >= 500:
            print(line)
