# SurgeConfigAdder
在命令行界面为你的 Surge 域名配置文件添加规则，搭配 Alfred 体验更佳。  
Add domain rules for your surge config file, better with Alfred.

## 配置
下载 `surgeadder.py`，更改文件中的 `path` 变量为 Surge 配置文件的位置，更改 `'FINAL,DIRECT'` 为 Surge 配置文件的 FINAL 字段（如果你不知道要不要改，就别改了）。

## 命令行中使用
更改路径至 `surgeadder.py` 所在文件夹。

```cd PATH/TO/FOLDER```
![Screen Shot 2017-08-30 at 11.10.54 PM](https://i.loli.net/2017/08/30/59a6d63979a5e.png)

输入 `python3 surgeadder.py domain.com`，`domain.com` 为需要翻墙的网站域名。
![Screen Shot 2017-08-30 at 11.12.24 PM](https://i.loli.net/2017/08/30/59a6d69e94bb4.png)

## Alfred 中使用
确认你已经购买 Alfred Powerpack，下载 `SurgeConfigAdder.alfredworkflow` 并双击导入 Alfred，编辑终端命令，更改路径为`surgeadder.py` 所在位置。
![Screen Shot 2017-08-30 at 11.21.47 PM](https://i.loli.net/2017/08/30/59a6d840b4268.png)

在 Alfred 中输入 `add domain.com` 即可添加规则。
![Screen Shot 2017-08-30 at 11.26.09 PM](https://i.loli.net/2017/08/30/59a6d92b0008d.png)

## 实现逻辑
查找 Surge 配置文件 surge.conf 的 FINAL 字段，并在该位置覆盖 `DOMAIN-SUFFIX,domain.com,Proxy` 和 FINAL 字段。如果你对改动有其他要求，编辑`f.write('DOMAIN-SUFFIX,%s,Proxy\n%s\n' %(inputDomain, finalRule))`。
