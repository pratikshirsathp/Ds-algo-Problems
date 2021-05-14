
"""Maximum and minimum of an array using minimum number of comparisons"""
def getMinMax(arr):

    n = len(arr)

    # even no. of array elements 
    if (n % 2 == 0):
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])
        i = 2
    # odd
    else:
        mx = mn = arr[0]
        i = 1

    # In the while loop, pick elements in pair and
    # compare the pair with max and min so far
    while (i < n - 1):
        if arr[i] < arr[i + 1]:
            mx = max(mx, arr[i + 1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i + 1])

        # Increment the index by 2 as two
        # elements are processed in loop
        i += 2

    return (mx, mn)


# Driver Code
if __name__ == '__main__':

    arr = [1000, 11, 445, 1, 330, 3000]
    mx, mn = getMinMax(arr)
    print("Minimum element is", mn)
    print("Maximum element is", mx)
