from tkinter import *

# from tkinter library importing message_box module
from tkinter import messagebox

# from Python Imaging Library (PIL) and import module ImageTk and Image module
from PIL import ImageTk,Image  

# Import mysql.connector driver for connecting to database
import mysql.connector as sql_db

# PARENT CLASS
class user():
  # Constructor of user
  def __init__(self,username,age,gender):
    self.username = username
    self.age = age
    self.gender = gender


# CHILD CLASS
class bank(user):
  # Constructor of bank
  def __init__(self, username, age, gender):
    super().__init__(username,age,gender)
    self.balance = 0
    self.password = ''

  def check_balance(self):
    mydb = sql_db.connect(host='localhost',
                            user='root',
                            password='admin',
                            database = 'bank_management')

     # using cursor function creating cursor object so we can execute all queries / Operations
    cur = mydb.cursor()

    # Query / Operatations
    Check = f"SELECT balance from passbook WHERE username = '{self.username}'"
      

    cur.execute(Check)
    # creating a database call BANK_MANAGEMENT with the help of execute function 
    rows = cur.fetchall()
    print(rows)
    mydb.close()
    # fetching balance from passbook table of bank_management database
    for i in range(0,1):
      res = [lis[i] for lis in rows]
      self.balance = res[0]

    print("Mr.",self.username,"your current balance in account is : ",self.balance)


  def amount_deposit(self, amount):
    # using connect function to establish connection to database at any host
      mydb = sql_db.connect(host='localhost',
                            user='root',
                            password='admin',
                            database = 'bank_management')

      # using cursor function creating cursor object so we can execute all queries / Operations
      cur = mydb.cursor()

      self.balance += amount
      # Query / Operatations
      Modify_into_passbook = f"UPDATE passbook SET balance = {self.balance},deposit = {amount} where username = '{self.username}'"

      # creating a database call BANK_MANAGEMENT with the help of execute function
      cur.execute(Modify_into_passbook)

      
      # commit() function help to reflect changes in database bank_management 
      mydb.commit()    

      mydb.close()
      
      print("The amount of RS.",amount,"has been deposited to your Bank of World Account successfully.")
      print(f'Mr.{self.username} your remaining balance in account is {self.balance}')
 

  def withdraw(self,amount):
    if self.balance >= amount :
      mydb = sql_db.connect(host='localhost',
                            user='root',
                            password='admin',
                            database = 'bank_management')

      # using cursor function creating cursor object so we can execute all queries / Operations
      cur = mydb.cursor()

      self.balance -= amount
      # Query / Operatations
      Modify_into_passbook = f"UPDATE passbook SET balance = {self.balance}, withdraw = {amount} where username = '{self.username}'"

      # creating a database call BANK_MANAGEMENT with the help of execute function
      cur.execute(Modify_into_passbook)

      
      # commit() function help to reflect changes in database bank_management 
      mydb.commit()    

      mydb.close()
     
      print("The amount of RS.",amount,"has been withdraw from your Bank of World Account successfully.")
      print(f'Mr.{self.username} your remaining balance in account is {self.balance}')

    else :
      print(f'Sorry Mr.{self.username}, cannot withdraw more money ! as your withdraw amount {amount} exceeds your remaining balance {self.balance} RS')
      print(f'{self.username} your remaining balance in account is {self.balance}')

      
  def student_Loan(self,cgpa,loan_amount):
    if 6 <= cgpa < 7:
      print("You will get 50% of our loan amount",loan_amount)
      print("So, you will get the loan of Rs.",loan_amount*0.5)
    elif(7 <= cgpa< 8):
      print("You will get 75% of our loan amount",loan_amount)
      print("So, you will get the loan of Rs.",loan_amount*0.75)
    elif( 8 <=cgpa< 9):
      print("You will get 90% of our loan amount",loan_amount)
      print("So, you will get the loan of Rs.",loan_amount*0.9)
    
    elif(9 <=cgpa <= 10.0):
      print("You will get 100% of our loan amount",loan_amount)
      print("So, you will get the loan of Rs.",loan_amount)

    else:
      print("Sorry, you are not eligible to get the loan since your CGPA is less.")
      print("Thank you for applying for loan to/with Bank of World of World")

  def car_Loan(self,loan_amount,annual_income):
      if self.age>=21:
        if annual_income >=300000:
          loan_amount_eligible= loan_amount*0.6   #loan*60%          
          print("Congragulations, you are eligible for the loan amount of RS ",loan_amount_eligible, "i.e 60% of your loan_amount.")
        else:
          print("Sorry, you are not eligible to get the loan since your minimum annual income is not more than our expected income i.e RS 300000 LPA")
          print("Thank you for applying loan to/with Bank of World")
      else:
        print("Sorry, you are not eligible to get the loan since your age is less than 21 years")
        print("Thank you for applying loan to/with Bank of World of World")
          
 #                   Assuming the interest @ 10.5%
 #               Loan Tenure (in Years) |  Per Lac EMI
 #                       5              |     2150
 #                       10             |     1350
 #                       15             |     1100
 #                       20             |     1000
 #                       25             |      945
 #                       30             |      915


  def home_loan(self,loan_amount,annunal_income,other_emi_proceeding,loan_tenure):
      if self.age >= 21:
                          # loan_amount = (annual income*(50%) - other_emi_proceeding) / per LPA EMI

        if loan_tenure <= 5:  #min or starting  5 years
          loan_amount_eligible=((annunal_income*0.5)-other_emi_proceeding)/2150
          print("Congragulations, you are eligible for the loan amount of RS ",loan_amount_eligible,"lakh only with an interest of 10.5% & an EMI of RS 2150.")
        elif (loan_tenure>5 and loan_tenure<=10):
          loan_amount_eligible=((annunal_income*0.5)-other_emi_proceeding)/1350
          print("Congragulations, you are eligible for the loan amount of RS ",loan_amount_eligible,"lakh only with an interest of 10.5% & an EMI of RS 1350")
        elif (loan_tenure>10 and loan_tenure<=15):
          loan_amount_eligible=((annunal_income*0.5)-other_emi_proceeding)/1100
          print("Congragulations, you are eligible for the loan amount of RS ",loan_amount_eligible,"only lakh with an interest of 10.5% & an EMI of RS 1100")
        elif (loan_tenure>15 and loan_tenure<=20):
          loan_amount_eligible=((annunal_income*0.5)-other_emi_proceeding)/1000
          print("Congragulations, you are eligible for the loan amount of RS ",loan_amount_eligible,"only lakh with an interest of 10.5% & an EMI of RS 1000")
        elif (loan_tenure>20 and loan_tenure<=25):
          loan_amount_eligible=((annunal_income*0.5)-other_emi_proceeding)/945
          print("Congragulations, you are eligible for the loan amount of RS ",loan_amount_eligible,"only lakh with an interest of 10.5% & an EMI of RS 945")
        else:
          loan_amount_eligible=((annunal_income*0.5)-other_emi_proceeding)/915
          print("Congragulations, you are eligible for the loan amount of RS ",loan_amount_eligible,"only lakh with an interest of 10.5% & an EMI of RS 915")


      else:
        print("Sorry, you are not eligible to get the loan since your age is less than 21 years")
        print("Thank you for applying loan to/with Bank of World")

