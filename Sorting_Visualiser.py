#Python Program to visualise sorting algorithms using matplotlib library
import matplotlib.pyplot as plt
import numpy as np
amount = 50
speed=0.01
lst=np.random.randint(1,100,amount)
x=np.arange(0,amount,1)
n=len(lst)
def algo(select):
    if(select==1):
        colour=["grey"]
        for i in range(n):
            for j in range(n-i-1):
                plt.title("Bubble Sort")
                plt.bar(x,lst,color=colour)
                plt.pause(speed)
                plt.clf()
                if(lst[j]>lst[j+1]):
                    colour=["grey" if k!=j and k!=j+1 else "orange" if k==j else "red" for k in x]
                    for temp in range(i):
                        colour[amount-1-temp]="lime"
                    lst[j],lst[j+1]=lst[j+1],lst[j]
        plt.bar(x,lst,color="lime")
        plt.show()
    elif(select==2):
        colour=["grey"]
        for i in range(n):
            min=i
            plt.title("Selection Sort")
            plt.bar(x,lst,color=colour)
            plt.pause(speed)
            plt.clf()
            for j in range(i+1,n):
                if(lst[min]>lst[j]):
                    min=j
                colour=["orange" if k==i else "red" if k==min else "grey" for k in x]
            lst[min],lst[i]=lst[i],lst[min]
            if(i>0):
                for temp in range(i):
                    colour[temp]="lime"
        plt.bar(x,lst,color="lime")
        plt.show()
    elif(select==3):
        colour=["grey"]
        for i in range(1,len(lst)):
            key=lst[i]
            j=i-1
            plt.title("Insetion Sort")
            plt.bar(x,lst,color=colour)
            plt.pause(speed/3)
            plt.clf()
            while(j>=0 and key<lst[j]):
                colour=["lime" if k==i else "red" if k==j else "grey" for k in x]
                plt.title("Insetion Sort")
                plt.bar(x,lst,color=colour)
                plt.pause(speed/3)
                plt.clf()
                lst[j+1]=lst[j]
                j-=1
                colour=["lime" if k==i else "red" if k==j else "grey" for k in x]
                plt.title("Insetion Sort")
                plt.bar(x,lst,color=colour)
                plt.pause(speed/3)
                plt.clf()
            lst[j+1]=key
    plt.bar(x,lst,color="lime")
    plt.show()
    
print("Select any of the Sorting Algorithm")
print("To Select:")
print("Bubble Sort : Type 1")
print("Selection Sort : Type 2")
print("Insertion Sort : Type 3")
select=int(input(""))
print("Unsorted Array::",lst )
algo(select)
print("Sorted Array::",lst )