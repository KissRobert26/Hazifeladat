# A program két beolvasott számot összehasonlítva írja közéjük a megfelelő relációs jelet

szam1= int(input ("Kérem adja meg az első számot"))
szam2= int(input ("Kérem adja meg a második számot"))

if szam1 < szam2:
    print(szam1,"<" ,szam2)

elif szam1 > szam2:
    print(szam1,">" ,szam2)

else:
    print(szam1, "=", szam2)



