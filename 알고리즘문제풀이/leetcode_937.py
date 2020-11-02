# 민채

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # let, dig을 구분할 리스트 생성
        temp_let = []
        temp_dig = []
        for log in logs:
            
            temp = log.split()
            temp = ' '.join(temp[1:])
            # identifier 다음에 숫자가 오는지 확인 후 맞으면 dig 아니면 let
            if temp[0].isdigit(): 
                temp_dig.append(log)
            else:
                temp_let.append(log)
        # 정렬
        temp_let.sort()
        temp_let.sort(key = lambda x: x.split()[1:])
        return temp_let + temp_dig

# HY
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        output = []
        digs = []
        for i in range(len(logs)):
            try:
                int(logs[i].split(' ')[1])
                digs.append(logs[i])
            except:
                output.append(logs[i])
        output.sort(key=lambda x: x.split(' ')[1:])
        return output + digs


