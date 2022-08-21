def bin_search(lst,search_term):
    """ A simple binary search proc which searches a term within a list 
    it returns -1 if not found. This has O logn time complexity"""
    low,high =0,len(lst)-1
    while low<=high:
        mid = (low+high)//2
        if lst[mid] == search_term:
            return mid
        elif lst[mid] > search_term:
            high = mid -1 
        elif lst[mid] < search_term:
            low = mid + 1
    return -1


if __name__  == "__main__":
    inp_array = [2,3,4,10,40]
    print(bin_search(inp_array,2))
    print(bin_search(inp_array,10))
    print(bin_search(inp_array,41))
    print(bin_search(inp_array,40))

