from subprocess import call
import os

for test in os.listdir('./'):
    if os.path.isfile(test) and not test.startswith('_'):
        call(["python", test])
