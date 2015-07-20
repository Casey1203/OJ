class Solution:

    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start)/2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1



    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if len(A) == 0:
            return [-1, -1]
        left = -1
        right = -1
        start = 0
        end = len(A) - 1
        while start + 1 < end:# find left bound
            mid = start + (end - start) / 2
            if A[mid] == target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            left = start
        elif A[end] == target:
            left = end
        start = 0
        end = len(A) - 1

        while start + 1 < end:# find right bound
            mid = start + (end - start) / 2
            if A[mid] == target:
                start = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            right = end
        elif A[start] == target:
            right = start
        
            
        return [left, right]

    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if len(A) == 0:
            return 0
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] > target or A[mid] == target:
                end = mid
            else:
                start = mid
        if A[end] < target:
            return len(A)
        elif A[start] > target or A[start] == target:
            return start
        else:
            return end
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) == 0:
            return False
        row = len(matrix)
        column = len(matrix[0])
        start = 0
        end = row - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                start = mid
            else:
                end = mid
        if matrix[end][0] <= target:
            row = end
        elif matrix[start][0] <= target:
            row = start
        else:
            return False

        start = 0
        end = column - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                end = mid
            else:
                start = mid
        if matrix[row][start] == target or matrix[row][end] == target:
            return True
        else:
            return False

    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix2(self, matrix, target):
        if len(matrix) == 0:
            return 0
        row = len(matrix)
        column = len(matrix[0])
        time = 0
        r = len(matrix) - 1
        c = 0
        while r >= 0 and c < column:
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else:
                time += 1
                r -= 1
                c += 1
        return time

    def findFirstBadVersion(self, n):
        # write your code here
        start = 1
        end = n
        while start + 1 < end:
            mid = start + (end - start) / 2
            if isBadVersion(mid) == True:
                end = mid
            else:
                start = mid
        if isBadVersion(start) == True:
            return start
        else:
            return end

    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        # write your code here
        if len(A) == 0:
            return 0
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
                start = mid
            elif A[mid] < A[mid-1] and A[mid] > A[mid+1]:
                end = mid
            else:
                start = mid
        if A[start] > A[start+1] and A[start] > A[start-1]:
            return start
        else:
            return end
            
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        # write your code here
        if len(A) == 0:
            return -1
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            if A[mid] >= A[0]:#left
                if target >= A[0] and target < A[mid]:
                    end = mid
                else:
                    start = mid
            else:#right
                if target > A[mid] and target <= A[len(A)-1]:
                    start = mid
                else:
                    end = mid
        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        else:
            return -1




    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # write your code here
        if len(num) == 0:
            return 0
        start = 0
        end = len(num) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if num[mid] >= num[end]:
                start = mid
            else:
                end = mid
        return min(num[start], num[end])

    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        if len(A) == 0:
            return B
        elif len(B) == 0:
            return A
        i = 0
        j = 0
        C = []
        m = len(A)
        n = len(B)
        while i < m and j < n:
            if A[i] < B[j]:
                C.append(A[i])
                i+=1
            elif A[i] > B[j]:
                C.append(B[j])
                j+=1
            else:
                C.append(A[i])
                C.append(B[j])
                i+=1
                j+=1
        if i < m:
            C.extend(A[i:])
        elif j < n:
            C.extend(B[j:])
        return C
    def reverse(self, nums, i, j):
        tmp = nums[i:j]
        for index in range(len(tmp)):
            nums[i+index] = tmp[len(tmp) - 1- index]
        
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if len(nums) == 0:
            return []
        drop_down = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i-1]:
                drop_down = i
                break
        self.reverse(nums, 0, i)
        self.reverse(nums, i, len(nums))
        self.reverse(nums, 0, len(nums))


    
def isBadVersion(id):
    return A[id]


A=[4,5,1,2,3]
s = Solution()
print s.recoverRotatedSortedArray(A)
