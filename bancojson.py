import json
import os

class Materia:
    def __init__(self, nome, nota_av=0, nota_simulado=0):
        self.nome = nome
        self.nota_av = nota_av
        self.nota_simulado = nota_simulado

    def calcular_final(self):
        return self.nota_av + self.nota_simulado
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "nota_av": self.nota_av,
            "nota_simulado": self.nota_simulado
        }
    
    def from_dict(data):
        return Materia(
            nome=data["nome"],
            nota_av=data.get("nota_av", 0),
            nota_simulado=data.get("nota_simulado", 0)
        )
    
class BancodeMaterias:
    def __init__(self, arquivo="Matérias.json"):
        self.arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), arquivo)
        self.materias = []
        self.carregar()
    
    def adicionar_materia(self, nome):
        if self.buscar_materia(nome) is None:
            self.materias.append(Materia(nome))
            self.salvar()
            print("✅ Matéria adicionada com sucesso!")
        else:
            print("⚠️ Essa matéria já existe.")

    def buscar_materia(self, nome):
        for m in self.materias:
            if m.nome == nome:
                return m
        return None

    def adicionar_nota_av(self, nome, nota):
        materia = self.buscar_materia(nome)
        if materia:
            materia.nota_av = nota
            self.salvar()
            print("✅ Nota AV adicionada!")
        else:
            print("⚠️ Matéria não encontrada.")

    def adicionar_nota_simulado(self, nome, nota):
        materia = self.buscar_materia(nome)
        if materia:
            materia.nota_simulado = nota
            self.salvar()
            print("✅ Nota de simulado adicionada!")
        else:
            print("⚠️ Matéria não encontrada.")

    def listar(self):
        if not self.materias:
            print("Nenhuma matéria cadastrada ainda.")
            return
        print("\n📊 MATÉRIAS CADASTRADAS:")
        for m in self.materias:
            print(f"- {m.nome}: AV={m.nota_av}, Simulado={m.nota_simulado}, Final={m.calcular_final()}")

    def salvar(self):
        with open(self.arquivo, "w") as f:
            json.dump([m.to_dict() for m in self.materias], f, indent=4)

    def carregar(self):
        try:
            with open(self.arquivo, "r") as f:
                data = json.load(f)
                self.materias = [Materia.from_dict(m) for m in data]
        except FileNotFoundError:
            self.materias = []
    
        
    