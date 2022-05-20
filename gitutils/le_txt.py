def get_emoji(numero_linha):
    ref_arquivo = open("gitutils/emojis.txt", "r", encoding="utf8")
    
    lista_de_emojis = ref_arquivo.readlines()
    ref_arquivo.close()
    emoji_atual = lista_de_emojis[int(numero_linha)]
    return emoji_atual


def get_branch_atual():
    arquivo_branch_atual = open("gitutils/branch_atual.txt", "r")
    branch_atual = arquivo_branch_atual.readlines()
    # print(int(branch_atual[0]))
    arquivo_branch_atual.close()
    return branch_atual[0]


def set_branch_atual(numero_linha):
    with open('gitutils/branch_atual.txt', 'w') as arquivo:
        arquivo.write(str(numero_linha))
        arquivo.close()
        return
