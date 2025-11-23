# agendaja

SaaS de agendamento e lembretes para profissionais autônomos e pequenos negócios.  
Permite gerenciar clientes, serviços, horários, lembretes automáticos e planos pagos com Stripe.

Repositório: https://github.com/brunolagaris/agendaja  
Autor: [@brunolagaris](https://github.com/brunolagaris)  
Portfólio: https://martinsbruno.dev


---

## Visão geral

### O que é o agendaja?

O **agendaja** é um backend SaaS focado em profissionais que vivem de horário marcado
(barbeiros, terapeutas, consultores, tatuadores, etc.).

Ele oferece:

- Painel para gerenciar **clientes**, **serviços** e **agendamentos**
- Página pública de agendamento para o cliente final
- **Lembretes automáticos** (e-mail) antes da sessão
- Sistema de **planos (free / pro)** com limitações claras
- Integração real com **Stripe** para assinaturas mensais

O foco deste projeto é ser **portfólio real**, com:

- Regras de negócio concretas
- Autenticação real
- Assinatura de planos de verdade (Stripe em modo de teste)
- Base pronta para deploy em produção


### Principais funcionalidades

- Cadastro e autenticação de usuários (profissionais)
- Gestão de:
  - Clientes
  - Serviços (nome, duração, preço)
  - Agendamentos (data, hora, status)
- Regras de plano:
  - **Free**: limite de agendamentos futuros, sem recursos avançados
  - **Pro**: agendamentos ilimitados e recursos extras
- Assinaturas com Stripe:
  - Criação de sessão de checkout
  - Webhook para ativar/desativar assinatura
- Lembretes:
  - Registro de lembretes agendados e enviados
  - Canal principal: e-mail

---

## Stack técnica

- **Linguagem:** Python 3.11+
- **Framework web:** Django 5
- **API:** Django REST Framework
- **Banco de dados:** PostgreSQL
- **Pagamentos:** Stripe (Subscriptions)
- **Configuração:** `python-dotenv` + `.env`
- **Testes:** `pytest` / `pytest-django` (planejado)
- **Qualidade de código:** `black`, `ruff` (planejado)
- **CI/CD:** GitHub Actions (planejado)

---

## Estrutura do projeto

```text
agendaja/
  config/           # Configuração principal do Django
  accounts/         # Usuários, planos, assinaturas
  scheduling/       # Clientes, serviços, agendamentos, lembretes
  billing/          # Integração com Stripe e logs de eventos
  manage.py
  requirements.txt
  .env.example
