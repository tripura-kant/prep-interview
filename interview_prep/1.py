# if-else

status = 200

if status >= 500:
    print("server error")
elif status >= 400:
    print("client error")
else:
    print("not found")        