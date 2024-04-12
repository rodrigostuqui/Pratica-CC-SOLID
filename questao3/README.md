## Instalação

1. Clone o Repositorio para sua maquina
 ```bash
    git clone https://github.com/rodrigostuqui/Pratica-CC-SOLID.git
 ```

2. Entre na pasta do repositorio em seguida na pasta questao3
```bash
    cd Pratica-CC-SOLID/questao3
```
3. Instale os requirements.txt
```bash
    pip install -r "requirements.txt"
```S

4. Execute com uvicorn
```bash
   uvicorn main:app --reload
```

### Execução de testes
Para executar todos os teste:
```bash
   pytest
```
### Questão 3) Desenvolva *em python* endpoints REST para gerir uma conta corrente
Neste exercício deve ser criado uma api REST para permtir realizar operações básicas de cadastro, debito, credito e saldo da conta corrente.

Siga as orientações abaixo:

##### Cadastrar conta corrente
- URL: POST /contas/
- ENTRADA: ```{ "banco": 1, "agencia": 1738, "conta": 10789 }```
- SAIDA: 201 ```{ "id": 1}```

##### Creditar na conta corrente
- URL: PUT /contas/\<id\>/credito
- ENTRADA: ```{ "valor": 10.75 }```
- SAIDA: 200

##### Debitar na conta corrente
- URL: PUT /contas/\<id\>/debito
- ENTRADA: ```{ "valor": 9.75 }```
- SAIDA: 200

##### Consultar o saldo da conta corrente
- URL: GET /contas/\<id\>/saldo
- SAIDA: 200 ```{ "valor": 1.0}```