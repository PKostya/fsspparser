import fs


gInfo = {

'obj': g2.go(capUrl),

'Headers-C-T': g2.response.headers['Content-Type'],

'url': g2.response.url,

'urlDetails': g2.response.url_details()

}

capHtml = capHtml = gInfo['obj'].unicode_body(ignore_errors=True, fix_special_entities=True)

b64cap = re.findall(r'base64,(.*?)\\" id=', capHtml, re.DOTALL)

savecaptcha = open(file="/home/ubuntu/captcha.png", mode="w")

savecaptcha.write(b64cap[0])

savecaptcha.close()

f = open(file="/home/ubuntu/captcha.png", mode="rb")

r = f.read()

i = base64.b64decode(r)

f.close()

fincapfile = open(file="/home/ubuntu/workspace/ffcap.jpeg", mode="wb")

capsave = fincapfile.write(i)

fincapfile.close()