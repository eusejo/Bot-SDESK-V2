# 📘 Documentação do Projeto

## 🛠️ Mudanças Realizadas

### 1. Correção de Condicional

``` python
if servico == 1 or 3 or 4:
    inspecoes()
```

❌ Problema: Essa condição sempre retornava **True**, porque `3` e `4`
são valores verdadeiros.

✅ Correção: Ajustada a condicional para verificar corretamente cada
valor.

------------------------------------------------------------------------

### 2. Função `patri()`

``` python
def patri():
    patris = []
    with open('patri.txt','r') as arq:
        for c in arq.readlines():
            patris.append(int(c.strip()))
    return patris
```

❌ Problema: Código pouco otimizado e ocorria erro quando patrimônios
tinham letras.

✅ Correção: Refatorada usando **list comprehension** e corrigido o
tratamento dos patrimônios inválidos.

------------------------------------------------------------------------

### 3. Organização do Código

📦 O código foi reorganizado utilizando **Classes** e **Módulos** para
melhor manutenção e escalabilidade.

------------------------------------------------------------------------

## 📚 Bibliotecas Utilizadas

-   🌐 **Selenium** → Automação com navegador\
-   ⚙️ **Argparser** → Uso de argumentos no terminal\
-   🎛️ **Questionary** → Criação de menu quando não há argumentos\
-   📝 **Logging** → Registro de logs da automação\
-   ⏰ **Schedule** → Agendamento de chamados

------------------------------------------------------------------------

🚀 Projeto atualizado com melhorias de legibilidade, manutenção e
performance.
🔮 Mais atualizações no futuro.
