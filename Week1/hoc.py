import re
text = "Salve mundi. Hoc est scribitus."
result = re.split(r'([,.]\s)', text)
print(result)
