# Fluxo Financeiro

**Área:** Financeiro  
**Sistema:** TOTVS Winthor + Excel  
**Revisão:** 2026-04

---

## Visão Geral

```
Pedido emitido → NF gerada → Lançamento TOTVS → Planilha de Caixa → Conciliação
```

---

## Etapas do Fluxo

### 1. Emissão e Faturamento
- Pedido aprovado no TOTVS → NF emitida automaticamente
- NF registrada em `dados/logistica/controle_nfs.xlsx`

### 2. Lançamento Financeiro
- Valor da NF lançado em contas a receber no TOTVS
- Lançamento manual refletido em `dados/financeiro/fluxo_caixa.xlsx`
- Despesas registradas em `dados/financeiro/despesas.xlsx`

### 3. Conciliação (execução periódica)
- Cruzamento entre NFs emitidas e entradas no fluxo de caixa
- Execução do prompt `prompts/conciliacao.prompt.md`
- Resultado salvo em `analises/inconsistencias/`

### 4. Fechamento
- Relatório gerado em `analises/relatorios/`
- Inconsistências tratadas e documentadas

---

## Indicadores Monitorados

| Indicador | Fonte | Frequência |
|---|---|---|
| Saldo de caixa | fluxo_caixa.xlsx | Diária |
| NFs não lançadas | controle_nfs.xlsx x fluxo_caixa.xlsx | Semanal |
| Despesas vs orçamento | despesas.xlsx | Mensal |
| Contas a receber em aberto | TOTVS | Semanal |

---

## Responsáveis

| Etapa | Responsável |
|---|---|
| Emissão de NF | Assistente Administrativo |
| Lançamento financeiro | Financeiro |
| Conciliação | Analista Financeiro / IA |
| Aprovação de relatório | Gestor |
