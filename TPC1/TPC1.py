s = "olameninos"

# Exercício 1

def reverse(s):
    r = s[-1::-1]
    return r

# Exercício 2

def countA(s):
    A = s.lower()
    counter = 0
    for l in A:
        if l == "a":
            counter +=1
    return counter 

# Exercício 3 

def countvowels(s):
    v = s.lower()
    counter = 0 
    vowels = ["a","e","i","o","u"]
    for l in v:
        if l in vowels:
            counter += 1
    return counter

# Exercício 4

def lower(s):
    return s.lower()

# Exercício 5

def uppercase(s):
    return s.upper()

# Exercício 6

def capicua(s):
    c = s[-1::-1]
    if c==s:
        print("A string é uma capicua!")
    else :
        print("A string não é uma capicua!")
        
# Exercício 7

s1 = "ola"
s2 = "alo"

def balanceadas(s1,s2):
    res = True
    for l1 in s1:
        if l1 not in s2:
            res = False
    if res:
        print("As strings estão balanceadas!")
    else:
        print("As strings não estão balanceadas!")
        
# Exercício 8 

def ocorrencias(s1,s2):
    tamanho = len(s1)
    count = 0 
    
    for i in range(0,len(s2)-tamanho+1):
        if s1 == s2[i:i+tamanho]:
            count += 1
    
    return count

# Exercício 9 

a = "listen" 
b = "silent"
c = "hello"
d = "world"

def anagrama (a,b):
    res = True
    listar = list(b)
    if len(a)==len(b):
        for l1 in a:
            if l1 not in listar:
                res = False
            else : 
                listar.remove(l1)
    else :
        res = False 
        
    return res

# Exercício 10

from collections import defaultdict

def classes_anagrama(dic):
    classes = defaultdict(list)
    
    for palavra in dic:
        chave = "".join(sorted(palavra))  
        classes[chave].append(palavra)
    
    return dict(classes)

dic = ["gato", "toga", "pato", "topa", "fato", "tafo"]

for chave, palavras in classes_anagrama(dic).items():
    print(f"Classe {chave}: {palavras}")