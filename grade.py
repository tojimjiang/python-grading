#ask for name and class
name = input('What is your name? ')
course = input('What class are you in? ')
#linegap
print()
#ask for test weight
weight_t = float(input('How much are tests worth in this class (i.e. 0.40 for 40%): '))
#ask for test scores
test_1 = float(input('Enter test score #1: ')) / 3
test_2 = float(input('Enter test score #1: ')) / 3
test_3 = float(input('Enter test score #1: ')) / 3
#linegap
print()
#print test avg
print('Your test average is:', format(test_1 + test_2 + test_3,'.2f'))
print()
#ask for homework weight
weight_h = float(input('How much are homework assignments worth in this class (i.e. 0.60 for 60%): '))
#Check weighting is possible
weight_sum = weight_h + weight_t
if weight_sum != 1:
    #message prited if error occurs
    print(name, ', your weighting for' ,  course, 'does not add up to exactly 100%!')
#ask for second trail
    print('Would you like for this program to run with the existing values?')
    rerun = input('Enter RUN for the program to run. Otherwise press enter. CaSe SeNsItIvE!')
#check if user wants a second run
    if rerun == 'RUN':
        #ask for scores
        homework_1 = float(input('Enter homework score #1: ')) / 3
        homework_2 = float(input('Enter homework score #1: ')) / 3
        homework_3 = float(input('Enter homework score #1: ')) / 3
        #linegap
        print()
        print('Your homework average is:', format(homework_1 + homework_2 + homework_3, '.2f'))
        print()
        #calcuations
        final = format((test_1 + test_2 + test_3)*weight_t + weight_h*(homework_1 + homework_2 + homework_3),'.2f')
        print('Thanks, ',name, '. Your calculated score in ', course, ' is ', final, sep='')
        print('Please note these values are not accurate as the sum of percentages is not equal to 100%')
#check if user would like the program to automatically adjust the values to retain the entered proportionallity. 
    else :
        print('-----')
        print('Would you like for this prgoram to automatically adjust the ratios?')
        adj_run = input('Enter ADJ for the program to automatically adjust. Otherwise press enter. CaSe SeNsItIvE!')
        if adj_run == 'ADJ':
            #ask for scores
            homework_1 = float(input('Enter homework score #1: ')) / 3
            homework_2 = float(input('Enter homework score #1: ')) / 3
            homework_3 = float(input('Enter homework score #1: ')) / 3
            #linegap
            print()
            print('Your homework average is:', format(homework_1 + homework_2 + homework_3, '.2f'))
            print()
            #calcuations
            weight_t_2 = weight_t / (weight_h + weight_t)
            weight_h_2 = weight_h / (weight_h + weight_t)
            final = format((test_1 + test_2 + test_3)*weight_t_2 + weight_h_2*(homework_1 + homework_2 + homework_3),'.2f')
            print('Thanks, ',name, '. Your calculated score in ', course, ' is ', final, sep='')
#let user know what the weights used were in the auto adjust
            print('The values used for weighting were', format(weight_t_2,'.3f'), 'for tests, and', format(weight_h_2, '.3f'), 'for homework assignments')
#check if user entered values are compatible with haricuts
        elif weight_t >= 1:
            print('Your weighting for the test portion is too high! Remember to use decimal notation!')
            print('ERROR CODE: -1')
            print('This program has stopped. Pleae re-run to try again.')
        else:
            print('-----')
            #ask user if they want a haircut
            print('Would you like the program to trim the homework value to fit?')
            cut_run = input('Enter CUT for the program to haircut the values, otherwise just press enter. CaSe SeNsItIvE!')
            if cut_run == 'CUT' :
                homework_1 = float(input('Enter homework score #1: ')) / 3
                homework_2 = float(input('Enter homework score #1: ')) / 3
                homework_3 = float(input('Enter homework score #1: ')) / 3
                #linegap
                print()
                print('Your homework average is:', format(homework_1 + homework_2 + homework_3, '.2f'))
                print()
                #calcuation
                weight_h_3 = 1 - weight_t
                final = format((test_1 + test_2 + test_3)*weight_t + weight_h_3*(homework_1 + homework_2 + homework_3),'.2f')
                print('Thanks, ',name, '. Your calculated score in ', course, ' is ', final, sep='')
                #alert user to value used for homework portion
                print('The weighting used for homework assignments is,' ,weight_h_3)
            else:
                print('ERROR CODE: 2147483647')
                print('This program has stopped. Please re-run to try again.')
else : #ask for test scores
    homework_1 = float(input('Enter homework score #1: ')) / 3
    homework_2 = float(input('Enter homework score #1: ')) / 3
    homework_3 = float(input('Enter homework score #1: ')) / 3
    #linegap
    print()
    print('Your homework average is:', format(homework_1 + homework_2 + homework_3, '.2f'))
    print()
    #calcuation
    final = format((test_1 + test_2 + test_3)*weight_t + weight_h*(homework_1 + homework_2 + homework_3),'.2f')
    print('Thanks, ',name, '. Your final score in ', course, ' is ', final, sep='')


