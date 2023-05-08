from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox,QWidget
from PyQt5.QtGui import QFont,QFontDatabase
from PyQt5.uic import loadUi
from PyQt5 import QtCore
import sys
import hashlib
import math

import mysql.connector as con

global text
text="demo"
global k
k=3
global choice

choice=1
class LoginScreen(QWidget):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui", self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.b2.clicked.connect(self.login)
        self.b1.clicked.connect(self.show_reg)
        
    def login(self):
        username = self.tb1.text()
        password = self.tb2.text()
        db = con.connect(host="localhost", user="root", password="", db="chatbot")
        cursor = db.cursor()
        self.tb1.setText("")
        self.tb2.setText("")

        cursor.execute(
            "select *from details where username='"
            + username
            + "'and password='"
            + password
            + "'"
        )
        results = cursor.fetchone()
        if results:
            QMessageBox.information(
                self, "Login Output", "You have successfully logged in!"
            )
            self.loginmain()
        else:
            QMessageBox.information(self, "Login Output", "Invalid credentials!")

    def show_reg(self):
        widget.setCurrentIndex(2)

    def loginmain(self):
        widget.setCurrentIndex(1)
        
class register(QDialog):
    global username

    def __init__(self):
        super(register, self).__init__()
        loadUi("register.ui", self)
        self.b4.clicked.connect(self.show_login)
        self.b4.clicked.connect(self.reg)

    def show_login(self):
        widget.setCurrentIndex(0)

    def reg(self):
        global username
        username = self.tb3.text()
        password = self.tb4.text()
        age = self.tb5.text()
        address = self.tb6.currentText()
        ph = self.tb7.text()
        id1 = 1
        db = con.connect(host="localhost", user="root", password="", db="chatbot")
        cursor = db.cursor()
        cursor.execute(
            "select *from details where Username='"
            + username
            + "'and Password='"
            + password
            + "'"
        )

        results = cursor.fetchone()

        if results:
            QMessageBox.information(
                self,
                "Registration Status",
                "User Already exists! please change your username",
            )
        else:
            query4 = "SELECT MAX(id) FROM details"
            cursor.execute(query4)
            id2 = cursor.fetchall()
            id1 = id2[0][0]
            id1 = id1 + 2
            query = f"insert into details values({id1},'{username}','{password}',{age},'{address}','{ph}')"
            print(id1)
            cursor.execute(query)
            db.commit()
            QMessageBox.information(
                self, "Registration status", "Registered Sucessfully"
            )
        
class main(QDialog):
    def __init__(self):
        super(main, self).__init__()
        loadUi("main.ui",self)
        global k
        global text
        self.p1.clicked.connect(self.ceasar_cypher)
        self.c1.clicked.connect(self.encrypt)
        self.c2.clicked.connect(self.decrypt)
        self.p2.clicked.connect(self.railfence)
        self.p3.clicked.connect(self.rsa)
        self.p4.clicked.connect(self.diffe_helman)
        self.p5.clicked.connect(self.hashing)
       
    
    
    def encrypt(self):
        global choice
        choice=1
        main.c2.setChecked(False)
    
    def decrypt(self):
        global choice
        choice=2
        main.c1.setChecked(False)

    def ceasar_cypher(self):
        global text 
        global k
        global choice

        text=self.i1.text()
        k=int(self.i3.text())
        if choice==1:
            ans = ""
            for i in range(len(text)):
                ch = text[i]
            
                if ch==" ":
                    ans+=" "
            
                elif (ch.isupper()):
                    ans += chr((ord(ch) + k-65) % 26 + 65)
                
                else:
                    ans += chr((ord(ch) + k-97) % 26 + 97)    
            print(ans)    
            main.i2.setText(ans)
        elif choice==2:
            dec = ""
        
            for j in range(len(text)):
                cha = text[j]
            
                if cha==" ":
                    dec+=" "
            
                elif (cha.isupper()):
                    dec += chr((ord(cha) - k-65) % 26 + 65)
                
                else:
                    dec += chr((ord(cha) - k-97) % 26 + 97)
            
            print(dec)
            main.i2.setText(dec)

    def railfence(self):
        global text 
        global k
        global choice

        text=self.i1.text()
        k=int(self.i3.text())  

        if choice==1:
            
            rail = [['\n' for i in range(len(text))]
                          for j in range(k)]
     
            dir_down = False
            row, col = 0, 0
     
            for i in range(len(text)):
                if (row == 0) or (row == k - 1):
                    dir_down = not dir_down
                rail[row][col] = text[i]
                col += 1
                if dir_down:
                    row += 1
                else:
                    row -= 1
            result = []
            for i in range(k):
                for j in range(len(text)):
                    if rail[i][j] != '\n':
                        result.append(rail[i][j])
            results=("".join(result))
            main.i2.setText(results)
            
        elif choice==2:
            
            rail = [['\n' for i in range(len(text))]
                  for j in range(k)]
     
            dir_down = None
            row, col = 0, 0
            
            for i in range(len(text)):
                if row == 0:
                    dir_down = True
                if row == k - 1:
                    dir_down = False
                
                rail[row][col] = '*'
                col += 1
                
                if dir_down:
                    row += 1
                else:
                    row -= 1
                    
            index = 0
            for i in range(k):
                for j in range(len(text)):
                    if ((rail[i][j] == '*') and
                    (index < len(text))):
                        rail[i][j] =text[index]
                        index += 1
                
            result = []
            row, col = 0, 0
            for i in range(len(text)):
                
                if row == 0:
                    dir_down = True
                if row == k-1:
                    dir_down = False
                    
                if (rail[row][col] != '*'):
                    result.append(rail[row][col])
                    col += 1
                    
                if dir_down:
                    row += 1
                else:
                    row -= 1
            results=("".join(result))
            main.i2.setText(results)
                    
    def rsa(self):
        global k
        k=int(self.i3.text())

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)


        def isPrime(a):
            for i in range(2, int(math.sqrt(a)) + 1):
                if a % i == 0:
                    return False
            return True


        def extEuc(a, b):
            old_r, r = a, b
            old_s, s = 1, 0
            old_t, t = 0, 1
            while r != 0:
                quotient = old_r // r
                old_r, r = r, (old_r - (quotient * r))
                old_s, s = s, (old_s - (quotient * s))
                old_t, t = t, (old_t - (quotient * t))

            return old_t


        p, q = 11 , 7

        if isPrime(p) and isPrime(q):
            n = p * q
            totient_n = (p - 1) * (q - 1)
            e = 2
            while e < totient_n:
                if gcd(totient_n, e) == 1:
                    break
                e += 1
                
            d = extEuc(totient_n, e) % totient_n
            cypherText = pow(k, e) % n
            print("Cypher text is ", cypherText)
            messageDecrypt = pow(cypherText, d) % n
            main.i2.setText(str(cypherText))
            
        else:
            main.i2.setText(p)
   
    def diffe_helman(self):
        global k
        k1=float(self.i3.text())
        k=int(k1)
        n = 179
        g = 7

    
        pb1 = pow(g, k) % n
        main.i2.setText(str(pb1))
   
            
    def hashing(self):
        global text
        text=self.i1.text()
        text2 = hashlib.md5(text.encode())
        text3=text2.hexdigest()
        main.i2.setText(text3)

app = QApplication(sys.argv)
reg=register()
ls=LoginScreen()
main=main()
widget=QtWidgets.QStackedWidget()
widget.addWidget(ls)
widget.addWidget(main)
widget.addWidget(reg)
widget.setFixedHeight(800)
widget.setFixedWidth(1000)
widget.setCurrentIndex(0)
widget.show()

app.exec_()