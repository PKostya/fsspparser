from grab import Grab
import re
import base64
from captcha_solver import CaptchaSolver
import logging

gInfo = {
'obj': g.go(url),
'Headers-C-T': g.response.headers['Content-Type'],
'url': g.response.url,
'urlDetails': g.response.url_details()
}
capHtml = gInfo['obj'].unicode_body(ignore_errors=True, fix_special_entities=True)
b64cap = re.findall(r'base64,(.*?)\\" id=', capHtml, re.DOTALL)
savecaptcha = open(file="/home/ubuntu/captcha.png", mode="w")
savecaptcha.write(str(b64cap[0]))
savecaptcha.close()

f = open(file="/home/ubuntu/captcha.png", mode="rb")
r = f.read()
i = base64.b64decode(r)
f.close()

fincapfile = open(file="/home/ubuntu/ffcap.jpeg", mode="wb")
capsave = fincapfile.write(i)
fincapfile.close()

inp = input(str())
inpr = re.compile(inp, flags=1)
g2.set_input("code", inp)
g2.submit(name_request=False)