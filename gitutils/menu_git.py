import git_functions

print("Menu de opções Git\n")
print('P -Lote de comandos, "add .", "Commit","Checkout main","rebase","Push origin main"')
print('G - Get branch')

selecao = input("Digite sua opção: ").upper()

if selecao == "P":
    comentario_commmit = input("Digite mensagem de commit: ")
    git_functions.push_batch(comentario_commmit)
elif selecao == "G":
    print(git_functions.get_branch())
