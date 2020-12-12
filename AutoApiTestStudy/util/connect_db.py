import pymysql


class ConnectDb:

    def __init__(self):
        self.connection = pymysql.connect(host='192.168.100.78',
                                          port=3306,
                                          user='root',
                                          password='root',
                                          db='51fanli_qilin',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.SSDictCursor)
        self.cur = self.connection.cursor()

    def conn_mysql(self):
        self.cur.execute('select * from tb_qilin_user order by id desc limit 8')
        # result = self.cur.fetchall()

        # print(result)

        for row in self.cur:
            print(row)
            # print('对 cursor 直接进行迭代，每循环一次，从数据库读取一条数据。不会提前把所有数据读取到内存中。')
            # print(row['username'])

        self.cur.close()
        self.connection.close()


if __name__ == '__main__':
    test = ConnectDb()
    test.conn_mysql()
