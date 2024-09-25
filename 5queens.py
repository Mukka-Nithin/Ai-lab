class solution:
    def __init__(self):
        self.Max=6
        self.A=[0]*self.Max
    def placement(self,i,j):
        for k in range(1,i):
            if (self.A[k] ==j) or abs(self.A[k] -j)==abs(k-i):
                return False
        print(self.A)
        return True
    def printplacedqueen(self,N):
        print('arrangment--->')
        print()

        for i in range(1,N+1):
            for j in range(1,N+1):
                if self.A[i] !=j:
                    print('\t_',end='')
                else:
                    print('\tq',end='')
            print()
            print()
    def N_queens(self,i,j):
        for k in range(1,N+1):
            if self.placement(i,k):
                self.A[i]=k
                if i == N:
                    self.printplacedqueen(N)
                else:
                    self.N_queens(i+1,N)
N=int(input("enter the queen value:"))
obj=solution()
obj.N_queens(1,N)
