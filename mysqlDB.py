# import mysql.connector
# import pymysql
#
# class mysqlDB():
#    # Open database connection
#    db = pymysql.connect("localhost","testuser","user123","dbuser")
#
#    # prepare a cursor object using cursor() method
#    conn = db.cursor()
#
#    print("Enter datas")
#    names=input()
#    surname=input()
#    age=input()
#    logg=input("login ")
#    passw=input("passw ")
#
#
#    try:
#       # Execute the SQL command
#       conn.execute("INSERT INTO customers (name, surname, AGE, login, password) VALUES ('%s', '%s', '%d', '%s','%s')" % \
#                      (names, surname,age,logg,passw))
#       # Commit your changes in the database
#       db.commit()
#    except:
#       # Rollback in case there is any error
#       db.rollback()
#
#    # disconnect from server
#       db.close()