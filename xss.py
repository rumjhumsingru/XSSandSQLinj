import requests
fname = "payloads.txt"
with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
payloads = [x.strip() for x in content] 
url = input("URL: ")
vuln = []
for payload in payloads:
    payload = payload
    xss_url = url+payload
    r = requests.get(xss_url)
    print(r.text.lower())
    if payload.lower() in r.text.lower():
        print(" XSS Vulnerable: " + payload)
        if(payload not in vuln):
            vuln.append(payload)
    else:
        print("This site is not vulnerable to Cross-Site Scripting!")

print ("--------------------\nAvailable Payloads:")
print ('\n'.join(vuln))


# https://xss-game.appspot.com/level1
# https://www.google.com/