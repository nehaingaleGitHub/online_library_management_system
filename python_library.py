from flask import Flask, render_template,request
import mysql.connector
app = Flask(__name__)

mydb=mysql.connector.connect(host="localhost",user="root",password='',database='lms_project')
mycursor=mydb.cursor()
#-----------------For opening First page of Website----------------
@app.route("/")
def template_test():
        return render_template('library_start.html')

#-------------For Opening ******Students Home Page------------------
@app.route("/stud_home")
def stud_home():
        data=[["neha@gmail.com","neha","ingale","pass"],
          ["abx@gmail.com","abc","ap","pass"]]
        print(data)
        return render_template('stud_home.html',da=data)
#----------for opening Registration Form------------------------
@app.route("/stud_registration")
def stud_registration():
        return render_template('stud_Registration.html')
#-----------------------For insert Record------------------------
@app.route("/read",methods = ['POST', 'GET'])
def read():
    if request.method == 'POST':
        r = request.form
        print(r)
        f=r['first_name']
        l=r['last_name']
        e=r['email']
        p=r['password']
        sqlQ = "INSERT INTO login_regis(`first_name`, `last_name`,`email`,`password`) VALUES (%s,%s,%s,%s)"
        value=(f,l,e,p)
        mycursor.execute(sqlQ, value)
        mydb.commit()
        print("Data inserted..")
        sql2="SELECT * FROM login_regis"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(myresult)
    return render_template('stud_login.html',da=myresult)
#    return render_template('table.html',da=myresult)
#-------------------For delete Record-------------------------------
@app.route("/deldata")
def deldata():
    w=request.args.get('fn')
    print(w)
    sql="DELETE FROM login_regis WHERE first_name='"+w+"'"
    mycursor.execute(sql)
    print(sql)
    mydb.commit()
    print("Data Deleted..")
    sql2="SELECT * FROM login_regis"
    print(sql2)
    mycursor.execute(sql2)
    myresult=mycursor.fetchall()
    #print(myresult)
    return render_template('table.html',da=myresult)
#========================= FOR UPDATE RECORD ===========================
@app.route("/updata")
def updata():
    w=request.args.get('fn')
    updt_fname=w;
    print("value show")
    sql2="SELECT * FROM login_regis WHERE first_name='"+w+"'"
    mycursor.execute(sql2)
    myresult=mycursor.fetchall()
    #print(myresult)
    return render_template('update_record.html',da=myresult,fn=w)
#---------------------- For update record--------------------------
@app.route("/updata2",methods = ['POST', 'GET'])
def updata2():
    if request.method == 'POST':
        r = request.form
        fn=r['first_name1']
        print(fn," = value of r")
        f=r['first_name']
        l=r['last_name']
        e=r['email']
        p=r['password']
        sqlQ = "UPDATE login_regis SET first_name=%s,last_name=%s,email=%s,password=%s WHERE first_name='"+fn+"' "
        print(sqlQ," = value of sqlQ")
        value=(f,l,e,p)
        mycursor.execute(sqlQ, value)
        mydb.commit()
        print("Data updated..")
        sql2="SELECT * FROM login_regis"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(myresult)
    return render_template('table.html',da=myresult)
#-------------------- students record show---------------------------
@app.route("/record")
def record():
        sql2="SELECT * FROM login_regis"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(myresult)
        return render_template('table.html',da=myresult)
#---------------------Open login page----------------------------------
@app.route("/stud_login")
def stud_login():
        return render_template('stud_login.html')
#----------------- login password check---------------------------------
@app.route("/login_check",methods = ['POST', 'GET'])
def login_check():
    if request.method == 'POST':
        r = request.form
        fn=r['email']
        pas=r['password']
        sql2="SELECT * FROM `login_regis` WHERE email='"+fn+"' AND password='"+pas+"' "
        print(sql2,"for login_check value")
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(len(myresult))
        if(len(myresult)>0):
            return render_template('stud_dashboard.html')
        else:
            he="Invalid Username OR Password"
            return render_template('stud_login.html',he=he)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Admin registration and login pages^^^^^^^^^^^^^
