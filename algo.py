import sqlite3


class Car():
    def Viewcar(self):
        print("********* View Car **********")
        print(
            '''Press 1> To.
            Enter according to which filter you want us to show car details:
            Press 1> To Filter

            Press 2> To.
            All Cars in Available 

            ''')
        type = int(input('''Enter response: '''))
        if type == 1:
            self.type = input('''\n Enter car type:                  
            1> Sedan
            2> Sport
            3> Hatchback
            4> SUV
            ''')
            conn = sqlite3.connect("caruserdata.db")
            cursor = conn.cursor()
            view_query = f"SELECT * FROM Car_data WHERE cartype='{self.type}'"
            cursor.execute(view_query)
            res = cursor.fetchall()
            print("\n\n")
            print(['Car Model', 'Brand', 'Type', 'Colour', 'Reg N0.', 'Price/day','S'])
            for i in res:
                print(f"{list(i)}\n")
            conn.close()
        
        elif type == 2:
            conn = sqlite3.connect("caruserdata.db")
            cursor = conn.cursor()
            view_all = f"SELECT * FROM Car_data"
            cursor.execute(view_all)
            res1 = cursor.fetchall()
            print("\n\n")
            print(['Car Model', 'Brand', 'Type', 'Colour', 'Reg N0.', 'Price/day', 'Status'])
            for j in res1:
                print(f"{list(j)}\n")
            conn.close()

        else:
            print("Invalid Input!!")

    def Deletecar(self):
        print("<<<<<<<<<<<< Enter Car model to delete the Car from Database >>>>>>>>>>")
        print('''\n\nEnter your option: 
        1> Press 1: View Car
        2> Press 2: Delete car
        ''')
        delopt = int(input("\nEnter your option: "))
        if delopt == 1:
            self.Viewcar()
            self.Deletecar()
        elif delopt == 2:
            print("<*********>Mention the following to delete <************>")
            self.carmoddel = input("Enter the Car model name: ")
             
            conn = sqlite3.connect("caruserdata.db")
            cursor = conn.cursor()
            del_query = f"DELETE FROM Car_data WHERE carmodel='{self.carmoddel}'"
            cursor.execute(del_query)
            conn.commit()
            conn.close() 





    def Registercar(self):
        print("************Register New Car ***************")
        self.carmodel = input("Enter car Model name: ")
        self.carbrand = input("Enter car Brand: ")
        self.cartype = input("\nEnter car type (Sedan, Sport, Hatchback, SUV) : ")
        self.colour = input("\nEnter colour of Car: ")
        self.Regnum = input("\nEnter car Register Number: ")
        self.Pricepd = input("\nEnter price per day of the car: ")
        print("**********************************************")

        conn = sqlite3.connect("caruserdata.db")
        cursor = conn.cursor()
        car_entry = '''CREATE TABLE IF NOT EXISTS Car_Data
            (carmodel TEXT, carbrand TEXT, cartype TEXT, carcolour TEXT, carregnum TEXT, price INT, status TEXT)'''
        conn.execute(car_entry)

        car_insert = f"INSERT INTO Car_data (carmodel, carbrand, cartype, carcolour, carregnum, price) VALUES (?, ?, ?, ?, ?, ?)"
        car_val = (self.carmodel, self.carbrand, self.cartype, self.colour, self.Regnum, self.Pricepd)
        cursor.execute(car_insert, car_val)
        conn.commit()
        conn.close()
        


    
    

