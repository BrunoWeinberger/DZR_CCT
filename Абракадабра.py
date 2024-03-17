string = 'аоыгСпДЕыйччЛавывсАаЛ ДвыотЕпотоЛмучфО - ГпайУтонЛвеселЯЙ СыйМявапкЕиудывЛО'
print(string)
result: str = ""
for s in string:
    if not s.islower():
        result = result + s
print(result)
