"""
The following text is encrypted with an ancient encryption method called the `Caesar Cipher`.
Can you restore the original text?
Hints: Upper/lowercase does not matter. Nothing was done to punctuations.

Details of Caesar cipher:
https://en.wikipedia.org/wiki/Caesar_cipher
"""
encrypted_text = "CnwbxaOuxf rb jw nwm-cx-nwm xynw bxdaln yujcoxav oxa vjlqrwn unjawrwp. Rc qjb j lxvyanqnwbren, oungrkun nlxbhbcnv xo cxxub, urkajarnb jwm lxvvdwrch anbxdalnb cqjc uncb anbnjalqnab ydbq cqn bcjcn-xo-cqn-jac rw VU jwm mnenuxynab njbruh kdrum jwm mnyuxh VU yxfnanm jyyurljcrxwb."
key = 17

def decode_caesar(text, shift):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    text = text.lower()
    n = len(text)

    decoded_text = ""

    for i in range(n):
        character = text[i]
        if character in alphabets:
            location = alphabets.find(character)
            new_location = (location + shift) % 26
            decoded_text += alphabets[new_location]
        else:
            decoded_text += character
    return decoded_text
print(decode_caesar(encrypted_text,key))
