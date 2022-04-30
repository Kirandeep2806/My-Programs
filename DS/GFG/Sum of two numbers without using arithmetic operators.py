#User function Template for python3

def sum(a,b):
    carry = 0
    setBitPos = 0
    res = 0
    while a or b:
        a_lsb = a&1
        b_lsb = b&1
        if carry and (a_lsb & b_lsb):
            carry = 1
            res = (1 << setBitPos) | res
        elif (carry and (a_lsb | b_lsb)) or (carry == 0 and (a_lsb & b_lsb)):
            carry = 1
        elif carry == 0 and not(a_lsb | b_lsb):
            carry = 0
        else:
            res = (1 << setBitPos) | res
            carry = 0

        setBitPos += 1
        a >>= 1
        b >>= 1
    if carry:
        res = (1 << setBitPos) | res
    return res
            
            
            

#{ 
#  Driver Code Starts
import math
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        inp = list(map(int,input().split())) 
        
        a=inp[0]
        b=inp[1]
        
        #ob=Solution()
        print(sum(a,b))
     
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends