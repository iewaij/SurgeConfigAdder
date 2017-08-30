# SurgeConfigAdder
使用命令行或者 Alfred 为你的 Surge 域名配置文件添加规则。
Add domain rules for your surge config file, using terminal or Alfred.

## 命令行中使用
下载 `surgeadder.py`，更改文件中的 `path` 变量为 Surge 配置文件的位置，务必保留引号。

更改 `'FINAL,DIRECT'` 为 Surge 配置文件的 FINAL 字段（如果你不知道要不要改，就别改了）。

更改路径至 `surgeadder.py` 所在文件夹。

```cd PATH/TO/FOLDER```
![Screen Shot 2017-08-30 at 11.10.54 PM](https://i.loli.net/2017/08/30/59a6d63979a5e.png)

输入 `python3 surgeadder.py domain.com`，`domain.com` 为需要翻墙的网站域名。
![Screen Shot 2017-08-30 at 11.12.24 PM](https://i.loli.net/2017/08/30/59a6d69e94bb4.png)

在 Surge 任务栏面板里点击重新加载。或者使用 surge-cli 命令重新加载配置文件。
![Screen Shot 2017-08-31 at 12.43.18 AM](https://i.loli.net/2017/08/31/59a6eb33cb7b6.png)

## Alfred 中使用

打开终端，输入以下命令启用 surge-cli。
```ln -s /Applications/Surge.app/Contents/Applications/surge-cli /usr/local/bin/surge-cli```

注意，Surge 在 2.0 版本以后改变了 surge-cli 的位置，如果你在之前启用了 surge-cli，需要前往 `/usr/local/bin/` 目录删除 `surge-cli`。

经过我的测试，此时输入 `surge-cli reload` 命令就能重新加载配置文件。如果这一步失败，请参阅 [Surge CLI 开始测试](https://medium.com/@Blankwonder/surge-cli-开始测试-70bef9fd7169)。


确认你已经购买 Alfred Powerpack，下载 `SurgeConfigAdder.alfredworkflow` 并导入 Alfred。编辑终端命令，更改 `path` 变量为配置文件所在位置，务必保留引号。
![Screen Shot 2017-08-31 at 12.30.21 AM](https://i.loli.net/2017/08/31/59a6e8267378f.png)

更改 `FINAL,DIRECT` 为 Surge 配置文件的 FINAL 字段（如果你不知道要不要改，就别改了），务必保留引号。
![Screen Shot 2017-08-31 at 12.31.08 AM](https://i.loli.net/2017/08/31/59a6e854632d6.png)

在 Alfred 中输入 `add domain.com` 即可添加规则。
![Screen Shot 2017-08-30 at 11.26.09 PM](https://i.loli.net/2017/08/30/59a6d92b0008d.png)

## 实现逻辑
使用 Python3 查找 Surge 配置文件 `surge.conf` 的 FINAL 字段，并在该位置覆盖 `DOMAIN-SUFFIX,domain.com,Proxy` 和 FINAL 字段。如果你对改动有其他要求，编辑`f.write('DOMAIN-SUFFIX,%s,Proxy\n%s\n' %(inputDomain, finalRule))`。改动完毕后，使用 `surge-cli reload` 命令重新加载配置文件。
