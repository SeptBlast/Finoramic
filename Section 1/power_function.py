#
#  Exam Link: https://www.interviewbit.com/problems/implement-power-function/
#
#   Question:
#   
#    Implement pow(x, n) % d.
#
#   In other words, given x, n and d,
#
#   find (xn % d)
#
#   Note that remainders on division cannot be negative. 
#   In other words, make sure the answer you return is non negative.
#
#   Input : x = 2, n = 3, d = 3
#   Output : 2
#
#   2^3 % 3 = 8 % 3 = 2.
#   
#   Algorithm:
#   Written By: Devesh Kumar
#   Submission Details in Image: Power_function.png
#

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        res = 1
        base = x%d
        while n>0:
            if n%2 ==1:
                res = (res*base)%d
            
            n = n>>1
            base = (base*base)%d
            
        return res%d
