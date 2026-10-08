import re

text = "Invoice: 105. The products cost Rs. 5000, 1,250 and Rs 12,500."

currency_pattern = r'(?:Rs\.?\s*|₹\s*)\d+(?:,\d{3})*|\b\d{1,3}(?:,\d{3})+\b'

values = re.findall(currency_pattern, text)

print("Currency values found:")

for value in values:
    print(value)
