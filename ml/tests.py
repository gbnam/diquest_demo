from konlpy.tag import Kkma, Twitter

# sentence = ['안녕하세요', '저는 김호근입니다', '반갑습니다']
# keyword = ['안녕', '저는', '김호근']
# print(sentence)
# print(keyword)

_kkma = Kkma()
_twt = Twitter()
text = "안녕하세요 저는 김호근 입니다."

print(text)
print(_kkma.nouns(text))
print(_twt.nouns(text))
