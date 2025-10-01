
## Cliente/Servidor TCP e UDP para Transferência de Arquivos  

### Objetivo
Desenvolver um programa cliente/servidor que realize a **transferência de um arquivo** entre duas máquinas ou na mesma, em caso de testes locais e compare o tempo de transmissão utilizando **sockets TCP e UDP**.  

---

### Requisitos atendidos
1. O arquivo a ser transferido (`file_example_MP4_1920_18MG.mp4`) é baixado do link:  
   https://file-examples.com/storage/fe90bd970b68dc58f98d738/2017/04/file_example_MP4_1920_18MG.mp4 

2. O **cliente** apresenta um menu e escolhe o protocolo (**TCP ou UDP**).  

3. A contabilização do tempo é feita **somente no servidor**, durante a transferência efetiva do arquivo.  

4. O tempo medido pelo servidor é enviado ao cliente e exibido em tela.  

5. Foram definidos testes entre máquinas distintas do laboratório. O **tamanho de buffer escolhido foi 4096 bytes (4 KB)**, pois este valor corresponde ao tamanho típico de uma página de memória do sistema operacional, equilibrando:
   - eficiência na cópia de dados (menos chamadas de sistema);  
   - baixo consumo de memória;  
   - portabilidade e alinhamento com boas práticas de sistemas de rede.  

6. Implementação realizada em **Python 3**

---

### 🔸 Pré-requisitos
- **Python 3.x** instalado nas máquinas.  
- Certifique-se de que o arquivo de teste (`file_example_MP4_1920_18MG.mp4`) está na mesma pasta do `servidor.py`.  

### 🔸 Executar o servidor
Na máquina **servidora**:
```bash
python3 servidor.py
```
> O servidor ficará ouvindo simultaneamente em **TCP (porta 5000)** e **UDP (porta 5001)**.  

### 🔸 Executar o cliente
Na máquina **cliente**:
```bash
python3 cliente.py
```
O cliente exibirá o menu:  
```
1 - TCP
2 - UDP
Escolha o protocolo:
```

No final, será exibido o **tempo de transmissão** (calculado pelo servidor). 

---

### Resultados Esperados
- **TCP**: transferência confiável, sem perdas, mas com maior tempo em caso de redes com latência/erros.  
- **UDP**: transferência mais rápida, mas sujeita a perdas de pacotes.

---

### Execução em laboratório
- Rodar o servidor em um computador, liberando as portas 5000 (TCP) e 5001 (UDP).  
- Rodar o cliente em outro computador, apontando para o **IP do servidor** de forma manual.  
- Recolher tempos de execução e comparar TCP vs UDP.  
