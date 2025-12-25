'''
Q4. Identify the Most Frequently Requested URL Path
Log Line:
 203.0.113.42 - - [24/May/2025:10:22:15 +0000] "GET /api/user/profile HTTP/1.1" 200 350
 Task: Extract the path (like /api/user/profile) and count the most accessed one.
'''

log_file="/Users/tripurakant/Documents/code/My_git/prep-int/coding-practical/access.log"
url_path_list = {}

with open(log_file) as f:
    for line in f:
        parts = line.split('"')
        if len(parts) < 2:
            continue  # skip malformed lines

        request = parts[1]              # GET /api/user/profile HTTP/1.1
        request_parts = request.split()

        if len(request_parts) < 2:
            continue

        path = request_parts[1]         # /api/user/profile
        url_path_list[path] = url_path_list.get(path, 0) + 1

# find the most frequently requested path
most_requested_path = max(url_path_list, key=url_path_list.get)

print("Most requested path:", most_requested_path)
print("Request count:", url_path_list[most_requested_path])
