

import sqlite3

conn = sqlite3.connect('my_account.db')
sql = conn.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS b_acc (username TEXT, usernumber TEXT,repl_bal INTEGER,withdrawal_m INTEGER, my_balance INTEGER,deposit INTEGER);')
sql.execute('INSERT INTO b_acc (username,usernumber,repl_bal,withdrawal_m,my_balance,deposit) VALUES ("Паша","+998",45667,45677,3455,3445);')

name = input("Введите свое ИФО: ")

sql.execute("SELECT * FROM b_acc WHERE username=?", (name,))
result = sql.fetchone()

if result is None:
   number = input("Введите свой номер телефона: ")
   balance = int(input("Введите свой баланс: "))
   a = int(input("Введите поступившую сумму: "))
   repl = balance+a
   b = int(input("Какая сумма денег была снята с вашего баланса: "))
   withdrawl = balance-b
   deposit1 = int(input("Введите сумму вклада: "))
   deposit = deposit1 *1/100
   deposit2 = deposit *1/100
   deposit3 = deposit2 *1/100
   sql.execute("INSERT INTO b_acc (username,usernumber,repl_bal,withdrawal_m,my_balance,deposit) VALUES(?,?,?,?,?,?);", (name,number,repl,withdrawl,balance,deposit))
   sql.execute("INSERT INTO b_acc (username,usernumber,repl_bal,withdrawal_m,my_balance,deposit) VALUES(?,?,?,?,?,?);",(name,number,repl,withdrawl,balance,deposit2))
   sql.execute("INSERT INTO b_acc (username,usernumber,repl_bal,withdrawal_m,my_balance,deposit) VALUES(?,?,?,?,?,?);",(name,number,repl,withdrawl,balance,deposit3))
   conn.commit()
else:
    question = input("Вы хотите просмотреть базу данных: ")
    if question.lower() =="да":
       print(sql.execute('SELECT * FROM b_acc WHERE username = ?;', (name,)).fetchall())
    else:
        print("Неизвестная операция")

question2 = input("Выберите действие: ")
if question2.lower() =="поиск":
    question1 = input("Введите имя: ")
    question3 = input("Введите номер: ")
    sql.execute("SELECT * FROM b_acc WHERE username=? AND usernumber=?", (question1, question3))
    results = sql.fetchall()
    for row in results:
        print(row)
    conn.commit()
else:
     pass

