# IT-ADM-002 — Edição de Pedido

**Sistema:** TOTVS Winthor  
**Responsável:** Assistente Administrativo  
**Revisão:** 2026-04

---

## Objetivo

Padronizar o processo de edição de pedidos já registrados no TOTVS Winthor.

---

## Pré-requisito

- Pedido existente e com status compatível com edição (não faturado)
- Acesso ao módulo de pedidos no TOTVS Winthor

---

## Passo a Passo

| # | Ação | Observação |
|---|---|---|
| 1 | Localizar o pedido | Buscar por número, cliente ou data |
| 2 | Acessar tela de edição | Pressionar `F12` na tela do pedido |
| 3 | Realizar as alterações necessárias | Quantidade, produto, preço ou dados do cliente |
| 4 | Confirmar e gravar | Verificar status após gravação |

---

## Pontos de Atenção

- Pedidos **já faturados** não podem ser editados — exige cancelamento e re-emissão
- Alterações de valor impactam o **fluxo de caixa** — comunicar o financeiro
- Manter registro das edições realizadas para fins de auditoria

---

## Regras de Negócio

- Edições de valor acima de 10% do pedido original requerem aprovação do gestor
- Alterações de cliente em pedido existente **não são permitidas** — cancelar e emitir novo pedido

---

## Referências

- IT-ADM-001 — Emissão de Pedido
- Fluxo: `processos/fluxos/fluxo_financeiro.md`
