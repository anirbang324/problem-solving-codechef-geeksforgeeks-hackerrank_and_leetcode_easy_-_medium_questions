# problem's link : https://leetcode.com/problems/robot-return-to-origin/description/

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        for move in moves:
            if move=='U':
                y+=1
            elif move=='R':
                x+=1
            elif move=='D':
                y-=1
            elif move=='L':
                x-=1
        return x==0 and y==0


s = Solution()
moves = input().upper()
# print(moves)
answer = s.judgeCircle(moves)
print(answer)