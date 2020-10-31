# 민채

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp =dict()
        for s in strs:
            '''
            s : original 단어
            temp_s : 알파벳 순으로 정렬된 단어
            '''
            temp_s = ''.join(sorted(s))
            if temp_s in list(temp.keys()):
                temp[temp_s].append(s)
            else:
                temp[temp_s] =[s]
                
        answer = []
        for i in temp.keys():
            answer.append(temp[i])
        
        # answer = sorted(answer, key=lambda x : len(x))
        return answer