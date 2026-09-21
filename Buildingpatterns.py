import re
text = "Contact us at support@example.com or admin@test.org"
redacted = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "[EMAIL HIDDEN]", text)
print(redacted)
names = "Doe, John; Smith, Alice; Brown, Bob"
converted = re.sub(r"(\w+),\s+(\w+)", r"\2 \1", names)
print(converted)
def double_number(match):
    num = int(match.group())
    return str(num * 2)
sentence = "I have 3 apples and 5 bananas."
doubled = re.sub(r"\d+", double_number, sentence)
print(doubled)
sample = "Wait!!! This is amazing!!! Really??"
collapsed, count = re.subn(r"([!?.,])\1+", r"\1", sample)
print(collapsed)
print("Replacements made:", count)
#Contact us at [EMAIL HIDDEN] or [EMAIL HIDDEN]
//#John Doe; Alice Smith; Bob Brown
#I have 6 apples and 10 bananas.
#Wait! This is amazing! Really?
#Replacements made: 3
