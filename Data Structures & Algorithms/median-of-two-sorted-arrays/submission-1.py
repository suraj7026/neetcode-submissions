class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A , B = nums1, nums2
        total = len(nums1) +len(nums2)
        half = total //2
        if len(A) > len(B):
            A,B = B,A
        
        l,r = 0, len(A) -1
        while True:
            ma = (l+r)//2
            mb = half - ma -2

            Aleft = A[ma] if ma >= 0 else float("-inf")
            Aright = A[ma + 1] if (ma+1) < len(A) else float("inf")
            Bleft =  B[mb] if mb >= 0 else float("-inf")
            Bright = B[mb + 1] if (mb+1) < len(B) else float("inf")

            if Aleft <= Bright and Aright >= Bleft: 
                if total % 2 == 0:
                    return (max(Aleft,Bleft) + min(Aright,Bright)) /2
                else:
                    return min(Aright,Bright)
            elif Aleft > Bright:
                r = ma - 1
            else:
                l = ma + 1

        