import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for chacarter in message:
    count.setdefault(chacarter, 0)
    count[chacarter] = count[chacarter] + 1

print(pprint.pformat(count))
