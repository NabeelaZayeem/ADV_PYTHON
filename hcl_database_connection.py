import mysql.connector
class MysqlDatabaseConnection:
    try:

        def connect(self,host,username,passwd,database):
            self.host=host
            self.username=username
            self.passwd=passwd
            self.database=database
            self.connection=mysql.connector.connect(host=self.host,username=self.username,passwd=self.passwd,database=self.database)
            self.cursor=self.connection.cursor()
    except Exception as e:
        print(e)
