import re
pattern = re.compile(r'\W+')
def LongestWord(sen):
  # code goes here
    x = pattern.split(sen)
    return max(x, key=len)
    
# keep this function call here  
print(LongestWord(input()))
