#While loop for student input
allow_in = 0
while allow_in == 0:
    num_student = int(input('How many students are in your class? '))
    if num_student > 0:
        print()
        allow_in += 1
    else:
        print('Invalid # of students. Try again.')
#While loop for test input
while allow_in == 1:
    num_test = int(input('How many tests in this class? '))
    if num_test > 0:
        print()
        allow_in += 1
    else:
        print('Invalid # of tests. Try again.')
#accumulator for the total averages calculated
total_avg = 0
#For loop for each student
for y in range(1,num_student+1):
    print('**** Student',y,'****')
    #accumulator for the total test score
    total_score = 0
    for x in range(1, num_test+1):
        while allow_in == 2:
            print('Enter score for test #',x,': ',sep='',end='')
            test_in = float(input())
            if test_in > 0:
                if test_in < 101:
                    break
                else:
                    print('Invalid score. Try again.')
            else:
                print('Invaid score. Try again.')
        total_score += test_in
        avg_score = float(format(total_score / num_test,'.2f'))
    total_avg += avg_score
    print()
    print('Average score for student #',y,' is ',avg_score,sep='')
    print()
    final_avg = float(format(total_avg / num_student,'.2f'))
print('Average score for all students is',final_avg)
    
