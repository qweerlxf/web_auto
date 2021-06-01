import MySQLdb

conn = MySQLdb.connect(
    host='192.168.1.104',
    user='songqin',
    passwd='songqin',
    db='plession',
    charset='utf8'
)

c = conn.cursor()

c.execute('select * from sq_course')

rows = c.fetchall()
print(rows)

for i in range(c.rowcount):
    row = c.fetchone()
    if row[1] == 'Python':
        print('检查点=>> Python课程找到，通过')
        break
    print(row)

c = conn.cursor()
for x in range(1000):
    c.execute(f"INSERT INTO sq_course(NAME,'desc',display_idx)VALUES('HAHA{x+1}','SDSDSD',6)")
conn.commit()

conn.close()



