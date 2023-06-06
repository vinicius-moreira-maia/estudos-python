import re

def main():
    ass = le_assinatura()
    textos = le_textos()
    texto_infectado = avalia_textos(textos, ass)

    print(f"O autor do texto {texto_infectado} está infectado com COH-PIAH")


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    ass = []

    for i in range(len(as_a)):
        ass.append(abs(as_a[i] - as_b[i]))
    
    soma = sum(ass)

    return soma / 6


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    suspeitos = []

    for texto in textos:
        ass_texto = calcula_assinatura(texto)
        res_comparacao = compara_assinatura(ass_texto, ass_cp)
        suspeitos.append(res_comparacao)
    
    indice_infectado = suspeitos.index(min(suspeitos))

    return indice_infectado + 1
    

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    assinatura = []

    sentencas = separa_sentencas(texto)
    frases = get_frases(sentencas)
    palavras = get_palavras(frases)

    tmp = tam_medio_palavras(palavras)
    assinatura.append(tmp)
    rtt = rel_type_token(palavras)
    assinatura.append(rtt)
    rhl = razao_hapax_legomana(palavras)
    assinatura.append(rhl)
    tms = tam_medio_sentenca(sentencas)
    assinatura.append(tms)
    cs = complexidade_sentenca(frases, sentencas)
    assinatura.append(cs)
    tmf = tam_medio_frase(frases)
    assinatura.append(tmf)

    return assinatura
    
# início das funções implementadas por mim

def get_frases(sentencas):
    frases = []

    for sentenca in sentencas:
        frases.extend(separa_frases(sentenca))
    
    return frases


def get_palavras(frases):
    palavras = []

    for frase in frases:
        palavras.extend(separa_palavras(frase))
    
    return palavras


def tam_medio_palavras(palavras):
    n_palavras = len(palavras)
    
    soma = 0

    for palavra in palavras:
        soma += len(palavra)
    
    return soma / n_palavras


def rel_type_token(palavras):
    return n_palavras_diferentes(palavras) / len(palavras)


def razao_hapax_legomana(palavras):
    return n_palavras_unicas(palavras) / len(palavras)


def tam_medio_sentenca(sentencas):
    soma = 0

    for sentenca in sentencas:
        for _ in sentenca:
            soma += 1
    
    return soma / len(sentencas)


def complexidade_sentenca(frases, sentencas):
    return len(frases) / len(sentencas)


def tam_medio_frase(frases):
    soma = 0

    for frase in frases:
        for _ in frase:
            soma += 1
    
    return soma / len(frases)

# fim das funções implementadas por mim
    

if __name__ == '__main__':
    main()