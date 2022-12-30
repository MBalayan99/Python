import qrcode
data = 'https://www.linkedin.com/in/mher-balayan-23051999/'
data1 = 'Հայլուր 15։30 Ադրբեջանցիները բացել են Լաչինի միջանցքը՝ միայն շտապօգնության մեքենայի համար'
img = qrcode.make(data)
img_1 = qrcode.make(data1)
img.save('My_Linkedin.png')

#print(img_1.__sizeof__)
img_1.save('text.jpg')