
#Hackerrank ------ Finding the percentage

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = float(sum(scores)/len(scores))
    query_name = raw_input()
    print ("%0.2f"%student_marks[query_name])