# GUI CLASS IS CHILD OF Bank of World CLASS 
# GUI class is used to created the gui window that associated with the Bank of World method and actions and help for more convinence and friendly
# interface for user.

class GUI(bank):
    # Constructor of GUI
    def __init__(self, username, age, gender,password):
        super().__init__(username, age, gender)
        

    def menu(self):

        top = Toplevel()
        top.geometry('800x500')      
        top.title("MENU WINDOW")

        Label(top, text="Bank of World Services", font=('arial Bold',30), bg='sky blue').pack()
        Label(top,text=f'Welcome {self.username}, choose your below Bank of World services:-', font=('Modern bold',17)).place(x=25,y=80)

        check_bal = Radiobutton(top,text='Check Balance', font=('arial bold italic',15),variable = radio_var, value=1).place(x=280, y=145) 

        deposit = Radiobutton(top,text='Deposit Money', font=('arial bold italic',15),variable = radio_var, value=2).place(x=280, y=185) 

        withdraw = Radiobutton(top,text='Withdraw Money', font=('arial bold italic',15),variable = radio_var, value=3).place(x=280, y=225)

        loan =  Radiobutton(top,text='Apply for loan', font=('arial bold italic',15),variable = radio_var,value=4).place(x=280, y=265)

        submit = Button(top, text='Submit', font=('arial Bold',15), bg='sky blue',fg='black',command= self.submit_menu).place(x=280, y=360)
        exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=400, y=360)

    def submit_menu(self):
       # fetching the user input using get() (a built_in function) to their respective variables

        radio = radio_var.get()  
        if radio == 0:
            messagebox.showerror("Error","Please select your choice :(")  # Showing an error message box 
        if radio == 1:
            self.gui_check_balance()               # INVOKING GUI CHECK FUNCTION 
        if radio == 2:
            self.gui_deposit()                     # INVOKING GUI DEPOSIT FUNCTION 
        if radio == 3:
            self.gui_withdraw()                    # INVOKING GUI WITHDRAW FUNCTION 
        if radio == 4:
            username = 'Dear ' + self.username +', choose your type of loan'
            top = Toplevel()
            top.geometry('800x500')      
            top.title("LOAN TYPE WINDOW")
            Label(top, text="Bank of World", font=('arial bold',30), bg='sky blue').pack()
            Label(top,text=username, font=('arial bold',17)).place(x=60,y=70)

            student_loan = Radiobutton(top,text='Student loan', font=('arial bold italic',15),variable = loan_radio_var, value=1).place(x=280, y=145) 

            car_loan = Radiobutton(top,text='Car loan', font=('arial bold italic',15),variable = loan_radio_var, value=2).place(x=280, y=185) 

            Home_loan = Radiobutton(top,text='Home loan', font=('arial bold italic',15),variable = loan_radio_var, value=3).place(x=280, y=225)


            submit = Button(top, text='Submit', font=('arial Bold',15), bg='sky blue',fg='black',command= self.gui_loan_menu).place(x=280, y=350) # INVOKING GUi LOAN MENU FUNCTION 
            exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=400, y=350)


    def gui_check_balance(self):
        temp_list = []
        top = Toplevel()
        top.geometry('800x500')      
        top.title("CHECK BALANCE WINDOW") 
        Label(top, text="Thanks for choosing Bank of World", font=('arial bold',30), bg='sky blue').pack()
        # INVOKING THE CHECK BALANCE FUNCTION
        self.check_balance()
        Label(top, text=f'Dear {self.username}, your current balance(INR) in account is : {self.balance}', font=('arial italic',15)).place(x=60, y=115)
        Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)

    def gui_deposit(self):
        top = Toplevel()
        top.geometry('800x500')      
        top.title("AMOUNT DEPOSIT WINDOW")
        Label(top, text="Bank of World", font=('arial bold',30), bg='sky blue').pack()
        Label(top, text='Deposit Amount -', font=('arial italic',15)).place(x=210, y=115)
        Entry(top, width=20,textvariable = amount_var).place(x=(150+240), y=120)  
        Submit = Button(top, text='Submit', font=('arial Bold',15), bg='sky blue',fg='black',command = self.deposit_submit_amnt).place(x=280, y=300)
        Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=400, y=300)

    def deposit_submit_amnt(self):
      # fetching the user input using get() (a built_in function) to their respective variables
        amount = amount_var.get()

        top = Toplevel()
        top.geometry('800x500')      
        top.title("DEPOSIT WINDOW")
        Label(top, text="Thanks for choosing Bank of World", font=('arial bold',30), bg='sky blue').pack()
        # INVOKING THE AMOUNT DEPOSIT FUNCTION
        self.amount_deposit(amount)
        Label(top, text= f'{amount} INR is successfully deposited in your Bank of World Account.' , font=('arial italic',15)).place(x=60, y=115)
        Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)


    def gui_withdraw(self):
        top = Toplevel()
        top.geometry('800x500')      
        top.title(" AMOUNT WITHDRAW WINDOW")
        Label(top, text="Bank of World", font=('arial bold',30), bg='sky blue').pack()
        Label(top, text='Withdraw Amount -', font=('arial italic',15)).place(x=210, y=115)
        Entry(top, width=20,textvariable = amount_var).place(x=(150+250), y=120)  
        Submit = Button(top, text='Submit', font=('arial Bold',15), bg='sky blue',fg='black',command = self.withdraw_submit_amnt).place(x=280, y=300)
        Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=400, y=300)

    def withdraw_submit_amnt(self):
       # fetching the user input using get() (a built_in function) to their respective variables
        amount = amount_var.get()

        top = Toplevel()
        top.geometry('800x500')      
        top.title(" WITHDRAW WINDOW")
        Label(top, text="Thanks for choosing Bank of World", font=('arial bold',30), bg='sky blue').pack()
        if amount <= self.balance:
          # INVOKING THE WITHDRAW FUNCTION
          self.withdraw(amount)
          Label(top, text= f'{amount} INR is successfully withdrawn from your Bank of World Account.' , font=('arial italic',15)).place(x=60, y=115)
          Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300) 

        elif amount > self.balance:
          # INVOKING THE WITHDRAW FUNCTION
          self.withdraw(amount)
          Label(top, text= 'Sorry, cannot withdraw more money !.' , font=('arial italic',15)).place(x=40, y=115)
          Label(top, text= 'Your withdraw amount exceeds your remaining balance amount.' , font=('arial italic',15)).place(x=40, y=145)
          Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300) 
         

    def gui_loan_menu(self):
       # fetching the user input using get() (a built_in function) to their respective variables
        loan_type = loan_radio_var.get()

        if loan_type == 1:
          top = Toplevel()
          top.geometry('800x500')      
          top.title(" STUDENT LOAN WINDOW")
          Label(top, text="Bank of World", font=('arial bold',30), bg='sky blue').pack()
          Label(top, text='CGPA -', font=('arial italic',15)).place(x=240, y=150)   # no need to use pack as we using grig funtion
          Entry(top, width=20,textvariable=cgpa_var).place(x=(150+240), y=155)

          Label(top, text='Loan Amount -', font=('arial italic',15)).place(x=240, y=185)
          Entry(top, width=20,textvariable=amount_var).place(x=(150+240), y=190)          

          Submit = Button(top, text='Submit', font=('arial Bold',15), bg='sky blue',fg='black',command = self.student_Loan_status).place(x=280, y=300)
          Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=400, y=300)

        if loan_type == 2:
          top = Toplevel()
          top.geometry('800x500')      
          top.title(" CAR LOAN WINDOW")
          Label(top, text="Bank of World", font=('arial bold',30), bg='sky blue').pack()
          Label(top, text='Annual income -', font=('arial italic',15)).place(x=250, y=150)   # no need to use pack as we using grig funtion
          Entry(top, width=20,textvariable=annunal_income_var).place(x=(150+270), y=155)

          Label(top, text='Loan Amount -', font=('arial italic',15)).place(x=250, y=185)
          Entry(top, width=20,textvariable=amount_var).place(x=(150+270), y=190)    
                

          Submit = Button(top, text='Submit', font=('arial Bold',15), bg='sky blue',fg='black',command = self.car_Loan_status).place(x=280, y=300)
          Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=400, y=300)

        if loan_type == 3:
          top = Toplevel()
          top.geometry('800x500')      
          top.title(" HOME LOAN WINDOW")
          Label(top, text="Bank of World", font=('arial bold',30), bg='sky blue').pack()
          Label(top, text='loan Tenure (Years) -', font=('arial italic',15)).place(x=160, y=150)   # no need to use pack as we using grig funtion
          Entry(top, width=20,textvariable = loan_tenure_var).place(x=(150+250), y=155)

          Label(top, text='Annual income -', font=('arial italic',15)).place(x=160, y=185)
          Entry(top, width=20,textvariable=annunal_income_var).place(x=(150+250), y=190)  

          Label(top, text='Other Precceding EMI -', font=('arial italic',15)).place(x=160, y=220)
          Entry(top, width=20,textvariable=other_emi_proceeding_var).place(x=(150+250), y=225)  

          Label(top, text='Loan Amount -', font=('arial italic',15)).place(x=160, y=255)
          Entry(top, width=20,textvariable=amount_var).place(x=(150+250), y=260)

          Submit = Button(top, text='Submit', font=('arial Bold',15), bg='sky blue',fg='black',command = self.home_Loan_status).place(x=280, y=300)
          Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=400, y=300)

    def student_Loan_status(self):
       # fetching the user input using get() (a built_in function) to their respective variables

        amount = amount_var.get()
        cgpa = cgpa_var.get()
      
        top = Toplevel()
        top.geometry('800x500')      
        top.title(" APPROVED STUDENT LOAN WINDOW")
        Label(top, text="Thanks for chossing Bank of World", font=('arial bold',30), bg='sky blue').pack()
        # INVOKING THE STUDENT LOAN FUNCTION
        self.student_Loan(cgpa, amount)

        if 6 <= cgpa <7:
          Label(top, text=f"You will get 50% of our loan amount : {amount}", font=('arial italic',15)).place(x=70, y=150)
          Label(top, text="So, you will get the loan of Rs", font=('arial italic',15)).place(x=70, y=185)
          Label(top, text=amount*0.5, font=('arial italic',15)).place(x=350, y=185)
          Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)
          
        elif(7<= cgpa<8):
           Label(top, text=f"You will get 75% of our loan amount : {amount}", font=('arial italic',15)).place(x=70, y=150)
           Label(top, text="So, you will get the loan of Rs", font=('arial italic',15)).place(x=70, y=185)
           Label(top, text=amount*0.75, font=('arial italic',15)).place(x=350, y=185)
           Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)

        elif(8 <=cgpa<9):
           Label(top, text=f"You will get 90% of our loan amount : {amount}", font=('arial italic',15)).place(x=70, y=150)
           Label(top, text="So, you will get the loan of Rs", font=('arial italic',15)).place(x=70, y=185)
           Label(top, text=amount*0.9, font=('arial italic',15)).place(x=350, y=185)
           Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)
          
        elif(9 <=cgpa <= 10):
           Label(top, text=f"You will get 100% of our loan amount : {amount}", font=('arial italic',15)).place(x=70, y=150)
           Label(top, text="So, you will get the loan of Rs", font=('arial italic',15)).place(x=70, y=185)
           Label(top, text=amount, font=('arial italic',15)).place(x=350, y=185)
           Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)

        else:
          Label(top, text="Sorry, you are not eligible to get the loan since your CGPA is less.", font=('arial italic',15)).place(x=70, y=150)
          Label(top, text="Thank you for applying for loan to/with Bank of World", font=('arial italic',15)).place(x=70, y=185)
          Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)

          
    def car_Loan_status(self):
       # fetching the user input using get() (a built_in function) to their respective variables
        amount = amount_var.get()
        annual_income = annunal_income_var.get()

        top = Toplevel()
        top.geometry('800x500')      
        top.title(" APPROVED CAR LOAN WINDOW")
        Label(top, text="Thanks for choosing Bank of World", font=('arial bold',30), bg='sky blue').pack()
       # INVOKING THE CAR LOAN FUNCTION
        self.car_Loan(amount, annual_income)

        if self.age >= 21:
          if annual_income >=300000:
            loan_amount_eligible = amount*0.6   #loan*60%     
            Label(top, text=f" Congragulations, you are eligible for the loan amount of RS {loan_amount_eligible}", font=('arial italic',15)).place(x=40, y=150)
            Label(top, text=" i.e 60% of your loan_amount.", font=('arial italic',15)).place(x=40, y=185)
            Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)     
           
          else:
            Label(top, text=" Sorry, you are not eligible to get the loan since your minimum annual income is", font=('arial italic',15)).place(x=40, y=150)
            Label(top, text=" not more than our expected income i.e RS 300000 LPA ", font=('arial italic',15)).place(x=40, y=185)
            Label(top, text=" Thank you for applying for loan to/with Bank of World", font=('arial italic',15)).place(x=40, y=250)
            Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)

        else:
          Label(top, text="Sorry, you are not eligible to get the loan since your age is less than 21 years", font=('arial italic',15)).place(x=70, y=150)
          Label(top, text="Thank you for applying for loan to/with Bank of World", font=('arial italic',15)).place(x=70, y=185)
          Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)
        
    def home_Loan_status(self):
       # fetching the user input using get() (a built_in function) to their respective variables
        loan_amount = amount_var.get()
        loan_tenure = loan_tenure_var.get()
        annunal_income = annunal_income_var.get()
        other_emi_proceeding = other_emi_proceeding_var.get()

        top = Toplevel()
        top.geometry('800x500')      
        top.title(" APPROVED HOME LOAN WINDOW")
        Label(top, text="Thanks for chossing Bank of World", font=('arial bold',30), bg='sky blue').pack()
        # INVOKING THE HOME LOAN FUNCTION
        self.home_loan(loan_amount, annunal_income, other_emi_proceeding, loan_tenure)

        if self.age >= 21:
                          # loan_amount = montly income*(50%) - other_emi_proceeding / lPA 

          if loan_tenure <= 5:  #upto 5 years
            loan_amount_eligible=((annunal_income*0.5)-other_emi_proceeding)/2150
            Label(top, text=f"Congragulations, you are eligible for the loan amount of RS {loan_amount_eligible}", font=('arial italic',15)).place(x=40, y=150)
            Label(top, text=" lakh only with an interest of 10.5% & an EMI of RS 2150. ", font=('arial italic',15)).place(x=40, y=185)
            Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)
            
    
          elif (loan_tenure>5 and loan_tenure<=10):
            loan_amount_eligible=((annunal_income*0.5)-other_emi_proceeding)/1350
            Label(top, text=f"Congragulations, you are eligible for the loan amount of RS {loan_amount_eligible}", font=('arial italic',15)).place(x=40, y=150)
            Label(top, text=" lakh only with an interest of 10.5% & an EMI of RS 1350. ", font=('arial italic',15)).place(x=40, y=185)
            Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)
            
          elif (loan_tenure>10 and loan_tenure<=15):
            loan_amount_eligible=((annunal_income*0.5)-other_emi_proceeding)/1100
            Label(top, text=f"Congragulations, you are eligible for the loan amount of RS {loan_amount_eligible}", font=('arial italic',15)).place(x=40, y=150)
            Label(top, text=" lakh only with an interest of 10.5% & an EMI of RS 1100. ", font=('arial italic',15)).place(x=40, y=185)
            Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)
            
          elif (loan_tenure>15 and loan_tenure<=20):
            loan_amount_eligible=((annunal_income*0.5)-other_emi_proceeding)/1000
            Label(top, text=f"Congragulations, you are eligible for the loan amount of RS {loan_amount_eligible}", font=('arial italic',15)).place(x=40, y=150)
            Label(top, text=" lakh only with an interest of 10.5% & an EMI of RS 1000. ", font=('arial italic',15)).place(x=40, y=185)
            Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)
           
          elif (loan_tenure>20 and loan_tenure<=25):
            loan_amount_eligible=((annunal_income*0.5)-other_emi_proceeding)/945
            Label(top, text=f"Congragulations, you are eligible for the loan amount of RS {loan_amount_eligible}", font=('arial italic',15)).place(x=40, y=150)
            Label(top, text=" lakh only with an interest of 10.5% & an EMI of RS 945. ", font=('arial italic',15)).place(x=40, y=185)
            Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)
            
          else:
            loan_amount_eligible=((annunal_income*0.5)-other_emi_proceeding)/915
            Label(top, text=f"Congragulations, you are eligible for the loan amount of RS {loan_amount_eligible}", font=('arial italic',15)).place(x=40, y=150)
            Label(top, text=" lakh only with an interest of 10.5% & an EMI of RS 915. ", font=('arial italic',15)).place(x=40, y=185)
            Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)

        else:
          Label(top, text="Sorry, you are not eligible to get the loan since your age is less than 21 years ", font=('arial italic',15)).place(x=40, y=150)
          Label(top, text="Thank you for applying loan to/with  of World", font=('arial italic',15)).place(x=40, y=185)
          Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=350, y=300)
          

