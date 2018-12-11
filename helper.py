import random

def read_input(s):
    file = open(s)
    return_array = []
    a = file.readline()
    while(a):
        d = map(float,a.split())
        return_array.append(d)
        a = file.readline()
    return return_array

def part_data(a):
    random.shuffle(a)
    partition = int(len(a)*0.75)
    return a[:partition],a[partition:]

def get_stats(a):
    mean = [0,0]
    variance = [0,0]
    for i in a:
        mean[0] += i[0]
        mean[1] += i[1]
        variance[0] += pow(i[0],2)
        variance[1] += pow(i[1],2)
    mean[0] /= len(a)
    mean[1] /= len(a)
    variance[0] /= len(a)
    variance[1] /= len(a)
    variance[0] -= pow(mean[0],2)
    variance[1] -= pow(mean[1],2)
    return (mean,variance)

def matrix_multiply(X,Y):
    return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

def matrix_add(X,Y):
    return [[X[i][k]+Y[i][k] for k in range(0,len(X[0]))] for i in range(0,len(X))]

def cov_div(X,n):
    return [[X[i][j]/float(n) for j in range(0,len(X[0]))] for i in range(0,len(X))]

def cov_diagonal(X):
    return [[X[i][j] if(i==j) else 0 for j in range(0,len(X[0]))] for i in range(0,len(X))]

def transpose(X):
    return zip(*X) 

def get_cov(m1,m2,input1,input2):
    s = 0.0
    for i in range(len(input1)):
        s += (input1[i] - m1)*(input2[i] - m2)
    s /= len(input1)
    return s

def cov_matrix(input,mean):
    m = [[],[]]
    X = []
    Y = []
    mean_X = mean[0]
    mean_Y = mean[1]
    for i in input:
        X.append(i[0])
        Y.append(i[1])
    m[0].append(get_cov(mean_X,mean_X,X,X))
    m[0].append(get_cov(mean_X,mean_Y,X,Y))
    m[1].append(get_cov(mean_Y,mean_X,Y,X))
    m[1].append(get_cov(mean_Y,mean_Y,Y,Y))
    return m

def get_determinant(matrix):
    return matrix[1][1]*matrix[0][0] - matrix[0][1]*matrix[1][0]

def get_difference_vector(input,mean):
    m = []
    m.append(input[0]-mean[0])
    m.append(input[1]-mean[1])
    return [m]

def inverse_matrix(m):
    determinant = get_determinant(m)
    return [[m[1][1]/determinant, -1*m[0][1]/determinant],[-1*m[1][0]/determinant, m[0][0]/determinant]]