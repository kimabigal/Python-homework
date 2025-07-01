def merge_lists(list1, list2):
    return list1 + list2

list1 = input("Enter your first list: ").split()
list2 = input("Enter your second list: ").split()

print("Your combined list:", merge_lists(list1, list2))