if __name__ == '__main__':
    nested_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name, score])
        
    lowest, second_lowest = 100, 100 


    for student in nested_list:
        marks = student[1]
        if lowest>marks:
            second_lowest = lowest
            lowest = marks
        elif second_lowest>=marks and lowest<marks:
            second_lowest = marks
    
    second_lowest_student = []
    for student in nested_list:
        if second_lowest == student[1]:
            second_lowest_student.append(student[0])

    for i in sorted(second_lowest_student):
        print(i)
