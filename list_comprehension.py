# Advanced Python Lists
# Task 1: Creating a List of Squares using List Comprehension

n = 10

def squares(n):
    square = [i ** 2 for i in range(1, n + 1)]
    return square

print(squares(n))    

#Time Complexity: O(n)
# since we are iterating over each number from '1' to 'n' and computing the square of each number,
# each number takes constant time

# Space Complexity:
# We are creating a new list of size 'n, so space complexity is also O(n)



# Task 2: Merging Two Pre-sorted Lists

list1 = ["eggs", "bacon", "cheese"]
list2 = ["coffee", "pancakes"]


def merge_sorted_lists(list1, list2):
    merged_lists = []
    i, h = 0, 0 # two pointers to merge the two lists

    while i < len(list1) and h < len(list2):
        if list1[i] < list2[h]:
            merged_lists.append(list1[i])
            i += 1
        else:
            merged_lists.append(list2[h])
            h += 1
        #returning the elements at this point I found was returning only partially from the list examples

    merged_lists.extend(list1[i:])
    merged_lists.extend(list2[h:]) # best solution for finding any remaining unproccessed elements I googled
    return merged_lists

print(merge_sorted_lists(list1, list2))


# Time Complexity:
# Alogrithim processes both 'list1' and 'list2' just once. Time Complexity is
# O(m +n)

# Space Complexity:
# Creating a new list stores the merged results. All elements would be contained in the new list so
# Space Complexity is also O(m+n)

