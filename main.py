import random

ans1 = ['No!', 'Yes!', 'maybe']

answser = ""

for x in range(1):
  answser = answser + random.choices(ans1)[0]

print('The answer to your question is:\n', answser)