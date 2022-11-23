import numpy as np
import pandas as pd

#utf-8의 인코딩으로는 한글이 깨져서 cp949로 인코딩합니다. 
df = pd.read_csv("extract.csv", encoding = 'cp949' )

def text_preprocessor(s):
  import re
  ## (2) puncuation 제거
  s = re.sub(r'[@%\\*=()/~#&\+á?\xc3\xa1\-\|\.\:\;\!\-\,\_\~\$\'\"]', repl=' ',string = s)

  # (4) 공백 삭제하기
  s = re.sub(r'\s+', ' ', s) #remove spaces
  s = re.sub(r"^\s+", '', s) #remove space from start
  s = re.sub(r'\s+$', '', s) #remove space from the end

  # (5) 리스트에 추가하기
  s_list = []
  s_list.append(s)          
  return s

# 전처리를 해서 나온 단어들을 특이사항list라는 새로운 열에 추가
df["특이사항list"] = df["특이사항"].apply(lambda s : text_preprocessor(s))

