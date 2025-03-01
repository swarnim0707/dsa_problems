# Longest Increasing subsequence problem leveraging a hash map + dynamic programming hybrid
# Time complexity: O(n log n) to O(n√n)
# Space complexity: O(n)

# This is an improvement of the conventional DP approach by using a dictionary to keep track of all the elements belonging to a particular score. From the nature of how the elements are appended, the list of each score has its elements in the descending order always, making it easier to search for the right score for any given element.

def lis(self, arr):
        score_dict = defaultdict(list)
        lis_arr = [1]*len(arr)
        max_score = 1
        score_dict[1].append(arr[0])
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                key = lis_arr[i-1] + 1
                while(True):
                    if not score_dict[key]:
                        score_dict[key].append(arr[i])
                        break
                    else:
                        if score_dict[key][-1] < arr[i]:
                            key += 1
                        else:
                            score_dict[key].append(arr[i])
                            break
                lis_arr[i] = key
            else:
                key = lis_arr[i-1]
                while(key > 0):
                    if(score_dict[key] and (score_dict[key][-1] >= arr[i])):
                        key -= 1
                    else:
                        break
                key += 1
                score_dict[key].append(arr[i])
                lis_arr[i] = key  
            max_score = max(max_score, lis_arr[i])
        # print(lis_arr)
        # print(arr)
        return max_score
