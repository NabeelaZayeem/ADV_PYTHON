from mysql.connector import Error
from hcl_database_connection import MysqlDatabaseConnection
class Hclstoredprocedure(MysqlDatabaseConnection):
    def execute_str_procedure(self):
        try:
            mydata=('pizza',)
            self.cursor.callproc("get_cust_details",args=mydata)
            for r in self.cursor.stored_results():
                print(r.fetchall())
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
connect_obj=Hclstoredprocedure()
connect_obj.connect("localhost","root","Nabila@123","hcl_vijayawada")
print(connect_obj)
connect_obj.execute_str_procedure()