import re
text_to_match='WelcomeToAlmaty'
pattern="[A-Z][^A-Z]*"
res=re.findall(pattern,text_to_match)
print(res)



