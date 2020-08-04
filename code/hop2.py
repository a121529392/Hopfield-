import numpy as np
import random

def read_sample(file):
    f=open(file,"r",encoding="utf-8")
    line=f.read()
    line=line.split("\n")

    hold=[]
    sample=[]
    column = 0
    for l in line:

        if l!='':
            column+=1
            row = 0
            for w in l:
                row +=1
                if w ==' ':
                    hold.append(-1)
                if w == "1":
                    hold.append(1)
        else:
            column = 0
            sample.append(hold)
            hold=[]

    sample.append(hold)
    return sample,row,column

def regularout(data,N,P):
    for j in range(P):
        ch = ""
        for i in range(N):
            ch += " " if data[j*N+i] == -1 else "X"
        print(ch)

def cal_weight(sample):
    N=len(sample)
    P=len(sample[0])
    for i in range(0,N,1):
        sample[i]=np.array(sample[i])
        sample[i]=sample[i][ :, np.newaxis]
        sample[i]=sample[i].dot(sample[i].T)

    sum=np.zeros(sample[i].shape)

    identity=np.identity(P)

    for i in range(0, N, 1):
        sum+=sample[i]

    return sum-N*identity

def cal_sita(weight):
    a = np.sum(weight, axis=1)
    a = a[:, np.newaxis]
    return a
def sgn(test,value):
    if value>0:
        return 1
    if value==0:
        return test
    if value<0:
        return -1
def hop_run(test,weight):
    test = np.array(test)
    for x in range(10):
        for i in range(0,len(test),1):
            hold_weight = weight[i][:, np.newaxis]
            hold = test[:, np.newaxis]
            ans=hold_weight.T.dot(hold)
            ans = np.squeeze(ans, 1)
            ans = np.squeeze(ans, 0)
            test[i]=sgn(test[i],ans)


    return test

def check_symmetric(a, rtol=1e-05, atol=1e-08):
    return np.allclose(a, a.T, rtol=rtol, atol=atol)


def add_nosie(t,value):
    v=int(value.split("%")[0])
    for i in range(0,len(t),1):
        if random.randint(0, 100) > 100-v:
            t[i] = -1*t[i]
    return t





if __name__ == '__main__':
    from sympy.matrices import Matrix, GramSchmidt
    file = "./Basic_Training.txt"
    test_file="./Basic_Testing.txt"
    bonus_train="./Bonus_Training.txt"
    bonus_test="./Bonus_Testing.txt"
    sample,sample_row,sample_column=read_sample(bonus_train)

    regularout(sample[6], 10, 10)
    test,test_row,test_column=read_sample(bonus_test)
    noise_test,n_r,n_c = read_sample(bonus_test)
    # noise_test=add_nosie(noise_test)
    weight=cal_weight(sample)
    # sita=cal_sita(weight)
    print("----org-----")
    regularout(test[6], 10, 10)
    a=hop_run(test[6],weight)

    print(weight)
    print("----result-----")
    regularout(a,10,10)

    print("----org-----")
    # regularout(noise_test[6], 10, 10)
    # b = hop_run(noise_test[6], weight)

    print("----result-----")
    # regularout(b, 10, 10)

    sample2, sample2_row, sample2_column = read_sample(file)
    print(sample2_row)
    print(sample2_column)
    regularout(sample2[1], sample2_row, sample2_column)


# print(o[0].tolist)

