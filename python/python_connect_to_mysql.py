import pymysql
 
conn = pymysql.connect(
    host='xxx',
    port=portnumber,
    user='xxx',
    password='xxx',
    database='xxx')
 
cursor = conn.cursor() 
#读取
cursor.execute("SELECT content FROM ai_spamchatreview_driver")
# data = cursor.fetchall()
data = cursor.fetchmany(5000)

conn.close()
