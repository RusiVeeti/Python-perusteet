nmr=['1','7','9','0']
pit=6
def generate(kood):
    if len(kood)==pit:
        if '1' in kood and '7' in kood and '9' in kood and '0' in kood:
            print(kood)
        return
    for m in nmr:
        generate(kood+m)
generate("")