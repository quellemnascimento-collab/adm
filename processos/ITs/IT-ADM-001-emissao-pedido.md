# IT-ADM-001 — Emissão de Pedido

**Sistema:** TOTVS Winthor  
**Responsável:** Assistente Administrativo  
**Revisão:** 2026-04

---

## Objetivo

Padronizar o processo de emissão de pedidos no sistema TOTVS Winthor, garantindo registro correto e rastreabilidade.

---

## Passo a Passo

| # | Ação | Observação |
|---|---|---|
| 1 | Acessar módulo de pedidos no TOTVS Winthor | Menu principal → Pedidos |
| 2 | Inserir dados do cliente | Validar CNPJ/CPF e dados cadastrais |
| 3 | Inserir produtos | Código, quantidade e preço conforme tabela vigente |
| 4 | Confirmar gravação | Verificar número do pedido gerado |

---

## Pontos de Atenção

- **Validar status do pedido:** Liberado ou Bloqueado antes de prosseguir
- **Edição futura:** Utilizar `F12` para acesso à tela de edição (ver IT-ADM-002)
- Pedidos bloqueados exigem aprovação do responsável financeiro antes do faturamento

---

## Erros Comuns

| Erro | Causa Provável | Ação |
|---|---|---|
| Pedido criado como bloqueado | Limite de crédito atingido | Acionar financeiro |
| Cliente não encontrado | Cadastro incompleto | Abrir chamado no TOTVS |
| Produto sem preço | Tabela de preços desatualizada | Verificar com comercial |

---

## Referências

- IT-ADM-002 — Edição de Pedido
- Fluxo: `processos/fluxos/fluxo_financeiro.md`
