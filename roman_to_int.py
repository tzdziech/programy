#konwercja rzymskich na arabskie

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        last = "0"
        for enum in s:
            if enum == "I":
                count += 1
            elif enum == "V":
                count += 5
                if last == "I":
                    count -= 2
            elif enum == "X":
                count += 10
                if last == "I":
                    count -= 2
            elif enum == "L":
                count += 50
                if last == "X":
                    count -= 20
            elif enum == "C":
                count += 100
                if last == "X":
                    count -= 20
            elif enum == "D":
                count += 500
                if last == "C":
                    count -= 200
            elif enum == "M":
                count += 1000
                if last == "C":
                    count -= 200
            last = enum
        return count

    
"MCMXCIV"

+1000
+100
+100