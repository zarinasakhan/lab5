import re
pattern='[ ,.]'
text_to_match='Hello, World.'
result=re.sub(pattern, ":", text_to_match.strip())
print(result)