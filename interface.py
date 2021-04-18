from network import *
v = input("Enter number of nodes: ")
k = input("Enter agent density (in percentage): ")
d = input("Enter number of attacker nodes: ")
n = input("Enter number of attacks: ")
t = input("Enter threshold: ")

v=int(v)
k = float(k)
k = (100+k-1)//k
d=int(d)
n=int(n)
t=float(t)


g = grid(v,d,k,n,t)
g.initiate()
while 1:
    g.run()
    char = input("Do you want to run again with different threshold value(Y/N)? ")
    if char=='Y' or char=='y':
        t = input("Enter new threshold: ")
        t=float(t)
    else:
        break