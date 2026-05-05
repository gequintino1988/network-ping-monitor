# 📡 Monitor Simples de Rede (Ping Script)

Um script em Python puro, criado com foco no aprendizado prático! Este projeto foi desenvolvido para monitorar a disponibilidade de equipamentos de rede de forma simples, utilizando uma lógica de programação linear e ideal para iniciantes.

É o projeto perfeito para quem está dando os primeiros passos em Análise e Desenvolvimento de Sistemas e quer entender como o Python interage com o sistema operacional para automatizar tarefas de infraestrutura de TI.

## 🚀 Funcionalidades

- **Foco Didático:** Código 100% comentado, linha por linha, explicando o que cada comando faz (ideal para estudos).
- **Leitura de Arquivos:** Lê uma lista de endereços IP diretamente de um arquivo de texto (`ips.txt`) utilizando laços de repetição (`for`).
- **Ping Automatizado:** Utiliza comandos nativos do sistema Windows para disparar testes de conexão contra os equipamentos.
- **Geração de Logs:** Cria e atualiza automaticamente um arquivo `status_log.txt` com o histórico dos testes, registrando o sucesso ou a falha com a data e hora exatas.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- Bibliotecas nativas:
  - `os` (para integração com comandos do sistema operacional).
  - `time` (para captura e formatação simples de horários).

## ⚙️ Passo a Passo: Como usar na sua máquina

1. **Clone o repositório:**
   ```bash
   git clone git clone https://github.com/gequintino1988/network-ping-monitor.git