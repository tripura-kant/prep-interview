'''
Q9. Extract Top 10 Referrers
Log:
 "GET /home HTTP/1.1" 200 1024 "https://google.com/search?q=..." "Mozilla/5.0"
 Task: Extract the referrer field and show the top 10 sources.
'''

log_file = "/Users/tripurakant/Documents/code/My_git/prep-int/coding-practical/access.log"
result = 0
count = 0
with open(log_file) as f:
    for line in f:
        parts = line.split('"')
        ref = parts[1]
        print(ref)