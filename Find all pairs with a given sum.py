# link of the question: https://practice.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x5808/1?page=1&curated[]=1&sortBy=submissions
#User function Template for python3

class Solution:
    def allPairs(self, A, B, N, M, X):
        a = []
        for i in A:
            for j in B:
                if i+j==X:
                    a.append([i,j])
        
        return sorted(a)



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        N, M, X = sz[0], sz[1], sz[2]
        A = [int(x) for x in input().strip().split()]
        B = [int(x) for x in input().strip().split()]
        ob=Solution()
        answer = ob.allPairs(A, B, N, M, X)
        sz = len(answer)
        
        if sz==0:
        	print(-1) 
        else: 
            
        	for i in range(sz):
        		if i==sz-1:
        		    print(*answer[i])
        		else:
        		    print(*answer[i], end=', ')
        

        T -= 1


if __name__ == "__main__":
    main()




# } Driver Code Ends