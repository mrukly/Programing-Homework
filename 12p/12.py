def search(a, x):
    """
    Check if a given number x exists in the list a

    Parameters:
    a (list): A list of integers
    x (int): The number to search for

    Returns:
    int: 1 if x is found in the list, otherwise 0
    """
  
    if len(a) == 0:
        return 0
    
    if a[0] == x:
        return 1
    
    return search(a[1:], x)

nums = list(map(int, input().split()))
x = int(input())
print(search(nums, x))
