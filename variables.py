import os
from demo import a

print("HOME: "+os.environ.get("HOME", ""))
print("SHELL: "+os.environ.get("SHELL",""))
print("FRUIT: "+os.environ.get("FRUIT", ""))

v=a
print(v)