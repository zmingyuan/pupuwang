from pupuwang.utils.Mydb import Mydb

mydb = Mydb('127.0.0.1','root','123455','temp',charset='utf8')

def getproxy():
    sql = 'select * from proxy_kuai ORDER BY rand() limit 1'
    res = mydb.query(sql)
    proxy_info = res[0]
    return proxy_info