#---------------------------------------------------------------OUTER GUI----------------------------------------------------------------------------------
# Tk() help to create a default GUI window
win = Tk()
# Global declared variables with assigning StringVar(), IntVar() from tkinter library
# StringVar() - It's used so that you can easily monitor changes to tkinter variables if they occur through the code
#               Holds a string; the default value is an empty string 

# IntVar() - # Holds an integer; the default value is 0
# Login window
username_var = StringVar()
password_var = StringVar()

# For Signup window
name_var = StringVar()
age_var = IntVar()
gender_var = StringVar()
Set_password_var = StringVar()

# for loantype and annual income
loan_radio_var =IntVar()
radio_var = IntVar()
amount_var = IntVar()
annunal_income_var = IntVar()
cgpa_var = IntVar()

annunal_income_var = IntVar()
other_emi_proceeding_var = IntVar()
loan_tenure_var = IntVar()



# MAIN WINDOW FOR ACCEPTING INPUT
def Login_window():
    win.geometry('800x500')      # L X B
    win.title('LOGIN WINDOW')
    Label(win, text="Welcome to Bank of World", font=('arial bold',35), bg='sky blue').pack()
    #  of World logo
    logo1 = ImageTk.PhotoImage(Image.open('bank.jpg'))
    label1 = Label(image=logo1)
    label1.image = logo1

    # Position of image 1
    label1.place(x=40,y=0)

    logo2 = ImageTk.PhotoImage(Image.open('bank.jpg'))
    label2 = Label(image=logo2)
    label2.image = logo2
     # Position of image 2
    label2.place(x=700,y=0)  

    Label(win, text=" \" A  of World is place that will lend you money,", font=('arial italic',17)).place(x=20, y=90)
    Label(win, text=" if you can prove that you don't need it \".", font=('arial italic',17)).place(x=300, y=130)
    Label(win, text='Username - ', font=('arial bold',15)).place(x=240, y=200)   # no need to use pack as we using grig funtion
    Entry(win, width=20,textvariable=username_var).place(x=(170+220), y=205)

    Label(win, text='Password - ', font=('arial Bold',15)).place(x=240, y=240)
    Entry(win, show = '*', width=20,textvariable=password_var).place(x=(170+220), y=250)  

    

    Submit = Button(win, text='login', font=('arial Bold',15), bg='sky blue',fg='black',command = check_login).place(x=200, y=350)
    Exit = Button(win, text='Signup', font=('arial Bold',15), bg='sky blue',fg='black',command= Signup_window).place(x=340, y=350)
    Exit = Button(win, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= win.destroy).place(x=500, y=350)
    win.mainloop()

