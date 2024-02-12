import sys
import math



def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def Q1(filename):
    print("Q1")
    X = shred(filename)
    #print
    for letter, count in X.items():
        print(f"{letter} {count}")

# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!

#shreds and returns the vector of file
def shred(filename):
    X = dict()
    with open (filename,encoding='utf-8') as f:
        # TODO: add your code here
        for line in f:
            for char in line:
                #check for english alphabet
                if char.isalpha() and char.isascii():
                    #update
                    upper_char = char.upper()
                    X[upper_char] = X.get(upper_char, 0) + 1
                
    #add the uncounted letters
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in alphabet:
        if letter not in X:
            X[letter] = 0;
    
    #sort
    newX = dict(sorted(X.items()))
    
    return newX

#takes a string and truncate to 4 decimals and float it
def truncate(x):
    return float("{:0.4f}".format(x))

#prints X1logE1 and X1logS1 as truncated values
def Q2(filename, index):
    print("Q2")
    Xe, Xs = x_log_p(filename, index)
    print(truncate(Xe))
    print(truncate(Xs))

#returns 1.2 calculation as a str without truncating
def x_log_p(filename, index):
    X = shred(filename)
    e,s = get_parameter_vectors()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #multiply # of A's and log10(of english vector for A)
    Xa = X.get(alphabet[index])
    Xe = float(Xa) * math.log(float(e[index]))
    #multiply # of A's and log10(of spanish vector for A)
    Xs = float(Xa) * math.log(float(s[index]))
    
    return Xe, Xs

#prints out F(english) and F(spanish)
def Q3(filename):
    print("Q3")
    Fe, Fs = F(filename)
    print(Fe)
    print(Fs)

#calculates and returns F(english) and F(spanish)
def F(filename):
    esum = 0 #english sum from i = [1,26] XilogPi
    ssum = 0 #spanish sum ...
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    emult = 0.6
    
    for i in range(26):
        Xe, Xs = x_log_p(filename, i)
        esum += Xe
        ssum += Xs
        #print(alphabet[i] + ' ' + str(Xe) + ' ' + str(Xs))
    
    return (truncate(math.log(0.6) + esum)), (truncate(math.log(0.4) + ssum))

#determines if file is english or spanish
def e_or_s(filename):
    print("Q4")
    Fe, Fs = F(filename)
    
    if (Fs - Fe >= 100): #english
        print(0)
    elif (Fs - Fe <= -100):
        print(1)
    else:
        val = 1/(1 + math.e**(Fs-Fe))
        print(truncate(val))
    

# main
def main():
    Q1("./letter.txt")
    Q2("./letter.txt", 0)
    Q3("./letter.txt")
    e_or_s("./letter.txt")
    
    
main()