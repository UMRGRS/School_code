#class
phi = (1 + 5 ** 0.5) / 2
lenguajes = ["Python", "Ruby", "PHP", "JavaScript", "Java"]
class CalculadoraRecursiva:
    
    def calcular_mcd(self,a,b):
        if b==0:
            return a
        else:
            return self.calcular_mcd(self,b,a%b)

    def suma_digitos(self,a):
        return 0 if a == 0 else a%10 + self.suma_digitos(self,a//10)
                        
    def generar_fibonacci(self,a):
        return 0 if a==0 else (print(int((phi**a-(1-phi)**a)/5 ** 0.5)) or self.generar_fibonacci(self,a-1))
            
    def potencia_recursiva(self,a,b):
        if b == 0:
            return 1
        elif b>0:
            return a * self.potencia_recursiva(self,a,b-1)
    
    def contar_elementos(self,lista:list):
        if not lista:
            return 0
        else:
            return 1 + self.contar_elementos(self,lista[1:])
        
owo = CalculadoraRecursiva
print(owo.calcular_mcd(owo,270,192))
print(owo.suma_digitos(owo,12345))
owo.generar_fibonacci(owo,6)
print(owo.potencia_recursiva(owo,3,3))
print(owo.contar_elementos(owo,lenguajes))