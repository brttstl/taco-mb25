## BUBBLESORT(A)
def bubbleSort(A):
    # 1 for i = 1 to A.length - 1
    for i in range(len(A) - 1):
        # 2 for j = A.length downto i + 1
        for j in range(len(A) - 1, i, -1):
            # 3 if A[j] < A[j - 1]
            if (A[j] < A[j - 1]):
                # 4 exchange A[j] with A[j - 1]
                A[j], A[j - 1] = A[j - 1], A[j]

## INSERTION-SORT(A)
def insertSort(A):
    # 1 for j = 2 to A.length
    for j in range(len(A)):
        # 2 key = A[j]
        temp = A[j]
        # 3 // Insert A[j] into the sorted sequence A[1 .. j - 1].
        # 4 i = j - 1
        i = j - 1
        # 5 while i > 0 and A[i] > key
        while ((i > 0) & (A[i] > temp)):
            # 6 A[i + 1] = A[i]
            A[i + 1] = A[i]
            # 7 i = i - 1
            i = i - 1
            # 8 A[i + 1] = key
            A[i + 1] = temp