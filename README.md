# 📡 Simple Network Ping Monitor

Um script automatizado em Python puro para monitorar a disponibilidade de equipamentos de rede, links dedicados e ativos de infraestrutura de TI.

Este projeto foi criado para simplificar a rotina de suporte, verificando rapidamente se gateways, modems e roteadores estão respondendo na rede, gerando um log de auditoria automático.

## 🚀 Funcionalidades

- **Ping Automatizado:** Lê uma lista de endereços IPv4 a partir de um arquivo de texto.
- **Multiplataforma:** Identifica automaticamente se o sistema é Windows ou Linux e ajusta o comando de rede.
- **Log de Auditoria:** Salva o histórico de indisponibilidade com data e hora exatas em um arquivo `status_log.txt`.
- **Fácil Manutenção:** Não requer instalação de bibliotecas externas complexas.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- Bibliotecas nativas: `os`, `platform`, `datetime`

## ⚙️ Como usar na sua máquina

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/network-ping-monitor.git](https://github.com/SEU_USUARIO/network-ping-monitor.git)