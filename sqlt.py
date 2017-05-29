import sqlite3 as sqlt
import sys

con = sqlt.connect('test.db')
cur = con.cursor()

# sql = """
# CREATE TABLE empl(id INTEGER primary key autoincrement, name text, tel text, position text);
#
# """

# sql = """
# insert into empl(name,tel,position) VALUES ('Crunky', '770023455555', 'Cleaner');
# """

# sql = """
# insert into empl(name,tel,position) VALUES ('{}','{}','{}');
# """.format('Chunky', '7700234567', 'Moderator')

sql = """
select * from empl;
"""


# cur.executescript(sql) // write in DB without answer
cur.execute(sql)
# print(cur.fetchall())

qur = cur.fetchall()
# for i in qur:
#     print(i[0])
#     print(i)

print(qur)

# cur.close()
# con.close()
