# #6475
# score = [(90,80),(85,75),(90,100)]
# for i in range(1,4):
#     print("{}번 학생의 총점은 {}점이고, 평균은 {}입니다.".format(i, score[i-1][0]+score[i-1][1], (score[i-1][0]+score[i-1][1])/2))

# #6275
# line = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
# vowl = ['a','e','i','o','u']
# for i in vowl:
#     line = line.replace(i,"")
# print(line)

# #6276
# numbers = [[num*i for i in range(1,10) if i%3!=0 and i%7!=0]
# if num%3!=0 and num%7!=0 else [] for num in range(2,10)]
# print(numbers)


# numbers2 = []
# for i in range(2,10):
#     number = []
#     if i%3==0 or i%7==0:
#         numbers2.append(number)
#     else:
#         for j in range(1,10):
#             if(j%3!=0 and j%7!=0):
#                 number.append(i*j)
#         numbers2.append(number)
        
# print(numbers2)


