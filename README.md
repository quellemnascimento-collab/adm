# Empresa Operacional AI

Sistema de análise operacional com inteligência artificial para suporte às áreas de Financeiro, Logística e RH.

## Sistemas Integrados

| Sistema | Uso |
|---|---|
| **TOTVS Winthor** | ERP principal — fonte de verdade para pedidos, NFs e financeiro |
| **Planilhas Excel** | Controle operacional complementar e conciliação manual |

## Objetivos

- Conciliação financeira automatizada entre TOTVS e planilhas
- Detecção e rastreamento de inconsistências
- Geração de relatórios gerenciais acionáveis
- Padronização e documentação de processos

## Estrutura do Repositório

```
/
├── /dados              → Planilhas operacionais (não versionadas — ver .gitignore)
│   ├── /financeiro     → Fluxo de caixa, despesas, conciliação
│   ├── /logistica      → Controle de NFs
│   └── /rh             → Base de colaboradores
│
├── /processos          → Documentação de processos
│   ├── /ITs            → Instruções de Trabalho (passo a passo)
│   └── /fluxos         → Fluxogramas em Markdown
│
├── /analises           → Saídas geradas pela IA
│   ├── /relatorios     → Relatórios gerenciais
│   ├── /inconsistencias → Registros de divergências detectadas
│   └── /dashboards     → Painéis de indicadores
│
├── /prompts            → Prompts especializados por área
└── /skills             → Definições de agentes/skills
```

## Áreas

### Financeiro
- Fluxo de caixa (entradas e saídas)
- Contas a pagar e a receber
- Conciliação entre TOTVS e planilhas de controle

### Logística
- Controle e rastreamento de Notas Fiscais
- Cruzamento entre NFs emitidas e registros financeiros

### RH
- Base de colaboradores ativos
- Controle de equipe e gestão de dados cadastrais

## Como Usar

1. Atualize as planilhas em `/dados` com os dados mais recentes
2. Execute o prompt da área desejada em `/prompts`
3. Os resultados são salvos em `/analises`
4. Inconsistências detectadas ficam em `/analises/inconsistencias`

## Processos Documentados

| Código | Título | Área |
|---|---|---|
| IT-ADM-001 | Emissão de Pedido | Administrativo |
| IT-ADM-002 | Edição de Pedido | Administrativo |