#-----------------------For insert Record------------------------
@app.route("/read2",methods = ['POST', 'GET'])
def read2():
    if request.method == 'POST':
        r = request.form
        print(r)
        f=r['first_name']
        l=r['last_name']
        e=r['email']
        p=r['password']
        sqlQ = "INSERT INTO admin(`first_name`, `last_name`,`email`,`password`) VALUES (%s,%s,%s,%s)"
        value=(f,l,e,p)
        mycursor.execute(sqlQ, value)
        mydb.commit()
        print("Data inserted..")
        sql2="SELECT * FROM admin"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(myresult)
    return render_template('admin_login.html',da=myresult)
@app.route("/adminlogin_check1",methods = ['POST', 'GET'])
def adminlogin_check1():
    if request.method == 'POST':
        r = request.form
        fn=r['email']
        pas=r['password']
        sql2="SELECT * FROM `admin` WHERE email='"+fn+"' AND password='"+pas+"' "
        print(sql2,"for admin value")
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(len(myresult))
        if(len(myresult)>0):
            return render_template('admin_dashboard.html')
        else:
            he="Invalid Username OR Password"
            return render_template('admin_login.html',he=he)

#======open ***student dashboard******==================
@app.route("/stud_dashboard")
def stud_dashboard():
        return render_template('stud_dashboard.html')
#======only show admin added book in student Record======
@app.route("/stud_search")
def stud_search():
        sql2="SELECT * FROM search_book"
        print(sql2,"value of sql2..............")
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(myresult)
        return render_template('stud_search.html',da=myresult)

#========Open issued book(Add page,table,Update HTML PAGES:)============================
@app.route("/stud_issuedbook")
def stud_issuedbook():
        return render_template('stud_issuedbook.html')

@app.route("/table_studissued")
def table_studissued():
        sql2="SELECT * FROM stud_issuedbook"
        print(sql2,"value of sql2..............")
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(myresult)
        return render_template('table_studissued.html',da=myresult)

@app.route("/table_studreturn")
def table_studreturn():
        sql2="SELECT * FROM returnbook"
        print(sql2,"value of sql2..............")
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(myresult)
        return render_template('table_studreturn.html',da=myresult)
        
#============student Add book (insert, update, delete)===============
@app.route("/insert_issuedbook",methods = ['POST', 'GET'])
def insert_issuedbook():
        if request.method == 'POST':
                r = request.form
                print(r)
                name=r['full_name']
                ad_id=r['book_ID']
                ad_bn=r['book_name']
                ad_an=r['author_name']
                ad_q=r['qty']
                sqlQ = "INSERT INTO stud_issuedbook(`full_name`,`book_ID`, `book_name`,`author_name`,`qty`) VALUES (%s,%s,%s,%s,%s)"
                value=(name,ad_id,ad_bn,ad_an,ad_q)
                mycursor.execute(sqlQ, value)
                mydb.commit()
                print("Data inserted..")
                sql2="SELECT * FROM stud_issuedbook"
                mycursor.execute(sql2)
                myresult=mycursor.fetchall()
                print(myresult)
        return render_template('table_studissued.html',da=myresult)
@app.route("/issuedbook_deldata")
def issuedbook_deldata():
    w=request.args.get('fn')
    print(w)
    sql="DELETE FROM stud_issuedbook WHERE book_ID='"+w+"'"
    mycursor.execute(sql)
    print(sql)
    mydb.commit()
    print("Data Deleted..")
    sql2="SELECT * FROM stud_issuedbook"
    print(sql2)
    mycursor.execute(sql2)
    myresult=mycursor.fetchall()
    #print(myresult)
    return render_template('table_studissued.html',da=myresult)

@app.route("/issued_updata")
def issued_updata():
    w=request.args.get('fn')
    updt_fname=w;
    print("value show")
    sql2="SELECT * FROM stud_issuedbook WHERE book_ID='"+w+"'"
    mycursor.execute(sql2)
    myresult=mycursor.fetchall()
    #print(myresult)
    return render_template('update_issuedbook.html',da=myresult,fn=w)

@app.route("/Issued_updata2",methods = ['POST', 'GET'])
def Issued_updata2():
    if request.method == 'POST':
        r = request.form
        fn=r['book_ID1']
        print(fn," = value of r")
        name=r['full_name']
        f=r['book_ID']
        l=r['book_name']
        e=r['author_name']
        p=r['qty']
        sqlQ = "UPDATE stud_issuedbook SET full_name=%s,book_ID=%s,book_name=%s,author_name=%s,qty=%s WHERE book_ID='"+fn+"' "
        print(sqlQ," = value of sqlQ")
        value=(name,f,l,e,p)
        mycursor.execute(sqlQ, value)
        mydb.commit()
        print("Data updated..")
        sql2="SELECT * FROM stud_issuedbook"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(myresult)
    return render_template('table_studissued.html',da=myresult)
