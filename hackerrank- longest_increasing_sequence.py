def longestIncreasingSubsequence(arr):
    info_list = [(1, arr[0])]
    for i in range(1, len(arr)):
        current_value = arr[i]
        # print ("processing value: ", current_value)
        seq_count = 1
        for index, (count_till_prev, prev_value) in enumerate(info_list):
            # print("\tprocessing the element: ", info_list[index])
            if current_value > prev_value:
                #print("here")
                seq_count = count_till_prev + 1
                if index == 0:
                    info_list.insert(index, (seq_count, current_value))
                    # print("inserting at index: ", index, "the count of ", seq_count)
                    break
                else:
                    info_list[index - 1] = (seq_count, current_value)
                    # print("updating at index: ", index, "the count of ", seq_count)
                    break
        if seq_count == 1:
            info_list[-1] = (seq_count, current_value)
            # print("updating the last element to the count of ", seq_count)
            # print("no. is bigger")

        # print(info_list)

    return info_list[0][0]

arr = [9, 7, 5, 4, 18, 19, 10, 11, 14, 15]
# arr = [2, 7, 4, 3, 8]

print(longestIncreasingSubsequence(arr))