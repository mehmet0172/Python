# # list =[1,2,3,4,5,6,7]
# # for x in list:l
# #   if x%2==1 and x>4:
# #     print(x)
# #     break
 
# # num = [42,8,7,1,124,8897,555]
# # sum = 0
# # for x in num:
# #   sum += x 
# #   print(sum)
# # x = range(5)
# # print(x)
  
# nums = list(range(3,15,3))
# print(nums[2])
#print('Это первый этаж.')
# Первый этаж построен, начинайте строить со второго
#for i in range(2,11):
#    a = i - 1
#    # Здесь вместо многоточий
#    # вставьте номер текущего этажа,
#    # вычислите и вставьте номер предыдущего этажа.
#    print('А это', i, 'этаж, он на один выше, чем этаж',a)
#months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

#for i in reversed(months):#tersine yazdirma saydirma
#    print(i)
#countdown_str = ''

#for i in reversed(range(0, 11)):
    
#    countdown_str = countdown_str + str(i) + ','

#countdown_str = countdown_str + ' ' + 'поехали!'
#print(countdown_str)



# Добавьте новые условия в elif и else
# Добавьте новые условия в elif и else
for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        # напишите ваш код здесь
        print('У вас', messages_count, 'новых сообщений')
    elif messages_count >= 2 and messages_count <= 4 :
        # напишите ваш код здесь
        print('У вас', messages_count, 'новых сообщений')
    else:
        # напишите ваш код здесь
        print('У вас', messages_count, 'новых сообщений')