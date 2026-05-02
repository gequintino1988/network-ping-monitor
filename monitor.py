# 1. IMPORTANDO BIBLIOTECAS (Trazendo ferramentas extras para o Python)
# Importa a biblioteca 'os' que permite rodar comandos do sistema operacional (como o ping)
import os

# Importa a biblioteca 'time' para pegar a hora atual de um jeito bem simples
import time

# 2. INÍCIO DO PROGRAMA
# Mostra uma mensagem na tela (terminal) dizendo que o programa começou
print("--- Iniciando Monitoramento ---")

# 3. LENDO OS IPS
# Abre o arquivo de texto que tem os IPs. A letra 'r' significa que vamos apenas ler (Read)
arquivo_ips = open('ips.txt', 'r')

# Lê todas as linhas de dentro do arquivo e guarda em uma lista chamada 'linhas'
linhas = arquivo_ips.readlines()

# Fecha o arquivo de IPs porque já guardamos tudo na memória e não precisamos mais dele
arquivo_ips.close()

# 4. PREPARANDO O ARQUIVO DE LOG
# Abre o arquivo de log para salvar os resultados. A letra 'a' significa adicionar (Append) no final
arquivo_log = open('status_log.txt', 'a')

# Pega a hora exata de agora e guarda na variável 'hora_atual'
hora_atual = time.ctime()

# Escreve no arquivo de log que o monitoramento começou, juntando os textos com o símbolo de +
arquivo_log.write("--- Novo teste iniciado em: " + hora_atual + " ---\n")

# 5. AVALIANDO CADA IP (O Laço de Repetição)
# Começa um laço (for). Ele vai passar por cada 'linha' dentro da nossa lista de 'linhas'
for linha in linhas:

    # Limpa espaços em branco invisíveis ou quebras de linha que ficam no final do IP
    ip = linha.strip()

    # Se a linha estiver completamente vazia, o 'if' percebe e o 'continue' pula para a próxima
    if ip == "":
        continue

    # Cria o comando de ping.
    # O "-n 1" diz para o Windows mandar apenas 1 pacote de teste (para ser mais rápido).
    comando = "ping -n 1 " + ip

    # Executa o comando no sistema usando a biblioteca 'os'
    # Se a internet funcionar e o IP responder, o Windows devolve o número 0.
    resultado = os.system(comando)

    # Pega a hora atual novamente para saber o momento exato deste teste específico
    hora_do_teste = time.ctime()

    # 6. VERIFICANDO O RESULTADO (A Condição)
    # Verifica se o resultado foi igual a 0 (ou seja, deu certo)
    if resultado == 0:
        # Cria a mensagem de sucesso
        mensagem = "[ONLINE] O IP " + ip + " esta funcionando bem."
    else:
        # Cria a mensagem de falha (se o resultado for diferente de 0)
        mensagem = "[OFFLINE] ALERTA: O IP " + ip + " falhou."

    # Mostra a mensagem final na tela preta para você ver rodando
    print(mensagem)

    # Escreve essa mesma mensagem dentro do arquivo de log, colocando a hora antes
    # O "\n" no final serve para o texto pular para a linha de baixo no arquivo
    arquivo_log.write(hora_do_teste + " -> " + mensagem + "\n")

# 7. FINALIZANDO
# Pula uma linha no arquivo de log para separar do próximo teste que você fizer no futuro
arquivo_log.write("\n")

# Fecha o arquivo de log para salvar todas as alterações no disco rígido
arquivo_log.close()

# Avisa na tela que o programa terminou todo o trabalho
print("--- Fim do Monitoramento ---")