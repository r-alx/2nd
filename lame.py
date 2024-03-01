#write a function that receives a string and  put each character of string in list.#

def raw(txt):
    chrs = []
    for ch in txt:
        chrs.append(ch)
    return chrs


out = raw("we are learning python")
print(out)