import re
pattern='ab*'
text_to_match='abbb'
result=re.match(pattern, text_to_match)
print(result)