def check_login():
    # for storing database list 
    temp_list = []
    if username_var.get() == "" or password_var.get() == "" :
      messagebox.showerror("Error","All fields are required")


    else:
      mydb = sql_db.connect(host='localhost',
                            user='root',
                            password='admin',
                            database = 'bank_management')

      # using cursor function creating cursor object so we can execute all queries / Operations
      cur = mydb.cursor()

      # Query / Operatations
      Check = f"SELECT * from user_data WHERE username = '{username_var.get()}' AND password = '{password_var.get()}'"

      cur.execute(Check)
      # creating a database call BANK_MANAGEMENT with the help of execute function 
     
      rows = cur.fetchall()
      # To check what cur return from
      # print(rows)
      #
      if rows == []:
        messagebox.showerror("Error","Incorrect username or password")
      # return you a string from list of tuples from the database
      else:
        for i in range(0,4):
          res = [lis[i] for lis in rows]
          temp_list.append(res[0])
          # for internal checking
          print('\n',temp_list[i])

      Check_login = f"SELECT * from passbook"

      cur.execute(Check_login)
      # creating a database call BANK_MANAGEMENT with the help of execute function 
     
      rows = cur.fetchall()
      if rows == []:
        Insert_into_passbook = f"INSERT INTO passbook (Username) VALUES('{username_var.get()}')"

        cur.execute(Insert_into_passbook)
        # creating a database call BANK_MANAGEMENT with the help of execute function 
        mydb.commit() 

        mydb.close()

      # Creating a object after checking database from login page
      obj_GUI = GUI(temp_list[0], temp_list[1], temp_list[2], temp_list[3]) 
      obj_GUI.menu()



      # To close connection with database.
      mydb.close() 



