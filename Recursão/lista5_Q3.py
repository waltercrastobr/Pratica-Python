def analisador_string(string_concat_variavel, nome_suspeito_variavel):
  if len(string_concat_variavel) < len(nome_suspeito_variavel):
    return False
  if string_concat_variavel[:len(nome_suspeito_variavel)] == nome_suspeito_variavel:
    return True
  return analisador_string(string_concat_variavel[1:], nome_suspeito_variavel)

nome_suspeito_fixo = input()
string_concat_fixo = input()

nome_suspeito_variavel = nome_suspeito_fixo.lower()
string_concat_variavel = string_concat_fixo.lower()

if analisador_string(string_concat_variavel, nome_suspeito_variavel) == True:
  print(f'Encontrei, o culpado é o {nome_suspeito_fixo}!')
elif analisador_string(string_concat_variavel, nome_suspeito_variavel) == False:
  print(f'Não era o {nome_suspeito_fixo}, tenho que continuar procurando.')
