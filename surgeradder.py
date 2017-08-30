import os
import re
import pprint
import sys

# Specify your config file path
# 请声明 Surge 配置文件路径
path = '/Users/USERNAME/Library/Mobile Documents/iCloud~run~surge/Documents/NAMEOFCOFIGFILE.conf' # Use this path if your config file in iCloud. 该路径为 iCloud Surge 文件夹路径。

# Specify your FINAL rule, 'FINAL,DIRECT' as default
# 请声明 Surge 文件中的 FINAL 语句, 默认为 'FINAL,DIRECT'
def  surgeAdder(path, finalRule = 'FINAL,DIRECT', inputDomain = sys.argv[1]):
    with open(path, 'r+') as f:
        content = f.read()
        # Look for where the finalRule starts
        ruleLoc = re.search(finalRule, content).span()[0]

        # Seek the location where the finalRule starts
        f.seek(ruleLoc,0)

        # Writing rule from input
        f.write('DOMAIN-SUFFIX,%s,Proxy\n%s' %(inputDomain, finalRule))
    print('Add %s to config file successfully!' %inputDomain)

surgeAdder(path)
