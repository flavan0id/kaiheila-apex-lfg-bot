import sqlite3 as sql
conn = sql.connect('apexLfg')
c = conn.cursor()

def doSql(rank: str):
    ret = []
    cursor = c.execute("SELECT * FROM ? ORDER BY c DESC", [rank])
    for row in cursor:
        ret.append(row[0] + row[1])

while True:
    msg = input()
    if not msg.startswith('!'):
        continue
    c.execute
    
