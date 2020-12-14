#!/usr/bin/env python
# coding: utf-8

__author__      = "Nadeem Nazeer"


"""
Solution 1: The simplest solution: Sort the list in ascending order(with one of the sorting algorithms ) 
and return the k-1 (k-th smallest/largest element). The time complexity is O(n*log(n)) - 
as that is what most sorting algorithms take. 

Solution 2: The issue with solution 1 is that we are not looking to sort everything - that was not the problem 
at hand - but we want to find what sits at kth position. So better solution is we just stop when we reach 
at kth position - and thus we can use algos 
like min/max heap select to do this - which has complexity of O(n*log(k)). 

Solution 3 (quickSelect):The best solution is we select the Pivot element and then use partitioning algorithm to find 
the correct position of pivot and arrange the remaining elements on left(elements < pivot)/right(elements > pivot),
select the partition which has k-1th index and and do the same for that. The ideal implementations of this solution
has time complexity is O(n).

"""
def quick_select(ls,k):
    '''
    Returns the kth-smallest element.

            Parameters:
                    ls (list): list of elements
                    k (int): kth-element to found

            Returns:
                    (int): kth element
    '''
    pivot = ls[0] # Select first element as pivot - there are better pivot selection algorithms.
    pivot_part = [pivot]
    left_part = []
    right_part = []
    try:

        for element in ls[1:]:
            if element < pivot: 
                left_part.append(element)
            elif element > pivot:
                right_part.append(element)
            else:
                pass
        if k <= len(left_part):
            return quick_select(left_part,k)
        elif k > len(left_part)+len(pivot_part):
            return quick_select(right_part,k-len(left_part)-len(pivot_part))
        else:
            return pivot
    except Exception as e:
        print("We aren't handling all inputs :(",e)


import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script to get the kth-smallest element')

    parser.add_argument('--list',type=str,help='A comma separated list of integers.', required=True)
    parser.add_argument('--kth',type=int, help='kth element to find', required=True)

    arguments = parser.parse_args()
    ls = arguments.list
    k = arguments.kth
    #ls = [1,6,4,2,3]
    print(quick_select (ls.split(","), k))
