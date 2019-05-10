import pymysql.cursors

conn = pymysql.connect(host='localhost',
                         user='root',
                         password='111111',
                         db = 'youtube',
                         charset='utf8mb4')

cursor = conn.cursor()

sql = '''
CREATE TABLE IF NOT EXISTS information (
    title VARCHAR(255) NOT NULL PRIMARY KEY,
    description TEXT,
    defaultLanguage VARCHAR(255),
    publishedAt VARCHAR(255)
    ) ENGINE = InnoDB
'''
cursor.execute(sql)
conn.commit()

sql = '''
CREATE TABLE IF NOT EXISTS caption (
    id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    defaultLanguage VARCHAR(255),
    caption TEXT,
    start VARCHAR(255),
    duration VARCHAR(255),
    FOREIGN KEY(title)
    REFERENCES information(title)
    ON DELETE CASCADE
    ON UPDATE CASCADE
    ) ENGINE = InnoDB
    '''
cursor.execute(sql)
conn.commit()
#cursor.close()

def insert_info(videos_info):
    with conn.cursor() as cursor:
        sql = '''
        INSERT INTO information (title, description, defaultLanguage, publishedAt)
        VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(sql, videos_info)
    conn.commit()

def insert_caption(videos_caption):
    with conn.cursor() as cursor:
        sql = '''
        INSERT INTO caption (title, defaultLanguage, caption, start, duration)
        VALUES (%s, %s, %s, %s, %s)
        '''
        cursor.executemany(sql, videos_caption)
    conn.commit()

#def close_connection():
#    if conn is not None:
#        conn.close()
