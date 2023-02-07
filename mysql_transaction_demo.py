from mysql.connector import Error
from hcl_database_connection import MysqlDatabaseConnection
class Hclpythontransaction(MysqlDatabaseConnection):
    def execute_transaction_query(self):
        custid=2
        sql="delete from customer where cust_id=%s"
        try:
            self.cursor.execute(sql,(custid,))
            self.connection.commit()
        except:
            self.connection.rollback()
            print("something went wrong")
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
connect_obj=Hclpythontransaction()
connect_obj.connect("localhost","root","Nabila@123","hcl_vijayawada")
connect_obj.execute_transaction_query()