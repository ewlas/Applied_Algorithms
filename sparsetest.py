from sparse_set import SparseSet
import time
import random



def main():

    #Showcase
    set1 = SparseSet(1000, 10)
    set2 = SparseSet(1000, 10)
    iter = 1000
    sumSearchX_no = 0
    sumSearchX_maybe = 0
    sumUnion = 0
    while iter > 0:
       
        set1.Insert(random.randint(3, 1000))
        set1.Insert(random.randint(3, 1000))
        set1.Insert(random.randint(3, 1000))
        set1.Insert(random.randint(3, 1000))
        set2.Insert(random.randint(3, 1000))
        set2.Insert(random.randint(3, 1000))
        set2.Insert(random.randint(3, 1000))
        set2.Insert(random.randint(3, 1000))

        print("Set 1:", set1)
        print("Set 2:", set2)

        timeSearchX_no = time.perf_counter()
        set1.Search(2)
        endtimeSearchX_no = time.perf_counter()

        timeSearchX_maybe = time.perf_counter()
        set1.Search(233)
        endtimeSearchX_maybe = time.perf_counter()

        timeUnion = time.perf_counter()
        set1.Union(set2)
        endtimeUnion = time.perf_counter()

        generalSearchX_no = endtimeSearchX_no - timeSearchX_no
        generalSearchX_maybe = endtimeSearchX_maybe - timeSearchX_maybe
        generalTimeUnion = endtimeUnion - timeUnion

        sumUnion += generalTimeUnion
        sumSearchX_maybe += generalSearchX_maybe
        sumSearchX_no += generalSearchX_no
        print(f"Execution time for union of two sets: {sumUnion:.6f} seconds")
        print(f"Execution time for searching the elem that is absent: {sumSearchX_no:.6f} seconds")
        print(f"Execution time for searching the elem that (maybe) present: {sumSearchX_maybe:.6f} seconds")
        set1.Clear()
        set2.Clear()

        print("""cycle""")
        
        iter-=1
        


if __name__ == "__main__":
    main()
