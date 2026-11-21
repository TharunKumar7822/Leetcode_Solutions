from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = [-1] * 100001
        
        for w, l in matches:
            if losses[w] == -1:
                losses[w] = 0
            if losses[l] == -1:
                losses[l] = 1
            else:
                losses[l] += 1
                
        zero_loss = []
        one_loss = []
        for player in range(1, 100001):
            if losses[player] == 0:
                zero_loss.append(player)
            elif losses[player] == 1:
                one_loss.append(player)
                
        return [zero_loss, one_loss]