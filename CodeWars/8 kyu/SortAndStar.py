def two_sort(array):
    array.sort()
    return '***'.join(list(array[0]))
print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))