#******************Return Book Details*************************************
#========Open Student Add **Return book** page============================
@app.route("/stud_returnbookform")
def stud_returnbookform():
        return render_template('stud_returnbookform.html')
#============student return book (insert, update, delete)===============
@app.route("/insert_returnbook",methods = ['POST', 'GET'])
def insert_returnbook():
        if request.method == 'POST':
                r = request.form
                print(r)
                name=r['full_name']
                ad_id=r['book_ID']
                ad_bn=r['book_name']
                ad_an=r['author_name']
                issued=r['issued_date']
                ret=r['return_date']
                sqlQ = "INSERT INTO returnbook(`full_name`,`book_ID`, `book_name`,`author_name`,`issued_date`,`return_date`) VALUES (%s,%s,%s,%s,%s,%s)"
                value=(name,ad_id,ad_bn,ad_an,issued,ret)
                mycursor.execute(sqlQ, value)
                mydb.commit()
                print("Data inserted..")
                sql2="SELECT * FROM returnbook"
                mycursor.execute(sql2)
                myresult=mycursor.fetchall()
                print(myresult)
        return render_template('table_studreturn.html',da=myresult)
@app.route("/return_deldata")
def return_deldata():
    w=request.args.get('fn')
    print(w)
    sql="DELETE FROM returnbook WHERE book_ID='"+w+"'"
    mycursor.execute(sql)
    print(sql)
    mydb.commit()
    print("Data Deleted..")
    sql2="SELECT * FROM returnbook"
    print(sql2)
    mycursor.execute(sql2)
    myresult=mycursor.fetchall()
    #print(myresult)
    return render_template('table_studreturn.html',da=myresult)

@app.route("/return_updata")
def return_updata():
    w=request.args.get('fn')
    updt_book_ID=w;
    print("value show")
    sql2="SELECT * FROM returnbook WHERE book_ID='"+w+"'"
    mycursor.execute(sql2)
    myresult=mycursor.fetchall()
    #print(myresult)
    return render_template('update_return.html',da=myresult,fn=w)

@app.route("/return_updata2",methods = ['POST', 'GET'])
def return_updata2():
    if request.method == 'POST':
        r = request.form
        fn=r['book_ID1']
        print(fn," = value of r")
        name=r['full_name']
        f=r['book_ID']
        l=r['book_name']
        e=r['author_name']
        issued=r['issued_date']
        ret=r['return_date']
        sqlQ = "UPDATE returnbook SET full_name=%s,book_ID=%s,book_name=%s,author_name=%s,issued_date=%s,return_date=%s WHERE book_ID='"+fn+"' "
        print(sqlQ," = value of sqlQ")
        value=(name,f,l,e,issued,ret)
        mycursor.execute(sqlQ, value)
        mydb.commit()
        print("Data updated..")
        sql2="SELECT * FROM returnbook"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(myresult)
    return render_template('table_studreturn.html',da=myresult)
#========Open Student Add **stud_requestbookform book** page============================
@app.route("/stud_requestbookform")
def stud_requestbookform():
        return render_template('stud_requestbookform.html')
#============student stud_request book book (insert, update, delete)===============
@app.route("/insert_requestbook",methods = ['POST', 'GET'])
def insert_requestbook():
        if request.method == 'POST':
                r = request.form
                print(r)
                name=r['full_name']
                ad_bn=r['book_name']
                ad_an=r['author_name']
                sqlQ = "INSERT INTO requestbook(`full_name`,`book_name`,`author_name`) VALUES (%s,%s,%s)"
                value=(name,ad_bn,ad_an)
                mycursor.execute(sqlQ, value)
                mydb.commit()
                print("Data inserted..")
                sql2="SELECT * FROM requestbook"
                mycursor.execute(sql2)
                myresult=mycursor.fetchall()
                print(myresult)
        return render_template('table_studrequest.html',da=myresult)
