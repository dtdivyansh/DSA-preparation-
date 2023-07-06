#https://practice.geeksforgeeks.org/problems/count-digits5716/1

class Solution:
    def evenlyDivides (self, N):
        num = N
        c = 0
        while(num):
            i = num%10
            if i and int(N/i) == N/i:
                c+=1
            num = num//10

        return c
