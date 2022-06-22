import time
import datetime
import pytz
import psycopg2


def database():
    conn = psycopg2.connect(host="ec2-54-247-125-38.eu-west-1.compute.amazonaws.com", database="da6enidfepcbi1",
                            user="wurekozwyaopqg",
                            password="b0c8f6c86460cf8be32c8df87286851234d400c28e300ed995a2bdf016ab5baa")
    return conn


def create_table_users():
    conn = database()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, " +
                   "chat_id VARCHAR(50), step VARCHAR(64), quantity INT, reg_date TIMESTAMP)")
    conn.commit()
    conn.close()
    return



def is_user(chat_id):
    conn = database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE chat_id='{}'".format(chat_id))
    result = cursor.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False

def is_blocked(chat_id):
    conn = database()
    cursor = conn.cursor()
    cursor.execute("SELECT blocked FROM users WHERE chat_id='{}'".format(chat_id))
    result = cursor.fetchone()
    conn.close()
    if result[0]:
        return True
    else:
        return False



def add_user(chat_id):
    conn = database()
    cursor = conn.cursor()
    date = datetime.datetime.now(pytz.timezone("Europe/Kiev"))
    cursor.execute("INSERT INTO users (chat_id,step,reg_date) VALUES (%s,%s,%s)", (chat_id,0,date))
    conn.commit()
    conn.close()
    return

def white(number):
    conn = database()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO whitelist (number) VALUES ('{number}')")
    conn.commit()
    conn.close()
    return

def is_white(number):
    conn = database()
    cursor = conn.cursor()
    cursor.execute("SELECT number FROM whitelist WHERE number='{}'".format(number))
    result = cursor.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False

def set_step(chat_id,step):
    conn = database()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET step='{}' WHERE chat_id='{}'".format(step,chat_id))
    conn.commit()
    conn.close()
    return

def block(chat_id):
    conn = database()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET blocked=TRUE WHERE chat_id='{}'".format(chat_id))
    conn.commit()
    conn.close()
    return

def unblock(chat_id):
    conn = database()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET blocked=False WHERE chat_id='{}'".format(chat_id))
    conn.commit()
    conn.close()
    return

def get_step(chat_id):
    conn = database()
    cursor = conn.cursor()
    cursor.execute("SELECT step FROM users WHERE chat_id='{}'".format(chat_id))
    result = cursor.fetchone()
    conn.close()
    return result[0]


def users():
    conn = database()
    cursor = conn.cursor()
    start = datetime.datetime.now(pytz.timezone('Europe/Kiev')).strftime('%Y-%m-%d 00:00:00')
    finish = datetime.datetime.now(pytz.timezone('Europe/Kiev'))
    cursor.execute("SELECT * FROM users WHERE reg_date BETWEEN '{}' AND '{}'".format(start,finish))
    result = cursor.fetchall()
    conn.close()
    return len(result)

def all_users():
    conn = database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    conn.close()
    return len(result)

def all_users_send():
    conn = database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    conn.close()
    return result

# create_table_users()

# print()

if not is_white('+380996626944'):
    print(1)
else:
    print(2)