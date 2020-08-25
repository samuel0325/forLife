score = [(90,80),(85,75),(90,100)]
for i in range(1,4):
    print("{}번 학생의 총점은 {}점이고, 평균은 {}입니다.".format(i, score[i-1][0]+score[i-1][1], (score[i-1][0]+score[i-1][1])/2))
    