# Q6. Extract and Count User Agents
# Extended Log:
#  203.0.113.42 - - [24/May/2025:10:22:15 +0000] "GET /api/user/profile HTTP/1.1" 200 350 "-" "Mozilla/5.0"
#  Task: Count the top 5 most common user agents.


count_agents = {}

with open("access.log") as f:
    for line in f:
        parts = line.split('"')
        if len(parts) < 6:
            continue
        user_agent = parts[-2]
        if user_agent in count_agents:
            count_agents[user_agent] += 1
        else:
            count_agents[user_agent] = 1

for agent,count in count_agents.items():
    print(agent,":", count)