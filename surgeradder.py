import re
import sys

# Specify your config file path
# 请声明 Surge 配置文件路径
path = '/Users/USERNAME/Library/Mobile Documents/iCloud~run~surge/Documents/NAMEOFCOFIGFILE.conf' # Use this path if your config file in iCloud. 该路径为 iCloud Surge 文件夹路径。

def surgeAdder(path, proxyName = 'Proxy', finalRule = 'FINAL,DIRECT', inputDomain = sys.argv[1]):
    with open(path, 'r+') as f:
        content = f.read()
        # Look for where the finalRule starts
        ruleLoc = re.search(finalRule, content).span()[0]

        # Seek the location where the finalRule starts
        f.seek(ruleLoc,0)

        # Writing rule from input
        f.write('DOMAIN-SUFFIX,%s,%s\n%s\n' %(inputDomain, proxyName, finalRule))
    print('Add %s to config file successfully!' %inputDomain)

surgeAdder(path)