@app.route("/request_deldata")
def request_deldata():
    w=request.args.get('fn')
    print(w)
    sql="DELETE FROM requestbook WHERE book_name='"+w+"'"
    mycursor.execute(sql)
    print(sql)
    mydb.commit()
    print("Data Deleted..")
    sql2="SELECT * FROM requestbook"
    print(sql2)
    mycursor.execute(sql2)
    myresult=mycursor.fetchall()
    #print(myresult)
    return render_template('table_studrequest.html',da=myresult)

@app.route("/request_updata")
def request_updata():
    w=request.args.get('fn')
    updt_book_ID=w;
    print("value show")
    sql2="SELECT * FROM requestbook WHERE book_name='"+w+"'"
    mycursor.execute(sql2)
    myresult=mycursor.fetchall()
    #print(myresult)
    return render_template('update_requestbook.html',da=myresult,fn=w)

@app.route("/request_update2",methods = ['POST', 'GET'])
def request_update2():
    if request.method == 'POST':
        r = request.form
        fn=r['book_name1']
        name=r['full_name']
        l=r['book_name']
        e=r['author_name']
        sqlQ = "UPDATE requestbook SET full_name=%s,book_name=%s,author_name=%s WHERE book_name='"+fn+"' "
        print(sqlQ," = value of sqlQ")
        value=(name,l,e)
        mycursor.execute(sqlQ, value)
        mydb.commit()
        print("Data updated..")
        sql2="SELECT * FROM requestbook"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(myresult)
    return render_template('table_studrequest.html',da=myresult)

@app.route("/table_studrequest")
def table_studrequest():
        sql2="SELECT * FROM requestbook"
        print(sql2,"value of sql2..............")
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(myresult)
        return render_template('table_studrequest.html',da=myresult)

#**************************************************************************
#========================= Admin Pages Coding==============================
#**************************************************************************

@app.route("/admin_home")
def admin_home():
        return render_template('admin_home.html')

@app.route("/admin_addbook")
def admin_addbook():
        return render_template('admin_addbook.html')

#============Admin add book(update Delete and Insert)=============
@app.route("/insert_book",methods = ['POST', 'GET'])
def insert_book():
        if request.method == 'POST':
                r = request.form
                print(r)
                ad_sr=r['sr_no']
                ad_id=r['book_ID']
                ad_bn=r['book_name']
                ad_an=r['author_name']
                ad_q=r['qty']
                sqlQ = "INSERT INTO search_book(`sr_no`,`book_ID`, `book_name`,`author_name`,`qty`) VALUES (%s,%s,%s,%s,%s)"
                value=(ad_sr,ad_id,ad_bn,ad_an,ad_q)
                mycursor.execute(sqlQ, value)
                mydb.commit()
                print("Data inserted..")
                sql2="SELECT * FROM search_book"
                mycursor.execute(sql2)
                myresult=mycursor.fetchall()
                print(myresult)
        return render_template('table2.html',da=myresult)

@app.route("/delete_data")
def delete_data():
    w=request.args.get('fn')
    print(w)
    sql="DELETE FROM search_book WHERE sr_no='"+w+"'"
    mycursor.execute(sql)
    print(sql)
    mydb.commit()
    print("Data Deleted..")
    sql2="SELECT * FROM search_book"
    print(sql2)
    mycursor.execute(sql2)
    myresult=mycursor.fetchall()
    #print(myresult)
    return render_template('table2.html',da=myresult)

#========================= FOR UPDATE RECORD ===========================
@app.route("/admin_updata")
def admin_updata():
    w=request.args.get('fn')
    updt_book_ID=w;
    print("Data update..")
    sql2="SELECT * FROM search_book WHERE sr_no='"+w+"'"
    mycursor.execute(sql2)
    myresult=mycursor.fetchall()
    #print(myresult)
    return render_template('admin_update.html',da=myresult,fn=w)
#---------------------- For update record--------------------------
@app.route("/admin_updata2",methods = ['POST', 'GET'])
def admin_updata2():
        if request.method == 'POST':
                r = request.form
                fn=r['sr_no1']
                print(fn," = value of r")
                ad_sr=r['sr_no']
                ad_id=r['book_ID']
                ad_bn=r['book_name']
                ad_an=r['author_name']
                ad_q=r['qty']
                sqlQ = "UPDATE search_book SET sr_no=%s,book_ID=%s,book_name=%s,author_name=%s,qty=%s WHERE sr_no='"+fn+"' "
                print(sqlQ," = value of sqlQ")
                value=(ad_sr,ad_id,ad_bn,ad_an,ad_q)
                mycursor.execute(sqlQ, value)
                mydb.commit()
                print("..............")
                sql2="SELECT * FROM search_book"
                mycursor.execute(sql2)
                myresult=mycursor.fetchall()
                print(myresult)
        return render_template('table2.html',da=myresult)

