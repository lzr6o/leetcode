class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        res = True
        for bit in bits[-2::-1]:
            if bit: res = not res
            else: break
        return res