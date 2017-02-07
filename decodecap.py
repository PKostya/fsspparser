from captcha_solver import CaptchaSolver
from orcreader import OrcReader


reader = OrcReader("/home/ubuntu/ffcap.jpeg")
f = reader.open()
print(reader.schema)
print(reader.num_cols)
#solver = CaptchaSolver("contrib", )

#with open(file="/home/ubuntu/ffcap.jpeg", mode="rb") as inp:
 #   raw_data = inp.read()

#solver = CaptchaSolver("contrib", "browser")

#capsolv = solver.solve_captcha(raw_data)
#print(type(capsolv))