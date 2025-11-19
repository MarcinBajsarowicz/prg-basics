def f(text):
    result = "" 
    for char in text[0:-1]:
        result += char + "-"
    return result
    
print(f("University"))