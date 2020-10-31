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

# jh
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp_dict = {}
        answer = []
        flag = [False] * len(strs)

        # 딕셔너리 생성
        for idx, str in enumerate(strs):
            tmp_dict[idx] = [str, Counter(str)]

        for i in range(0, len(tmp_dict.keys())):

            if flag[i] == True :
                continue
            flag[i] = True
            tmp = [tmp_dict[i][0]]
            for j in range(i+1, len(tmp_dict.keys())):
                if flag[j] == True :
                    continue
                if tmp_dict[i][1] == tmp_dict[j][1]:
                    flag[j] = True
                    tmp.append(tmp_dict[j][0])
            answer.append(list(tmp))

        # for i in range(len(answer)) :
        #     answer[i] = sorted(answer[i], reverse=False)

        answer = sorted(answer, key=lambda x : len(x))

        return answer

# HY
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = dict()
        for s in strs:
            key = ''.join(sorted(s))
            if key in list(_dict.keys()):
                _dict[key].append(s)
            else:
                _dict[key] = [s]

        return list(_dict.values())
