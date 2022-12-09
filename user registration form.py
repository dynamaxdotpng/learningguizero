from hashlib import pbkdf2_hmac
import sqlite3
from guizero import *

Connect2DB = sqlite3.connect("user_registration.db")
Cursor4DB = Connect2DB.cursor()
NewWindowApp = App(title='User Registration Form')

def Insert_Records_Into_DB():
    TextBoxForFirstNameValue = TextBoxForFirstName.value
    TextBoxForLastNameValue = TextBoxForLastName.value
    TextBoxForEmailValue = TextBoxForEmail.value
    TextBoxForCreditCardValue = int(TextBoxForCreditCard.value)
    our_app_iters = 500_000
    salt_for_has = bytes(str(TextBoxForEmailValue),'utf-8')
    password_for_hash = bytes(str(TextBoxForPassword.value),'utf-8')
    derived_key = pbkdf2_hmac('sha256',password_for_hash)
    TextBoxForPasswordValue = TextBoxForPassword.value
    Data_Object_For_Insertion = (TextBoxForFirstNameValue,TextBoxForLastNameValue,TextBoxForEmailValue,TextBoxForCreditCardValue,TextBoxForPasswordValue)
    Insertion_Command = "INSERT INTO users VALUES(?,?,?,?,?)"
    Cursor4DB.execute(Insertion_Command,Data_Object_For_Insertion)
    Connect2DB.commit()

def see_records_from_DB():
    Cursor4DB.execute("SELECT * FROM user")
    print(Cursor4DB.fetchall())

TextBoxForFirstName = TextBox(NewWindowApp,width=50)
TextBoxForFirstName.value = 'First Name'
TextBoxForLastName = TextBox(NewWindowApp,width=50)
TextBoxForLastName.value = 'Surname'
TextBoxForEmail = Text(NewWindowApp,width=50)
TextBoxForEmail.value = 'Email'
TextBoxForCreditCard = TextBox(NewWindowApp,width=50)
TextBoxForCreditCard.value = 'Credit Card Number'
TextBoxForPassword = Text(NewWindowApp,width=50)
TextBoxForPassword.value = 'Password'

RegistrationFormButton = PushButton(NewWindowApp,text='Add to \nthe database',command=Insert_Records_Into_DB)
CheckDBButton = PushButton(NewWindowApp,text='Check database\ncontents',command=see_records_from_DB)

NewWindowApp.display()
Connect2DB.close()