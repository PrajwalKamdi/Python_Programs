class Arrays:
  def second_largest(self,arr):
    max=0
    for i in range(0, len(arr)):
      if(arr[i]>max):
        max=arr[i]
    print(max)

arr=Arrays()
a=[1,2,3,4,5]
arr.second_largest(a)