class User(Car):


    def Rentcar(self):

        print(f"***********************Hello> {self.logusername} Welcome to Luid Car Rental Service ******************************")
        
        print("\n\n***************** Kindly Enter your details ****************")
        self.customer_name = input("\n\nEnter your Fullname: ")
        self.gender = input("\n Enter your gender (Male / Female): ")
        self.dob = input("\nEnter your DOB: ")
        self.licensenumber = input("\nEnter your License Number: ")
        self.rent_model = input("\nEnter Car model name: ")
        self.from_rent = input("\nRent car from (dd/mm/yyyy): ")
        self.upto = input("\nRent car upto (dd/mm/yyyy): ")
        print("\n***************************************************************")

      
        conn = sqlite3.connect("caruserdata.db")
        cursor = conn.cursor()
        table_rent_query = '''CREATE TABLE IF NOT EXISTS Rent_Data
            (customername TEXT, customergender TEXT, customerdob DATE, customerlicnum TEXT, carmodel TEXT, rentedfrom DATA, rentedupto DATE)'''
        conn.execute(table_rent_query)
        insert_detail = f"INSERT INTO Rent_Data (customername, customergender, customerdob, customerlicnum, carmodel, rentedfrom, rentedupto) VALUES (?, ?, ?, ?, ?, ?, ?)"
        insert_val = (self.customer_name, self.gender, self.dob, self.licensenumber, self.rent_model, self.from_rent, self.upto)
        cursor.execute(insert_detail, insert_val)
        conn.commit()
        conn.close()

        conn = sqlite3.connect("caruserdata.db")
        cursor = conn.cursor()
        update_query = f"UPDATE Car_Data SET status='Rented Already' WHERE carmodel='{self.rent_model}'"
        cursor.execute(update_query)
        conn.commit()
        conn.close()
        print("\n\n Successfully Rented Car")
        self.interface()

    
    def interface(self):
        print('''\n\n <<<<<<<<< Choose anyone option >>>>>>>>>
            1> Press 1 to Rent a Car.
            2> Press 2 to View a Car
            3> Press 3 to exit
            
            *******************************************************''')
        choose = int(input("\nEnter your choice: "))
        if choose == 1:
                self.Rentcar()
                
        elif choose == 2:
                self.Viewcar()
                self.interface()

        elif choose == 3:
                exit
        else:
                print("Invalid Input!!!")

        

    def login(self):
        print("> Press 1. To stay in login page. <<<<<<<<<<<<")
        print("\n> Press 2. To go in signup page.  <<<<<<<<<<<<")     
        val = int(input("\nEnter your option>>> "))

        if val == 1:
            self.logusername = input("Enter login username: ")
            self.logpassword = input("\nEnter login password: ")
            conn = sqlite3.connect("caruserdata.db")
            cursor = conn.cursor()
            statement = f"SELECT username from Customer_Data WHERE username='{self.logusername}' AND Password = '{self.logpassword}';"
            cursor.execute(statement)
            if not cursor.fetchone():  # An empty result evaluates to False.
                print("**************Incorrect Login Details***************")
                self.login()
            else:
                print("********************Welcome To Car Rental***************************")

            conn.close()
            self.interface()
        
        elif val == 2:
            self.signup()

        else:
            print("Invalid input!!")

        conn.close()
        


    def signup(self):

        print("******************************SignUp window*************************")
        self.username = input("Enter your username: ")
        self.password = input("Enter your password containing 6 character or more: ")
        self.comfirm_password = input("Enter password again to confirm it: ")
        
        if self.password == self.comfirm_password and len(self.password) >= 6:
            print("Signup Successfully")
            print("****************************************************************")
            conn = sqlite3.connect("caruserdata.db")
            cursor = conn.cursor()
            table_create_query = '''CREATE TABLE IF NOT EXISTS Customer_Data
            (username TEXT, password TEXT)
            '''
            conn.execute(table_create_query)
            data_insert_query = '''INSERT INTO Customer_Data (username ,password) VALUES (?, ?)'''
            data_insert_tuple = (self.username, self.password)

            cursor.execute(data_insert_query, data_insert_tuple)
            conn.commit()

            conn.close()
            self.login()




        elif len(self.password) < 6:
            print("ERROR!!!!!","Enter password containing characters more then!")
            self.signup()

        else:
            print("ERROR!!!!!","Both password should match!! ")
            self.signup()






