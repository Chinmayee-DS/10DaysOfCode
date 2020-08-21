# # Enter your code here. Read input from STDIN. Print output to STDOUT
q = int(input())
queue = []
ret = []
ar = []
i = x = 0
while(i < q):
   # temp = raw_input()
    #print(temp)
    # if(temp == 1):
    #i = i+1
    #     one = int(input())
    #     print(one)
    #     continue
      
     ar = list(map(int, raw_input().split()))
     if ar[0] == 1:
         queue.append(ar[1])
     elif ar[0] == 2:
         queue.pop(0)
     else:
         ret.append(queue[0])
     i = i+ 1
for x in range(len(ret)):
    print(ret[x])


