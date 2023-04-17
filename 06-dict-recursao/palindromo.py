def main():
    test_pal()
    
def is_palindrome(s):

    def to_chars(s):
        s = s.lower()
        letters = ''

        for c in s:
            if c.isalpha():
                letters += c
        
        return letters
    
    def is_pal(s):
        if len(s) <= 1:
            print("  retornando True do caso base  ")
            return True
        else:
            # a cada chamado um slice menor é passado como parâmetro
            res = s[0] == s[-1] and is_pal(s[1:-1])
            print(f"  retornando {res} para {s}  ")
            return res
    
    return is_pal(to_chars(s))

def test_pal():
    print(is_palindrome("dogood"))

if __name__ == "__main__":
    main()