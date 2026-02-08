import itertools

digits = ['1', '7', '9', '0']
required = set(digits)

valid_codes = []

for combo in itertools.product(digits, repeat=6):
    code = ''.join(combo)
    if set(code) >= required: 
        valid_codes.append(code)

print(f"Total valid codes: {len(valid_codes)}")
for c in valid_codes:
    print(c)