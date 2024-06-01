def search(arr, num, limits):
    half_index = (limits[0] + limits[1]) // 2
    if limits[1] - limits[0] == 0:
        return half_index if (arr[half_index][1] < num) else half_index + 1

    if limits[1] - limits[0] == 1:
        if num > arr[half_index][1]:
            return half_index
        return half_index + 1 if (arr[half_index + 1][1] < num) else half_index + 2

    if arr[half_index][1] == num:
        return half_index
    if arr[half_index][1] < num:
        return search(arr, num, (limits[0], half_index-1))
    else:
        return search(arr, num, (half_index+1, limits[1]))

arr = [(2,12), (1,9)]

# arr = [(5, 15), (4, 14), (3, 11), (2, 10), (1, 4)]
# print(search(arr,8, (0, len(arr)-1)))






def longestIncreasingSubsequence(arr):
    info_list = [(1, arr[0])]
    for i in range(1, len(arr)):
        print(info_list)
        current_value = arr[i]
        print ("processing value: ", current_value)
        seq_count = 1
        index = search(info_list, current_value, (0, len(info_list)-1))
        if index == len(info_list):
            info_list[- 1] = (seq_count, current_value)
            continue
        print("index = ",index)
        seq_count = info_list[index][0] + 1
        if index == 0:
            info_list.insert(index, (seq_count, current_value))
            print("inserting at index: ", index, "the count of ", seq_count)
        else:
            info_list[index - 1] = (seq_count, current_value)
            print("updating at index: ", index, "the count of ", seq_count)



    return info_list[0][0]

arr = [9, 7, 5, 4, 18, 19, 10, 11, 14, 15]
# arr = [2, 7, 4, 3, 8]
print(longestIncreasingSubsequence(arr))
