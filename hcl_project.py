from hcl_database_connection import MysqlDatabaseConnection
class Booking(MysqlDatabaseConnection):
    def available_seats(self):
        try:
            self.cursor.callproc('get_no_avail_seats')
            for r in self.cursor.stored_results():
                seats=r.fetchall()
                # seats = r.fetchone()
            return seats
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()


    def book(self):
        pass
b1=Booking()
b1.connect("localhost","root","Nabila@123","train")
sts=b1.available_seats()
seats_avl={}

###################################
# seats_avl['Train_number']=sts[0]     line-8 --if fetchone() is used it'll print 1st tuple.
#                                      For printing 1st row from DB
#
# seats_avl['Train_name']=sts[1]
#
# seats_avl['Seat']=sts[2]
# print(seats_avl)
#######################################

data=[]
j=0
for i in sts:


    seats_avl[j]=i
    data.append(i)
    j+=1
s={}
k=1
# keys=['no','name','seats']
d1={}
d1=('Train_number','Train_name','Available_seats')
data1=[]

for d in data:
   # d1['no']=d[0]
   # d1['name']=d[1]
   # d1['seats']=d[2]
   #
   mn = dict(zip(d1,d))
   data1.append(mn)

   k+=1

print(data1)





    #data.append(seats_avl)
# print(seats_avl)
# print(sts)
