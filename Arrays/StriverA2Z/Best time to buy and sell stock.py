class Solution:
    def stockBuySell(self, arr, n):
        currentmax=0
        for i in range(n-1):
            for j in range(i+1,n):
                if(arr[j]>arr[i]):
                    currentmax=max((arr[j]-arr[i]),currentmax)
        return currentmax
  