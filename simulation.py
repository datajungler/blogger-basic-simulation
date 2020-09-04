import numpy as np

N = 1000
k = 30
total = np.zeros(N)
total_score = np.zeros(k)


for i in range(N):
    chinese = np.random.permutation(k)
    chinese = [1 if l <= 20-1 else 0 for l in chinese]
    
    math = np.random.permutation(k)
    math = [1 if l <= 23-1 else 0 for l in math]
    
    eng = np.random.permutation(k)
    eng = [1 if l <= 27-1 else 0 for l in eng]
    for j in range(k):
        total_score[j] = chinese[j] + math[j] + eng[j]
    
    total[i] = sum([1 if t==3 else 0 for t in total_score])
    
        
print(total)
print("# of ppl got three full marks: {0}".format(min(total)))