class Rental(User):
        def Updaterent(self):
            print('''Select any one Option to change Rent details
            1> Update Car Status (Press 1.)
            2> From Date change (Press 2.)
            3> Upto Date change (Press 3.)
            ''')
            updateopt = int(input("Enter your choise: "))
            if updateopt == 1:
                self.carupdate = input("\nEnter the car model name: ")
                self.statuscar = input("\nEnter the status of the Specific car (Not available, Available): ")
                conn = sqlite3.connect("caruserdata.db")
                cursor = conn.cursor()
                update_status = f"UPDATE Car_Data SET status='{self.statuscar}' WHERE carmodel='{self.carupdate}'"
                cursor.execute(update_status)
                conn.commit()
                conn.close()

            elif updateopt == 2:
                self.carmod = input("\nEnter the car model name: ")
                self.fromcardate = input("\nEnter New from car rent date(dd/mm/yyyy) : ")
                conn = sqlite3.connect("caruserdata.db")
                cursor = conn.cursor()
                update_status_date = f"UPDATE Rent_Data SET rentedfrom='{self.fromcardate}' WHERE carmodel='{self.carmod}'"
                cursor.execute(update_status_date)
                conn.commit()
                conn.close()
            

            elif updateopt == 3:
                self.carmod1 = input("\nEnter the car model name: ")
                self.uptocardate = input("\nEnter New upto car rent date(dd/mm/yyyy) : ")
                conn = sqlite3.connect("caruserdata.db")
                cursor = conn.cursor()
                update_status_date_upto = f"UPDATE Rent_Data SET rentedupto='{self.uptocardate}' WHERE carmodel='{self.carmod1}'"
                cursor.execute(update_status_date_upto)
                conn.commit()
                conn.close()
            
            else:
                 print("Invalid Input!!!")

        def Deleterent(self):
                print("****************** Delete Rental Entry ********************")
                self.cardelmod = input("\nEnter the car model name from Rental data: ")
                conn = sqlite3.connect("caruserdata.db")
                cursor = conn.cursor()
                del_carrent = f"DELETE FROM Rent_data WHERE carmodel='{self.cardelmod}'"
                cursor.execute(del_carrent)
                conn.commit()
                conn.close()

        def Viewrent(self):
                print("********* View Rented Data **********")

                enterstart = int(input("Enter Anything. To show all results for Rental data:\n\n"))
                    
                conn = sqlite3.connect("caruserdata.db")
                cursor = conn.cursor()
                view_all = f"SELECT * FROM Rent_data"
                cursor.execute(view_all)
                res1 = cursor.fetchall()
                print("\n\n")
                print(['Customer Name', 'Gender', 'DOB', 'Customer License no', 'Car Model', 'Rented From', 'Rented Upto'])
                for j in res1:
                    print(f"{list(j)}\n")
                conn.close()
        
               





class Employee(Rental):
        
        def emplogin(self):
            self.empusername = "admin"
            self.emppassword = "carrental"
            logempuser = input("Enter employee username: ")
            logemppass = input("Enter employee password: ")
            if self.empusername == logempuser and self.emppassword == logemppass:
                self.emppage()

            else:
                 print("Invalid Username or Password")
                 self.emplogin()


        def emppage(self):
                print('''************************** Employee main Page**********************************
                1> Press 1. To View all Cars
                2> Press 2. To Delete Car from Data
                3> Press 3. To Register new Car
                4> Press 4. To View all Rental Details
                5> Press 5. To Update Rent Service
                6> Press 6. To Delete Rent Service
                7> Press 7. To EXIT\n''')

                empopt = int(input("Enter your response: "))
                if empopt == 1:
                     self.Viewcar()
                     self.emppage()
                
                elif empopt == 2:
                     self.Deletecar()
                     self.emppage()

                elif empopt == 3:
                     self.Registercar()
                     self.emppage()

                elif empopt == 4:
                     self.Viewrent()
                     self.emppage()

                elif empopt == 5:
                     self.Updaterent()
                     self.emppage()

                elif empopt == 6:
                     self.Deleterent()
                     self.emppage()

                elif empopt == 7:
                     exit

                else:
                     print("Invalid input!!")





user1 = User()
emp1 = Employee()

#user1.login()
emp1.emplogin()