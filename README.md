# 🛰️ ECS Message Processor com Regras Dinâmicas via DynamoDB + DAX

Este projeto implementa um processador de mensagens de alta performance usando **AWS ECS**, **SQS**, **SNS**, **DynamoDB**, e **DAX**, com código totalmente modularizado em **Python** e padrões de arquitetura escaláveis.

## 🎯 Objetivo

Consumir mensagens de uma fila SQS (originadas via SNS), aplicar regras de negócio configuráveis dinamicamente via DynamoDB, realizar transformações e persistir os dados processados em uma nova tabela DynamoDB com suporte a DAX para cache de escrita/leitura otimizada.

---

## 🧱 Arquitetura

- **SQS + SNS:** Distribuição assíncrona de eventos.
- **ECS Fargate:** Execução escalável e desacoplada.
- **DynamoDB (Rules Table):** Define dinamicamente quais campos devem ser preservados, sobrescritos ou ignorados.
- **DynamoDB (Data Table):** Persistência dos dados processados.
- **DAX (opcional):** Otimização de leitura/gravação com fallback automático para DynamoDB nativo.

---

## 🧠 Funcionalidades

- ✅ Consumo de mensagens individual ou em lote (até 10 simultaneamente)
- ✅ Processamento concorrente via `ThreadPoolExecutor`
- ✅ Aplicação de regras de negócio baseadas em origem e estrutura da mensagem
- ✅ Leitura dinâmica de permissões e campos válidos da tabela de regras
- ✅ Suporte a cache in-memory com TTL de 1 minuto para regras
- ✅ Fallback automático do DAX para DynamoDB caso o DAX esteja indisponível
- ✅ Extensível via Padrão Strategy para novas regras (SOLID: OCP)

---

## 📁 Estrutura de Pastas

ecs_message_processor/
├── main.py # Entry point para Lambda ou ECS
├── consumers/ # SQS consumer
├── services/ # Orquestração e processamento
├── domain/ # Regras de negócio
├── repositories/ # Integrações com Dynamo/DAX
├── adapters/ # Adaptações de entrada
├── utils/ # Logger e helpers
├── config.py # Leitura de variáveis de ambiente
└── tests/ # Testes automatizados
