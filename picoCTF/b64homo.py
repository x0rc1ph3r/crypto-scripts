import requests
import base64
s=requests.Session()
s.get("http://mercury.picoctf.net:25992/")
cookie = s.cookies["auth_name"]
unb64 = base64.b64decode(cookie)
unb64b = base64.b64decode(unb64)

for i in range (0,128):
    pos = i // 8
    guessdec = guessdec = unb64b[:pos] + chr(ord(unb64b[pos]) ^ (1 << (i % 8))) + unb64b[pos+1:]
    guessenc1 = base64.b64encode(guessdec)
    guess = base64.b64encode (base64.b64encode(guessdec))
    r = requests.get("http://mercury.picoctf.net:25992/", cookies={"auth_name": guess})
    if "pico" in r.text:
        print (r.text)
        break

# run with python2
