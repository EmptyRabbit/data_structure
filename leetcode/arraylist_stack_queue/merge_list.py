class Solution:
    """
    #88
    """

    def merge(self, A, m: int, B, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            A[:] = B[:]
            return A
        if n == 0:
            return A

        i, j = 0, 0
        while i < len(A) and j < n:
            if A[i] <= B[j]:
                i += 1
            else:
                A[i + 1:] = A[i:-1]
                A[i] = B[j]
                i += 1
                j += 1

        if i == len(A) and j < n:
            A[-(n - j):] = B[j:]

        return A


a = Solution()
result = a.merge([1, 2, 3, 0, 0, 0], 3, [1, 4, 6], 3)
print(result)
