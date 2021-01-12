import pymysql


def connect():
    db = pymysql.Connect(
        host="localhost", port=3306, user="root", passwd="admin@06.", db="recruit", charset="utf8",
    )
    cursor = db.cursor();

    createDatabase = """CREATE TABLE IF NOT EXISTS job(
                            name VARCHAR(255),
                            city VARCHAR(255) ,
                            address VARCHAR(255) ,
                            experience VARCHAR(255) ,
                            post VARCHAR(255)
                          )
                          """

    cursor.execute(createDatabase)

    readCsvSendSql(cursor)

    db.commit()


#读取csv文件 并写入到mysql数据库中
def readCsvSendSql(cursor):
    with open('data/job.csv') as file:
        for csvStr in file.readlines():
            strs = csvStr.replace("\n", "").split(",")
            sql = "INSERT INTO job(name,city,address,experience,post) values ({0},{1},{2},{3},{4})".format(
                "'" + strs[0] + "'",
                "'" + strs[1] + "'",
                "'" + strs[2] + "'",
                "'" + strs[3] + "'",
                "'" + strs[4] + "'")
            cursor.execute(sql)


if __name__ == '__main__':
    connect()
