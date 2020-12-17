def eval_expr(r,d={}):

    r=r.split()

    n=len(r)

    zas =[]

    counter=0

    # GJ: Načo robíte toto?
    for i in range(n):

        if r[i] in d:

            counter+=1

    # GJ: toto asi nie je v poriadku. Ak tam nie sú premenné, je to výraz bez premenných,
    # GJ: no a čo? Nemusí byť zato rovný nule, nie? Opravujem zakomentovaním.
    # if counter == 0:
    #    return 0

    # GJ: Takto sa cyklus tohto typu v Pythone nerobí.
    # GJ: Je to *nonpythonic*, explicitne som to zakazoval na prednáške.
    # GJ: Má tam byť for token in r:
    # GJ: a potom všade miesto r[i] má byť token.
    # GJ: Premennú i totiž nikde nepotrebujete, potrebujete r[i].

    for i in range(n):

        if r[i] in d:
    
            zas.append(int(d[r[i]]))

        if r[i].isdigit():

            zas.append(int(r[i]))

        elif r[i]=="+":

            a=zas.pop()

            b=zas.pop()

            zas.append(int(a)+int(b))

        elif r[i]=="*":

            a=zas.pop()

            b=zas.pop()

            zas.append(int(a)*int(b))

        elif r[i]=="/":

            a=zas.pop()

            b=zas.pop()

            zas.append(int(b)/int(a))

        elif r[i]=="-":

            a=zas.pop()

            b=zas.pop()

            zas.append(int(b)-int(a))            

    return zas.pop()


def to_infix(r):

    r=r.split()

    zas=[]

    n=len(r)

    for i in range(n):

        if r[i].isdigit():

            zas.append(int(r[i]))

        elif r[i] == "+":
            a=zas.pop()

            b=zas.pop()

            txt1=" ({} + {}) ".format(a,b)

            zas.append(txt1)

        elif r[i] == "-":

            a=zas.pop()

            b=zas.pop()

            txt2=" ({} - {}) ".format(a,b)

            zas.append(txt2)


        elif r[i]=="*":

            a=zas.pop()

            b=zas.pop()

            txt3=" ({} * {}) ".format(a,b)

            zas.append(txt3)


        elif r[i]=="/":

            a=zas.pop()

            b=zas.pop()

            txt4=" ({} / {}) ".format(a,b)

            zas.append(txt4)

    # GJ: return, nie print
    return zas.pop()


    

