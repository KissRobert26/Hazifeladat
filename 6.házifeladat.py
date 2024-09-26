
szam= int(input ("Kérem adjon meg egy szöget 0° és 360° között!"))

if (szam >= 0) and (szam <= 360):
      if(szam == 0):
          print(szam,"fok nullszög")
      if (szam > 0) and (szam < 90):
          print(szam, "fok hegyesszög")
      if (szam == 90):
          print(szam, "fok derékszög")
      if (szam > 90) and (szam < 180):
          print(szam, "fok tompaszög")
      if (szam == 180):
          print(szam, "fok egyenesszög")
      if (szam > 180) and (szam < 360):
          print(szam, "fok homorúszög")
      if (szam == 360):
          print(szam, "fok teljesszög")


