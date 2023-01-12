import psycopg2

def connectDB():
    conn = psycopg2.connect(
        host="isilo.db.elephantsql.com",
        database="tfcgdopt",
        user="tfcgdopt",
        password="yqIAIr-LQEz6-Ppn27sM8LA4vN9BFzRE")
    print(conn)
    return conn

def makeCursor(conn):
    cur = conn.cursor()
    return cur

# conn = connectDB()
# cur = makeCursor(conn)

# cur.execute("DROP TABLE IF EXISTS test_table")
# a = 'wbi'
# cur.execute("""CREATE TABLE test_table (
# 				name VARCHAR(32),
# 				age INT);
# 			""")
# cur.execute("INSERT INTO test_table (name, age) VALUES (%s, %s)",(name,age))
# conn.commit()