import os
import shutil

os.chdir("/home/config")
print(os.system("touch here"))
pd = os.getenv("PWD")
old_pd = os.getenv("OLDPWD")
print(pd, old_pd)
