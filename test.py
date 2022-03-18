def test(a:str, b:str):
    assert len(b)==1, "ya fucked up, too many letters in b"
    i = 0
    ### iterates the i variable
    while i<len(a):
        if a[i] == b[0]: ### the b[i] will throw an error because b has only 1 char (i out of range error)
            ### also, made the code run with `if` instead of `if not` for clarity (no double negative)
            return True
        else:
            i+=1 ### iterates
    return False ### if the entire while statement runs and no match, return false
            

print(len('12345'))