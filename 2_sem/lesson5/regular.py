import re

main_text = (
    "Lol djdjnsknjsd djdj kek kdskd"
    "Loldmd jdjd kek kik kak"
    "lul lil djdj kok lol kek@m.ru"
    "\nlel"
)

email_reg = r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)'

result = re.match(r"l.l", main_text)
print(result)

result = re.search(r"l.l", main_text)
print(result.group())

result = re.findall(r"l.l", main_text)
print(result)

result = re.sub(r"l.l", '***', main_text)
print(result)

result = re.findall(email_reg, main_text)
print(result)
