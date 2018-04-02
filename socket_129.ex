[root@centos7 python]# chmod +x socket_129.py 
[root@centos7 python]# python socket_129.py 
  File "socket_129.py", line 17
    (hostname, aliaslist, ipaddrlist+ = host
                                      ^
SyntaxError: invalid syntax
[root@centos7 python]# vi socket_129.py
[root@centos7 python]# python socket_129.py 

------------- Host Information ----------------
('ubuntu', [], ['192.168.0.20'])

---------- Host Information line by------------
ubuntu
[]
['192.168.0.20']

------------- Host Information ----------------
ip :  ubuntu
ip :  192.168.0.20
[root@centos7 python]# 
