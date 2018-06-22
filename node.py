#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import json
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
def setting():
    p = 0
    print "我们将会收取收益的5%作为费用，同意请按P，不同意请按下其他任意键:"
    info = raw_input()
    if info == "p" or info == "P":
        print "正在设置中………"
        if sett == 0:
            if os.makedirs("C:/WWS/date/COINNODE") :
                print "文件夹创建失败！请联系制作者2637037990  "
                print "程序异常 EXIT001"
                print "程序已关闭"
                os._exit(0)
            else:
                while p == 0 :
                    print "请输入您的币种"
                    coinname = raw_input()
                    print "请确认您的币种叫做",coinname,"正确请输入Y"
                    info = raw_input()
                    print info
                    if info == "Y"or info == "y" :
                        f = open("C:/WWS/date/COINNODE/set.inf","w")
                        f.write("#THIS IS WWS PROGRAM SET TXT DO NOT BREAK IT!")
                        f.write("\n")
                        f.write("[coinname] = '")
                        f.write(coinname)
                        f.write("'\n")
                        p = 1
                    else:
                        p = 0
                while p == 1 :
                    print "请输入钱包JSON-RPC IP地址（不包括端口）例：127.0.0.1"
                    info = raw_input()
                    ip = info
                    print "请输入钱包JSON-RPC 端口 例：5201”
                    info = raw_input()
                    port = info
                    print "请输入钱包JSON-RPC 用户名 : WWS"
                    info = raw_input()
                    username = info
                    print "请输入钱包JSON-RPC 密码 : WWS@#$J!@TY#!Y@Ghgew"
                    info = raw_input()
                    password = info
                    f.write("[ip] = '")
                    f.write(ip)
                    f.write("'\n")
                    f.write("[port] = '")
                    f.write(port)
                    f.write("'\n")
                    f.write("[username] = '")
                    f.write(username)
                    f.write("'\n")
                    f.write("[password] = '")
                    f.write(password)
                    f.write("'\n")
                    print "正在测试连接"
                    rpc_connection = AuthServiceProxy("http://"+username+password+"@"+ip+":"+port)
                    commands = [ [ "getblockhash", height] for height in range(100) ]
                    block_hashes = rpc_connection.batch_(commands)
                    blocks = rpc_connection.batch_([ [ "getblock", h ] for h in block_hashes ])
                    block_times = [ block["time"] for block in blocks ]
                    if block_times > -1 :
                        print"测试成功！！！！！！！！"
                        f.write("[ip] = '")
                        f.write(ip)
                        f.write("'\n")
                        f.write("[port] = '")
                        f.write(port)
                        f.write("'\n")
                        f.write("[username] = '")
                        f.write(username)
                        f.write("'\n")
                        f.write("[password] = '")
                        f.write(password)
                        f.write("'\n")
                        p = 2
                    else:
                        p = 1
                        print "对不起！测试失败，请重试!"
        else:
            print "正在读取配置文件中"
            f = open("C:/WWS/date/COINNODE/set.inf")
            z = 0
            k = 0
            read = ""
            while k == 0 :
              z = z + 1
              line = f.readline()
              if z == 1 :
                  if line != "#THIS IS WWS PROGRAM SET TXT DO NOT BREAK IT!\n":
                     k = 1
                     print "数据遭到破坏！！！"
              read = read + line
              print read
              
    else:
        print "正在关闭程序………"
        print "进程关闭"
        os._exit(0)

if os.path.exists("C:/WWS/date/COINNODE")  :
    print "您并不是第一次启动…………"
    sett = 1
    setting();
else:
    print "您应该是第一次启动…………"
    sett = 0
    setting();
