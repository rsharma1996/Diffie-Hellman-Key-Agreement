# Python code for key exchange
"""
mypowerfunction:  a customizable exponential function for computing g^(A*b)mod p, exponentiation by squaring/modular exp
1.p is a prime number taken from the link provided: Converted it into an int of base 10
2.g is the generator g=2 for DH ffdh2048 bits
3.The program asks the client to enter their private key (Student #) as the server's private key is hardocded
4.First we compute g^(a) mod p for Client where a is Client's student #
5.Then we compute g^(b) mod p for Server where b is Server's private key 4472
6.Now, this gives us the public keys for both the Server and client.
Taking these values, we compute:
7.Clients shared secret as servers public key^(Client's private key) mod p
8.Servers shared secret as clients public key6(Servers private key) mod p
***If this is same, the program works!***
"""


def mypowerfunc(base, exp,mod):
    if exp < 0:
        x = 1 / base
        y = -exp
    elif exp == 0:
        x = 1
    else:
        n = mypowerfunc(base, exp // 2,mod)
        x = n * n
        if exp % 2 == 1:
            x *= base
    return x %mod


p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
g = 2
print("Prime number is: ", p)
print("Generator used is: ", g)
MyPrivateKey = int(input("Please enter your private key: "))
# MyPublicKey= mypowerfunc(g,MyPrivateKey,p)
MyPublicKey= pow(g,MyPrivateKey,p)
print("Your public key is this: ", MyPublicKey)
ServerPrivateKey = 4472
ServerSharedPublic=pow(g,ServerPrivateKey,p)
# ServerSharedPublic=mypowerfunc(g,ServerPrivateKey,p)
print("Servers public key is this: ", ServerSharedPublic)
# MySharedSecret = mypowerfunc(ServerSharedPublic, MyPrivateKey,p)
MySharedSecret = pow(ServerSharedPublic, MyPrivateKey,p)
print("Your shared secret with server is this: ", MySharedSecret)
# ServerSharedSecret =mypowerfunc(MyPublicKey, ServerPrivateKey,p)
ServerSharedSecret =pow(MyPublicKey, ServerPrivateKey,p)
print("Servers shared secret is this: ", ServerSharedSecret)
print("\n-------\n")
# SharedSecret= mypowerfunc(g,(MyPrivateKey*ServerPrivateKey),p)
SharedSecret= pow(g,(MyPrivateKey*ServerPrivateKey),p)
print("Shared secret as per the formula explained during class: ", SharedSecret)