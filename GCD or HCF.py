#https://www.codingninjas.com/studio/problems/hcf-and-lcm_840448?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf

def gcd(a,b):
    if not a:
        return b
    if a > b:
        return gcd(a%b,b)
    else:
        return gcd(b%a,a)

n, m = [int(i) for i in input().split()]
if n>m:
    print(gcd(n%m,m))
else:
    print(gcd(m%n,n))
