import hashlib
import math

def encrypt_text(p_text,n):
    ans = ""
    
    for i in range(len(p_text)):
        ch = p_text[i]
        
        if ch==" ":
            ans+=" "
         
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
            
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
            
    return ans

#print("||welcome to Ceaser cipher||")
p_text = input("Please enter plain text:")
n = int(input("Please enter your key:")) 
#print("Plain Text is : " + p_text)
#print("Key pattern is : " + str(n))
a = encrypt_text(p_text,n)
a = a.swapcase()

print("Cipher Text is : " +a)

def decrypt_text(c_text, k):

    dec = ""
    
    for j in range(len(c_text)):
        cha = c_text[j]
        
        if cha==" ":
            dec+=" "
         
        elif (cha.isupper()):
            dec += chr((ord(cha) - k-65) % 26 + 65)
            
        else:
            dec += chr((ord(cha) - k-97) % 26 + 97)
            
    return dec

c_text = input("\nPlease enter cipher:")
k = int(input("Please enter your decryption key:")) 
#print("Cipher is : " + c_text)
#print("Key pattern is : " + str(k))
b = decrypt_text(c_text,k)
b = b.swapcase()

print("Plain Text is : "+b)


def encryptRailFence(text, key):
 
    rail = [['\n' for i in range(len(text))]
                  for j in range(key)]
     
    dir_down = False
    row, col = 0, 0
     
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))
     
def decryptRailFence(cipher, key):
 
    
    rail = [['\n' for i in range(len(cipher))]
                  for j in range(key)]
     
    dir_down = None
    row, col = 0, 0
     
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
         
        rail[row][col] = '*'
        col += 1
         
        if dir_down:
            row += 1
        else:
            row -= 1
             
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
               (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
         
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
         
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))
 


def diffe_helman():
 
    n = 179
    g = 7

    user_A = int(input("private key of user a :"))
    if (user_A > n):
        #print("private key entered should be less than n!")
        return user_A
    
    else:
        pb1 = pow(g, user_A) % n


    user_B = int(input("private key of user b:"))
    if (user_B > n):
        #print("private key entered should be less than n!")
        return user_B
    
    else:
        pb2 = pow(g, user_B) % n
        #print("public key of user B is :", pb2)
    
diffe_helman()

def hashing():
    #print("TO CHECK FILE TEMPERING")
    x = input("enter text :")
    text = hashlib.md5(x.encode())
    print(text.hexdigest())

    y = input("to check tamper :")
    text2 = hashlib.md5(y.encode())
    print(text2.hexdigest())

    if(text.hexdigest() == text2.hexdigest()):
        #print("text is not tampered bro chill you are safe!!")
        return text.hexdigest()
    else:
        #print("bhai temper hogaya :|")
        return text2.hexdigest()
hashing()


def rsa():
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
        #print("Value of d: ", d)
        cypherText = pow(k, e) % n
        print("Cypher text is ", cypherText)
        messageDecrypt = pow(cypherText, d) % n
    else:
        return p
        
rsa()


