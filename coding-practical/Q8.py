'''
Q8. Calculate Average Response Size
Field: Last field in the log line (e.g., 350 in bytes)
 Task: Calculate the average size of all responses.

'''

log_file = "/Users/tripurakant/Documents/code/My_git/prep-int/coding-practical/access.log"
result = 0
count = 0
with open(log_file) as f:
    for line in f:
        # print(line)
        parts = line.split()
        res_size = parts[9]
        if not res_size:
            continue
        result += int(res_size)
        count += 1
        avg_size = result / count
    print(avg_size)