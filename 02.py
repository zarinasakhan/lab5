import re
pattern='ab{2,3}'
text_to_match='abbbb'
result=re.match(pattern, text_to_match)
print(result)