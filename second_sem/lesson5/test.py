import re

main_text = (
    "Jdsjksdh sdjldsdsk djdskl lol@m.ru  dskldsnlk"
    "Lolodsl ddhhd lo2@ma.ru"
    "fkldlkdf kldflkdf fkfkfk@n.ru dksldsk"
    "lololdo@ndnd.com kmldskldslmk dskdkm"
    "kek@m.uk djdjdj dk"
)

email_reg = r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)'
result = re.findall(email_reg, main_text)
print(result)
print(list(filter(lambda x: x.endswith('ru'), result)))


mul = lambda x: (lambda y: y * x)
times4 = mul(4)
print(times4(2))