def Signup_window():
    top = Toplevel()
    top.geometry('800x500')      # L X B
    top.title('SIGN UP WINDOW')
    Label(top, text="Welcome to Bank of World", font=('arial bold',35), bg='sky blue').pack()
    #  of World logo
    logo1 = ImageTk.PhotoImage(Image.open('bank.jpg'))
    label1 = Label(image=logo1)
    label1.image = logo1

    # Position of image 1
    label1.place(x=40,y=0)

    logo2 = ImageTk.PhotoImage(Image.open('bank.jpg'))
    label2 = Label(image=logo2)
    label2.image = logo2

    # Position of image 2
    label2.place(x=700,y=0)  

    Label(top, text=" \" A  of World is place that will lend you money,", font=('arial italic',17)).place(x=20, y=90)
    Label(top, text=" if you can prove that you don't need it \".", font=('arial italic',17)).place(x=300, y=130)
    Label(top, text='Username - ', font=('arial bold',15)).place(x=240, y=200)   # no need to use pack as we using grig funtion
    Entry(top, width=20,textvariable=name_var).place(x=(170+220), y=205)

    Label(top, text='Age - ', font=('arial Bold',15)).place(x=240, y=240)
    Entry(top, width=20,textvariable=age_var).place(x=(170+220), y=250)  

    Label(top, text='Gender -', font=('arial Bold',15)).place(x=240, y=285)
    Entry(top, width=20,textvariable= gender_var).place(x=(170+220), y=290)

    Label(top, text ='Set password -',font=('arial Bold',15)).place(x=240, y=325)
    Entry(top,width=20,textvariable= Set_password_var).place(x=(170+220), y=330)

    Submit = Button(top, text='Submit', font=('arial Bold',15), bg='sky blue',fg='black',command = user_input).place(x=280, y=400)
    Exit = Button(top, text='Exit', font=('arial Bold',15), bg='sky blue',fg='black',command= top.destroy).place(x=400, y=400)
    top.mainloop()
  

