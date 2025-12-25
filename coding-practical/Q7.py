'''
List All IPs That Triggered 404 Errors
'''


log_file = "/Users/tripurakant/Documents/code/My_git/prep-int/coding-practical/access.log"

with open(log_file) as f:
    for line in f:
        # print(line)
        parts = line.split()
        ip = parts[0]
        err_code = parts[8]
        if not err_code:
            continue
        status_field = int(err_code)
        if status_field == 404:
            print(f"{ip}: {err_code}")

        # print(f"{ip}: {err_code}")