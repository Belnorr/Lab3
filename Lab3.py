print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    if n>=10:
        print("List is too long 10 or more uin the list")
        return 1
    
    if n ==0:
        print("List is empty")
        return 0
    
    if n<10:
        for eachnum in arr_result:
            if isinstance(eachnum, int) == False:
                print("Not all number in this are integer")
                return 2
            
    if n < 10:
        # Traverse through all array elements
        for i in range(n - 1):
            # range(n) also work but outer loop will
            # repeat one time more than needed.

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                if sorting_order == SORT_ASCENDING:
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]


                elif sorting_order == SORT_DESCENDING:
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                else:
                    # Return an empty array
                    arr_result = []
    else:
        arr_result = -1

    return arr_result

def main():
    # Driver code to test above
    #rr = [64, 34, 25, 12, 22, 11, 90, 100, 200, 300, 400]
    #rr = [64, 34, 25, 12, 22, 11, 90]
   #arr = []
    arr = [64, 34, 25, 12, 22, 11, "bababa"]
    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)

if __name__ == "__main__":
    main()


