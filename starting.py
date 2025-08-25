
from bancojson import BancodeMaterias

banco = BancodeMaterias()

while True:
    print("\n--- MENU ---")
    opcao = input(
        "1 - Adicionar matéria\n"
        "2 - Adicionar nota AV\n"
        "3 - Adicionar nota Simulado\n"
        "4 - Listar matérias\n"
        "5 - Fechar\n"
    )

    match opcao:
        case "1":
            nome = input("Nome da matéria: ")
            banco.adicionar_materia(nome)

        case "2":
            nome = input("De qual matéria deseja adicionar a AV? ")
            nota = float(input("Nota da AV: "))
            banco.adicionar_nota_av(nome, nota)

        case "3":
            nome = input("De qual matéria deseja adicionar o Simulado? ")
            nota = float(input("Nota do Simulado: "))
            banco.adicionar_nota_simulado(nome, nota)

        case "4":
            banco.listar()

        case "5":
            print("Saindo...")
            break