#=========admin added book **show admin** and use to update and Delete Record==========
@app.route("/search_book")
def search_book():
        sql2="SELECT * FROM search_book"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(myresult)
        return render_template('table2.html',da=myresult)
#========== student reuest book : show admin dashboard==========
@app.route("/table_adminrequest")
def table_adminrequest():
        sql2="SELECT * FROM requestbook"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(myresult)
        return render_template('table_adminrequest.html',da=myresult)

#=============for show student issued book in admin page===============
@app.route("/table_issuedbook")
def table_issuedbook():
        sql2="SELECT * FROM stud_issuedbook"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(myresult)
        return render_template('table_issuedbook.html',da=myresult)

@app.route("/table_adminreturn")
def table_adminreturn():
        sql2="SELECT * FROM returnbook"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(myresult)
        return render_template('table_adminreturn.html',da=myresult)

@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route("/admin_login")
def admin_login():
        return render_template('admin_login.html')

@app.route("/admin_regis")
def admin_regis():
        return render_template('admin_regis.html')

@app.route("/adminlogin_check",methods = ['POST', 'GET'])
def adminlogin_check():
    if request.method == 'POST':
        r = request.form
        fn=r['email']
        pas=r['password']
        sql2="SELECT * FROM `admin` WHERE email='"+fn+"' AND password='"+pas+"' "
        print(sql2,"=for login_check value")
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        print(len(myresult))
        if(len(myresult)>0):
            return render_template('admin_dashboard.html')
        else:
            he="Invalid Username OR Password"
            return render_template('admin_login.html',he=he)
#===============For search record(all tables--table2,stud_search,issued table,return table)=======
#==============function for searching data============================
@app.route("/search_addbookadmin")
def search_addbookadmin():
        w=request.args.get('fn')
        updt_book_ID=w;
        print("value show")
        sql2="SELECT * FROM search_book WHERE book_name='"+w+"'"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        #print(myresult)
        return render_template('table2.html',da=myresult,fn=w) 
#=====for search admin add books in student record=======
@app.route("/search_b")
def search_b():
        w=request.args.get('fn')
        updt_book_ID=w;
        print("value show")
        sql2="SELECT * FROM search_book WHERE book_name='"+w+"'"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        #print(myresult)
        return render_template('stud_search.html',da=myresult,fn=w)
#=====for search student added book(issued Book) in Admin dashboard=======
@app.route("/search_adminissued")
def search_adminissued():
        w=request.args.get('fn')
        updt_book_ID=w;
        print("value show")
        sql2="SELECT * FROM stud_issuedbook WHERE book_name='"+w+"'"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        #print(myresult)
        return render_template('table_issuedbook.html',da=myresult,fn=w)
#=====search record on student dashboard(isssued book)=======
@app.route("/search_studiss")
def search_studiss():
        w=request.args.get('fn')
        updt_book_ID=w;
        print("value show")
        sql2="SELECT * FROM stud_issuedbook WHERE book_name='"+w+"'"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        #print(myresult)
        return render_template('table_studissued.html',da=myresult,fn=w)
#=====search record on student dashboard(Return book)=======
@app.route("/search_studreturn")
def search_studreturn():
        w=request.args.get('fn')
        updt_book_ID=w;
        print("value show")
        sql2="SELECT * FROM returnbook WHERE book_name='"+w+"'"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        #print(myresult)
        return render_template('table_studreturn.html',da=myresult,fn=w)
#=====search record on admin Dashboard(Return book)=======
@app.route("/search_adminreturn")
def search_adminreturn():
        w=request.args.get('fn')
        updt_book_ID=w;
        print("value show")
        sql2="SELECT * FROM returnbook WHERE book_name='"+w+"'"
        mycursor.execute(sql2)
        myresult=mycursor.fetchall()
        #print(myresult)
        return render_template('table_adminreturn.html',da=myresult,fn=w)

#---------close---------------------------------------------
if __name__ =='__main__':
    app.run()
