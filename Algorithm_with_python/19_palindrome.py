def palindrome(s):

  qu = []
  st = []

  for i in s:
    if i.isalpha(): # 문자열인지 아닌지 체크
      qu.append(i.lower())
      st.append(i.lower())

  while qu:
    if qu.pop(0) != st.pop():
      return False

  return True


print(palindrome("Hello"))

print(palindrome("wow"))