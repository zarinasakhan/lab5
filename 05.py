import re
pattern='a.*b$'
text_to_match='askarb'
result=re.match(pattern, text_to_match)
print(result)