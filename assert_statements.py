# assert [condition], [error message]

def palindrome(string):
    assert len(string) > 0, "No se puede ingresar una cadena vacía"
    return string == string[::-1]


print(palindrome(""))