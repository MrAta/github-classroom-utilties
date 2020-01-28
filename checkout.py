import os
import sys

if len(sys.argv) < 3:
    print("Usage: phython3 checkout.py /path/to/repos date time")
source_path = sys.argv[1]
ddl = sys.argv[2:]
deadline = " ".join(i for i in ddl)

if not(source_path.endswith("/")):
    source_path+="/"

levels = source_path.count('/') + 1
for subdir in os.walk(source_path):
    for i in subdir:
        if type(i) == str:
            if(len(i.split('/')) == levels):
                os.chdir(i)
                print("Working on ", i)
                os.system("git checkout 'master@{" + deadline+"}'")


