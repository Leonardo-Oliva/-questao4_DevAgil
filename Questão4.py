def encryptThis(message):
    """
    Criptografa uma palavra seguindo as regras citadas abaixo:

    A mensagem é uma string contendo palavras separadas por espaços.

    Cada palavra na mensagem deve ser criptografada da seguinte maneira:

    O primeiro caractere da palavra deve ser convertido para o seu código ASCII.

    O segundo caractere da palavra deve ser trocado com o último caractere.

    A função deve retornar a mensagem criptografada, mantendo a mesma estrutura de palavras separadas por espaços.
    """
    words = message.split()
    result = []
    for word in words:
        if len(word) == 0:
            result.append('')
        else:
            first_char = str(ord(word[0]))
            if len(word) == 1:
                result.append(first_char)
            else:
                encrypted_word = first_char + word[-1] + word[2:-1] + word[1]
                result.append(encrypted_word)
    return ' '.join(result)
    

# Testes Unitários
def teste_encryptThis():
    # Teste para palavra de cinco letras
    assert encryptThis("Hello") == '72olle'
    print()

    # Teste para palavra de quatro letras
    assert encryptThis("good") == '103doo'

    # Teste para frase com duas palavras
    assert encryptThis("hello world") == '104olle 119drlo'

    # Teste para palavra vazia
    assert encryptThis("") == ''

    # Teste para palavra de uma letra
    assert encryptThis("a") == '97'

# Executando os testes unitários se este arquivo for executado diretamente
if __name__ == '__main__':
    teste_encryptThis()
    print("Todos os testes passaram com sucesso")