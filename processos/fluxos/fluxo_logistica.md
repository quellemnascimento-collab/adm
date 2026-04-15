# Fluxo Logístico

**Área:** Logística  
**Sistema:** TOTVS Winthor + Excel  
**Revisão:** 2026-04

---

## Visão Geral

```
Pedido aprovado → Separação → Emissão de NF → Expedição → Entrega → Confirmação
```

---

## Etapas do Fluxo

### 1. Recebimento do Pedido
- Pedido liberado no TOTVS (status: Liberado)
- Verificar disponibilidade em estoque

### 2. Emissão da Nota Fiscal
- NF emitida no TOTVS após liberação
- Registrar número da NF em `dados/logistica/controle_nfs.xlsx`
- Campos obrigatórios: número NF, data emissão, cliente, valor, status

### 3. Expedição
- NF impressa e vinculada à carga
- Atualizar status em `controle_nfs.xlsx`: `Emitida → Em Trânsito`

### 4. Entrega e Confirmação
- Confirmar entrega com assinatura do cliente
- Atualizar status: `Em Trânsito → Entregue`
- Comunicar financeiro para baixa no contas a receber

### 5. Devoluções
- Registrar NF de devolução com referência à NF original
- Atualizar `controle_nfs.xlsx` com status `Devolvida`
- Cruzar com financeiro para ajuste no fluxo de caixa

---

## Status de NF

| Status | Descrição |
|---|---|
| `Emitida` | NF emitida, aguardando expedição |
| `Em Trânsito` | Mercadoria despachada |
| `Entregue` | Confirmação de entrega recebida |
| `Devolvida` | Devolução total ou parcial |
| `Cancelada` | NF cancelada antes da expedição |

---

## Indicadores

| Indicador | Meta |
|---|---|
| NFs entregues no prazo | > 95% |
| NFs sem confirmação > 7 dias | 0 |
| Taxa de devolução | < 2% |

---

## Referências

- Fluxo financeiro: `processos/fluxos/fluxo_financeiro.md`
- Prompt de conciliação: `prompts/conciliacao.prompt.md`
