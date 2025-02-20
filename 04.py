import re
pattern='[A-Z][a-z]+'
text_to_match='Adel AAsel arman'
result=re.findall(pattern, text_to_match)
print(result)