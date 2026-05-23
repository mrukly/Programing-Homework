def odd_list(a, n):
    """
    Recursively returns a list of even numbers from the given list

    Parameters:
    a (list): A list of integers
    n (int): The number of elements in the list (length of a)

    Returns:
    list: A new list containing only the even values from a
    """
    if n == 0:
        return []
    
    result = odd_list(a, n - 1)
    
    if a[n - 1] % 2 == 0: 
        result.append(a[n - 1])
    
    return result


nums = list(map(int, input("Enter integers separated by spaces: ").split()))
n = len(nums)

print(odd_list(nums, n))
