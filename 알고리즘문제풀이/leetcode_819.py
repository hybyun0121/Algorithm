# 민채
class Solution:
    import re
    from collections import Counter
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 문자와 숫자가 아니면 삭제하고 문자는 소문자 변환 그리고 리스트로 분리
        words = re.sub('[^\w]',' ',paragraph).lower().split()
        # banned 안에 포함되지 않는 것들만 필터링
        words = filter(lambda x: x not in banned, words)
        # Counter로 단어별 수 세기
        counter = Counter(words)
        # 가장 많이 나온 단어 리턴
        return counter.most_common(1)[0][0]

# HY
from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-zA-Z]+',' ', paragraph)
        word_list = paragraph.split(' ')
        word_dict = Counter(word_list)
        word_dict = sorted(word_dict.items(), key = lambda x:x[1], reverse=True)
        for w, _ in word_dict:
            if not w in banned and w is not "":
                return w

# jh
import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-zA-Z0-9]', ' ', paragraph).split()
        cnt = dict(Counter(paragraph))

        for key, _ in sorted(cnt.items(), key=lambda x: x[1], reverse=True):
            if key not in banned:
                return key