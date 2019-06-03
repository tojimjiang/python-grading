#Part 1
#Data File Reading
file_found = 0
while file_found == 0:
    file_name = input('Enter a file name (i.e. class1 for class1.txt): ')
    try:
        read_file = open(file_name + '.txt', 'r')
        print('Successfully opened ', file_name, '.txt', sep='')
        break
    except:
        print('File can not be found')
        print()
print()
print('**** ANALYZING ****')
print()
read_file_str = read_file.read()
split_read = read_file_str.split()
#This means that split read is sprint based on the positions of the N's
split_read_len = len(split_read)

invalid_count = 0
valid_count = 0
class_point = 0
highest_score = 0
lowest_score = 0
all_scores = []
score_seen = []
score_count = []
student_list = {}

#HARD CODED ANSWER KEY
answerkey = 'B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D'
#Answerkey Processing
answer_list = answerkey.split(',')
#Student Information Processing
for x in range(0,split_read_len):
    student_split = split_read[x].split(',')
    #Extract ID Number:
    id_number = student_split[0]
    id_digits = id_number[1:]
    #Validate List Slots
    if len(student_split) != 26:
        print('Invalid line of data: does not contain exactly 26 values:')
        print(student_split)
        print()
        invalid_count += 1
    #Validate 9 Len ID
    elif len(student_split[0]) != 9:
        print('Invalid line of data: N# is invalid!')
        print(student_split)
        print()
        invalid_count += 1
    #Validate "N" ID
    elif id_number[0] != 'N':
        print('Invalid line of data: N# is invalid!')
        print(student_split)
        print()
        invalid_count += 1
    #Validate 8 Digits after N
    elif not id_digits.isnumeric():
        print('Invalid line of data: N# is invalid!')
        print(student_split)
        print()
        invalid_count += 1
    else:
        valid_count += 1
        student_point = 0
        ###print (student_split[0])
        #The Grader
        for y in range(1,26):
            if student_split[y] == answer_list[y-1]:
                student_point += 4
                ###print('Correct')
            elif student_split[y] == '':
                ###print('Omit')
                student_point += 0
            else:
                student_point -= 1
                ###print('Incorect')
        #Student Grade Processing Recieving
        class_point += student_point
        #Add Student Score to Grade List
        student_list[student_split[0]] = student_point
        #Record Score in All Score list
        all_scores.append(student_point)
#NO ERRORS Message
if invalid_count == 0:
    print('No errors found!')
    print()
#After Grading, Data is processed
#sort list
all_scores.sort()
#length of all scores list
all_scores_len = len(all_scores)
for z in range (0, all_scores_len-1):
    if all_scores[z] in score_seen:
        location_seen = score_seen.index(all_scores[z])
        score_count[location_seen] += 1
    else:
        score_seen.append(all_scores[z])
        score_count.append(1)
#Solve for Mean Score:
mean_score = class_point/valid_count
#Find High/Low Scores
lowest_score = score_seen[0]
highest_score = max(score_seen)
#Find Mode(s)
mode_count = max(score_count)
mode_freq = score_count.count(mode_count)
if mode_freq == 1:
    mode_index = score_count.index(mode_count)
    mode_score = score_seen[mode_index]
else:
    prev_mode = -1
    mode_score = []
    for a in range(0,mode_freq - 1):
        mode_index = score_count.index(mode_count,prev_mode + 1)
        prev_mode = mode_index
        mode_score.append(score_seen[mode_index])
#Find Median
score_len = len(all_scores)
if score_len % 2 == 1:
    median_index = score_len // 2 - 1
    median_score = all_scores[median_index]
else:
    high_median = score_len//2
    low_median = high_median - 1
    median_score = (all_scores[high_median] + all_scores[low_median])/2
#Test Result Report
print('**** REPORT ****')
print('Total valid lines of data:', valid_count)
print('Total invalid lines of data:', invalid_count)
print()
print('Mean (average) score:', mean_score)
print('Highest score:',highest_score)
print('Lowest score:',lowest_score)
print('Range of Scores:', highest_score - lowest_score)
print('Median score:', median_score)
print('Mode score(s):',mode_score)
#Curve Request
while file_found == 0:
    curve_request = input('Would you like to apply a curve to the scores? (y)es or (n)o? ')
    if curve_request == 'y':
        break
    elif curve_request == 'n':
        break
    else:
        print('Your input was not understood, please try again')
#Curve Score Request
while curve_request == 'y':
    try:
        curve_to = float(input('Enter a desired mean score: '))
        if curve_to < mean_score:
            print('Your desired mean score is lower than the current mean score, please try again')
        elif curve_to == mean_score:
            print('Your desired mean score is the same as the current mean score, please try again')
        elif curve_to > 100:
            print('Your curve is past a 100, the maximum grade, please try again')
        elif curve_to > mean_score:
            curve_amt = curve_to - mean_score
            break
    except:
        print('You did not enter a valid grade! Please try again')
#Curve creating file
if curve_request == 'y':
    print('Done! A new grade file has been written! (', end='')
    curve_file = open(file_name+'_grades_with_curve.txt','w')
    #writing file curve function from sorted dictionary
    for key, values in sorted(student_list.items()):
        curve_file.write(key)
        curve_file.write(',')
        curve_file.write(str(values))
        curve_file.write(',')
        curve_file.write(str(values + curve_amt))
        curve_file.write("\n")
    curve_file.close()
    print(file_name+'_grades_with_curve.txt', ')', sep='')
#Normal Grades File
if curve_request == 'n':
    print('OK! A grade file has been created! (', end='')
    grade_file = open(file_name+'_grades.txt','w')
    #writing grade file function from sorted dictionary
    for key, values in sorted(student_list.items()):
        grade_file.write(key)
        grade_file.write(',')
        grade_file.write(str(values))
        grade_file.write("\n")
    grade_file.close()
    print(file_name+'_grades.txt', ')', sep='')
    
