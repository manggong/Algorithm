def same_name(text):
    result = set()
    for i in range(0,len(text)-1):
        for j in range(1,len(text)):
            if text[i] == text[j]:
                result.add(text[i])
    return result




text1 = ["a","b","c","c","a"]
text2 = ["a","a","b","b","c"]

print(same_name(text1))