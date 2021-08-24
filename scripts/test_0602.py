import pymysql

sql = "SELECT count( 1 ) num,c.ZJ,c.MC,z.ZJ AS ryzt,z.MC AS ryztmc " \
      "FROM jc_ryxx a " \
      "LEFT JOIN jc_qyxx b ON a.QYZJ = b.QYZJ " \
      "LEFT JOIN zd_xzqh c ON c.ZJ = b.CS " \
      "LEFT JOIN zd_gy_zdsj z ON a.RYZT = z.ZJ GROUP BY c.ZJ,c.MC,z.ZJ,z.MC"

db = pymysql.connect("192.168.0.50", "syb", "a123456", "gfpj")
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
cursor.execute(sql)
data = cursor.fetchall()
# for i in data:
#     print("字段:", i, "值", data[i])
# print(data)
for i in data:
    print(i)
    print()
cursor.close()
db.close()
