weight = int(input())
height = float(input())
index = weight / (height**2)

if index < 18.5:
  print('body index :' , index, "underweight")
  
elif index < 25 :
  print ('body index :', index, "normal")
  
elif index < 30 :
  print ('body index :', index, "Overweight")
  
elif index >= 30 :
  print('body index :', index, 'Obesity')
  