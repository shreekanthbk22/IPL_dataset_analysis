import mysql.connector
import json

class create_dict(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value

class data:
    #__init__ function for database connection
    def __init__(self,username,pwd):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user=username,
            password=pwd,
            database="IPL",
            auth_plugin='mysql_native_password'
            )
        print("connection succesfull")

    
    def query1(self):
        mydict = create_dict()
        mycursor = self.mydb.cursor()
        mycursor.execute("select distinct(`dismissal_kind`) as `dismissal_type`, count(*) as `no_of_dismissals` \
                          from `ipl_ball_by_ball` \
                          where `dismissal_kind`!='NA' \
                          group by `dismissal_kind`")
        myresult = mycursor.fetchall()
        
        for row in myresult:
            mydict.add(row[0],({"dismissal_type":row[0],"no_of_dismissals":row[1]}))
        
        stud_json = json.dumps(mydict, indent=2, sort_keys=True)
        return stud_json

    def query2(self):
        mydict = create_dict()
        mycursor = self.mydb.cursor()
        mycursor.execute("select distinct(`fielder`),count(*) as `no_of_catches` from `ipl_ball_by_ball` \
                          where `dismissal_kind`='caught' \
                          group by `fielder` \
                          order by `no_of_catches` desc \
                          limit 10")
        myresult = mycursor.fetchall()
        
        for row in myresult:
            mydict.add(row[0],({"fielder":row[0],"no_of_catches":row[1]}))
        
        stud_json = json.dumps(mydict, indent=2, sort_keys=True)
        return stud_json


if __name__ == "__main__":
    #dataset are stored in local MySQL database 
    print('database used is MySQL')

    #username and password to access database
    username = input("enter username: ")
    pwd = input("enter password: ")
    

    obj = data(username,pwd)

    print('result for Query1: '+obj.query1(),sep="\n")
    
    print('result for Query2: '+obj.query2(),sep="\n")
   