# CREATING A FUNCTION FOR CREATING AN OBJECT OF CLASS GUI AND CONNECTION FOR DATABASE
def user_input():
    if name_var.get()=="" or age_var.get()==0 or gender_var.get()=="" or Set_password_var.get()=='' :
      messagebox.showerror("Error","All fields are required")
    else :
      name = name_var.get()
      age = age_var.get()
      gender = gender_var.get().lower()
      password = Set_password_var.get()

     # print(name,age,gender,password)
      # using connect function to establish connection to database at any host
      mydb = sql_db.connect(host='localhost',
                            user='root',
                            password='admin',
                            database = 'bank_management')

      # using cursor function creating cursor object so we can execute all queries / Operations
      cur = mydb.cursor()

      # Query / Operatations
      Insert_into_user_data = f"INSERT INTO user_data VALUES('{name}', {age}, '{gender}','{password}')"
      Insert_into_passbook = f"INSERT INTO passbook (Username) VALUES('{name}')"

      # creating a database call BANK_MANAGEMENT with the help of execute function
      cur.execute(Insert_into_user_data)

      
      # commit() function help to reflect changes in database bank_management 
      mydb.commit()    

       # creating a database call BANK_MANAGEMENT with the help of execute function
      cur.execute(Insert_into_passbook)

      
      # commit() function help to reflect changes in database bank_management 
      mydb.commit() 

      # To close connection with database.
      mydb.close()  

     # Creating object of class GUI as well as invoking its constructor.
      obj_GUI = GUI(name, age, gender,password) 
      obj_GUI.menu()
    

# INVOKING THE login_window (ROOT WINDOW) FUNCTION

Login_window()