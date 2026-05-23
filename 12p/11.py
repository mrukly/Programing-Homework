def ind_maxlist(a):
    """
    Finds the index of the first maximum element in a list

    Parameters:
    a (list): A list of integers (non-empty)
    start_index (int): Current starting index for the sublist (default 0)

    Returns:
    int: The index of the first maximum element in the list
    """
    if len(a) == 1:
        return 0
    
    index = ind_maxlist(a[1:])
    
    max = a[index + 1]
    
    if a[0] >= max:
        return 0
    else:
        return index + 1

nums = list(map(int, input().split()))
print(ind_maxlist(nums))
