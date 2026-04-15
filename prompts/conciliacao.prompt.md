# Prompt — Conciliação Financeira

**Área:** Financeiro / Logística  
**Arquivos de entrada:**
- `dados/logistica/controle_nfs.xlsx`
- `dados/financeiro/fluxo_caixa.xlsx`
- `dados/financeiro/conciliacao.xlsx`

---

## Instrução ao Modelo

Você está analisando dados financeiros e logísticos da empresa que opera com TOTVS Winthor.

Objetivo: garantir que todas as notas fiscais emitidas estejam corretamente refletidas no financeiro.

### Passo a Passo Obrigatório

1. **Somar NFs emitidas** — total de NFs com status `Entregue` no período
2. **Subtrair devoluções** — NFs com status `Devolvida`
3. **Calcular valor esperado em caixa** — NFs entregues menos devoluções
4. **Comparar com valor real no fluxo** — verificar entradas em `fluxo_caixa.xlsx`
5. **Identificar divergências** — diferença entre valor esperado e valor real
6. **Listar notas faltantes** — NFs entregues sem entrada correspondente no caixa
7. **Apontar possíveis erros operacionais** — duplicidades, valores divergentes, lançamentos errados

---

## Entregável

Retornar em Markdown com as seguintes seções:

### 1. Resumo da Conciliação
| Item | Valor |
|---|---|
| Total NFs emitidas | R$ |
| Total devoluções | R$ |
| Valor esperado em caixa | R$ |
| Valor real no fluxo | R$ |
| **Divergência** | **R$** |

### 2. Notas Não Lançadas
Lista de NFs sem entrada correspondente no fluxo de caixa.

### 3. Diferenças Financeiras
NFs com valor divergente entre logística e financeiro.

### 4. Recomendações
Ações práticas para resolver cada inconsistência encontrada.

---

## Regra

Seja direto, analítico e orientado à decisão.
