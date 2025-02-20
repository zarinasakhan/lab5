import re
pattern='.+'
text_to_match='snake_case'

def repl(match):
    word=str(match.group(0))
    res=''
    upperdo=False
    for i in range (len(word)):
        if word[i]=="_":
            upperdo=True
        else:
            if (upperdo):
                res+=word[i].upper()
                upperdo=False
            else:
                res+=word[i]
    return res

result=re.sub(pattern, repl, text_to_match.strip())
print(result)