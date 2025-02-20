import re
pattern='[a-z]+_[a-z]+'
text_to_match='abb_bb abc_ fg'
result=re.findall(pattern, text_to_match)
print(result)