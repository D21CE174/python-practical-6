
#AIM: You are given n words. Some words may repeat. For each word, 
# output its number of occurrences. 
# The output order should correspond with the input order of appearance of the word. 
# See the sample input/output for clarification. 
import collections;

N = int(input())
D = collections.OrderedDict()

for i in range(N):
    WORD = input()
    if WORD in D:
        D[WORD] +=1
    else:
        D[WORD] = 1 

print(len(D));

for K,V in D.items():
    print(V,end = "");
print("this program is prepared by darshan and id :d21ce174")