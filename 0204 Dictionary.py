if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

#Creating a list of marks
marks = student_marks[query_name]

#Summation of marks
sum = 0
for i in marks:
    sum = sum + i

#Average of marks
res = sum / len(marks)

#Formatting res to 2 decimal points and displaying
print("{:.2f}".format(res))