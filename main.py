n = int(input())
valid_emails = []
for i in range(n):
    email = input()
    valid_emails.append(email)
for i in valid_emails:
    if email.endswith("sigma.com"):
        print(i)




