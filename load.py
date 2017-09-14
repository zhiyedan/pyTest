import MySQLdb
import time

start = time.time()
count = 1000

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'sj',
    'db': 'test',
    'charset': 'utf8'
}
conn = MySQLdb.connect(**config)
conn.autocommit(1)
cursor = conn.cursor()

file = open('/home/zhiyedan/Desktop/test2','r')

validData = []

for line in file:
    item = line.split('\t')
    # if (item[5] == 'NULL' or item[6] == 'NULL'):
    if (not item[1].strip() or item[1] == 'NULL' or not item[2].strip() or item[2] == 'NULL'):
        continue
    item_str = "','".join(item)
    validData.append(item_str)

totalLen = len(validData)
sub_sql = ''
while len(validData) > 0 :
    for j in range(1,count):
        if len(validData)<=0:
            break
        sub_sql = (sub_sql + '(\'' +validData.pop()).strip('\r\n')+'\'),'
    sub_sql =  sub_sql.strip(',')
#    sql = "insert into mbk_ride17917 (user_id,reg_date,first_order_date,max_order_duration,order_cnt,sum_dist_km,sum_dura_hr,freq_district,max_order_date,max_order_cnt,rushhour_order_cnt,sum_redpacket,first_order_city,sum_order_day) values " + sub_sql
    sql =  "insert into users (name,age,birthday,rade) values " + sub_sql
    print 'sql is :' + sql
    try:
        cursor.execute(sql)
        conn.commit()
        print 'ok!'
        print 'left '+len(validData)+' data, percent :' + len(validData)/totalLen + '\%'
    except:
        conn.rollback()

cursor.close()
conn.close()
end = time.time() - start
print end
