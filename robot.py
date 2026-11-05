class Robot:
    def __init__(self, codice: str, modello: str, applicazione: str, peso_massimo_componenti_kg: float, stato: str) -> None:
        self.codice : str = codice
        self.modello: str = modello
        self.applicazione: str = applicazione
        self.peso_massimo_componenti_kg: float = peso_massimo_componenti_kg
        self.stato: str = stato
        self.ListaComp = list[Componente] 
        
    def  aggiungi_componente(self, n_componente: Componente) -> None:
        if n_componente.peso_kg < peso_Massimo:
            self.ListaComp[n_componente]= n_componente
        else  : print(ValueError)
        
    def peso_componenti(self) -> float:
        for c in self.Lista[n_componente]:
            self.somma+=self.n_componente.peso_kg
            
    def componenti_sotto_peso(self, peso_massimo: float) -> list[Componente]:
        risultati = [s for s in self.ListaComp.values() if s.peso_kg < peso_massimo]
        return risultati            