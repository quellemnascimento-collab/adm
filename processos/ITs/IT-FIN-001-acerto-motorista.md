# IT-FIN-001 — Acerto de Motorista (Contas a Receber)

**Área:** Financeiro  
**Sistema:** TOTVS Winthor + Excel  
**Responsável:** Assistente Financeiro / Caixa  
**Revisão:** 2026-04

---

## Objetivo

Padronizar o processo de acerto de motorista, garantindo que os valores recebidos via canhoto sejam corretamente registrados no controle de notas, lançados no caixa e baixados no TOTVS Winthor — sem divergências entre os sistemas.

---

## Pré-requisitos

- Acesso à pasta compartilhada `G:\Drives compartilhados\CRC - ES\Administrativo - CRC ES\Financeiro\`
- Acesso ao TOTVS Winthor com permissão na rotina 421
- Canhotos físicos entregues pelo motorista em mãos

---

## Passo a Passo

### Etapa 1 — Verificar o Controle de Notas Mensal

| # | Ação | Detalhe |
|---|---|---|
| 1 | Abrir a planilha **Controle de Notas Mensal** | Caminho: `G:\Drives compartilhados\CRC - ES\Administrativo - CRC ES\Financeiro\Contas a receber` |
| 2 | Localizar a nota correspondente ao canhoto recebido | Buscar pelo número da NF ou nome do cliente |
| 3 | Conferir se os dados do canhoto batem com a planilha | Ver pontos de atenção abaixo |
| 4 | Preencher as informações do acerto na linha da nota | Preencher todos os campos obrigatórios |

**Campos obrigatórios a preencher:**

| Campo | Descrição |
|---|---|
| Valor da nota | Valor original da NF |
| Número da nota | Número da NF emitida |
| Condição de pagamento | À vista, prazo, boleto, etc. |
| Data do pagamento | Data prevista ou acordada |
| Valor pago | Valor efetivamente recebido do motorista |
| Motorista do acerto | Nome do motorista que realizou a entrega |
| Data do acerto | Data em que o canhoto foi entregue e o valor recebido |

---

### Etapa 2 — Lançar no Controle de Caixa

| # | Ação | Detalhe |
|---|---|---|
| 5 | Abrir o arquivo **Controle de Caixa ES** | Caminho: `G:\Drives compartilhados\CRC - ES\Administrativo - CRC ES\Financeiro\Fluxo de Caixa\Fechamento diário de caixa` |
| 6 | Localizar a data do acerto | Aba ou linha correspondente ao dia atual |
| 7 | Lançar a entrada do valor recebido | Registrar conforme campos solicitados na planilha |
| 8 | Salvar a planilha | Garantir que o lançamento foi gravado |

---

### Etapa 3 — Dar Baixa no TOTVS Winthor

| # | Ação | Detalhe |
|---|---|---|
| 9 | Acessar o TOTVS Winthor | Fazer login com usuário e senha |
| 10 | Acessar a **Rotina 421** | Baixa de títulos / Contas a receber |
| 11 | Localizar o título pelo número da NF ou cliente | Conferir valor e vencimento antes de baixar |
| 12 | Informar os dados do pagamento | Data, valor recebido e forma de pagamento |
| 13 | Confirmar a baixa | Verificar se o status do título mudou para "Baixado" |

---

### Etapa 4 — Fechamento do Caixa

| # | Ação | Detalhe |
|---|---|---|
| 14 | Realizar a contagem física do dinheiro | Conferir se o total em espécie bate com os lançamentos do dia |
| 15 | Arquivar os canhotos | Organizar fisicamente por data e número de NF |
| 16 | Fechar o caixa | Registrar saldo final no Controle de Caixa ES |

---

## Pontos de Atenção

- **Divergência de valor:** Se o valor pago pelo motorista for diferente do valor da nota, registrar a diferença e comunicar o supervisor imediatamente — não lançar valor errado
- **Canhoto sem assinatura:** Não acertar valores sem canhoto assinado pelo cliente
- **Nota não encontrada na planilha:** Verificar se a NF está na planilha correta do mês; se não estiver, acionar o responsável pela emissão
- **Baixa duplicada no TOTVS:** Antes de dar baixa na rotina 421, sempre confirmar que o título não está já baixado

---

## Critérios de Validação

O processo foi executado corretamente quando:

- [ ] Todos os campos do Controle de Notas Mensal estão preenchidos para o canhoto recebido
- [ ] O valor lançado no Controle de Caixa ES bate com o valor do canhoto
- [ ] O título está com status **Baixado** na rotina 421 do TOTVS
- [ ] O saldo final do caixa confere com a contagem física do dinheiro
- [ ] O canhoto está arquivado fisicamente

---

## Possíveis Erros e Correções

| Erro | Causa Provável | Correção |
|---|---|---|
| Valor pago diverge do valor da NF | Desconto concedido na entrega ou troco errado | Registrar diferença, comunicar supervisor, não fechar sem aprovação |
| Título não encontrado na rotina 421 | NF não lançada no financeiro do TOTVS | Acionar responsável pelo faturamento para incluir o título |
| Canhoto sem número legível | Canhoto danificado ou preenchimento incorreto | Consultar o número da NF na planilha pelo nome do cliente e data |
| Planilha travada (somente leitura) | Outro usuário com o arquivo aberto | Aguardar liberação ou solicitar fechamento do arquivo |
| Saldo do caixa não fecha | Lançamento duplicado ou valor errado | Revisar todos os lançamentos do dia antes de fechar |

---

## Melhorias de Processo

1. **Validação automática por fórmula:** Incluir na planilha Controle de Notas Mensal uma coluna de status com fórmula que compare o valor pago com o valor da nota e destaque em vermelho divergências automaticamente — eliminando conferência manual.

2. **Checklist digital de fechamento de caixa:** Criar uma aba na planilha Controle de Caixa ES com checklist das etapas desta IT (colunas: etapa concluída / responsável / hora), evitando que o caixa seja fechado com etapas pendentes.

---

## Referências

- Fluxo: `processos/fluxos/fluxo_financeiro.md`
- Prompt de conciliação: `prompts/conciliacao.prompt.md`
- TOTVS Winthor — Rotina 421: Baixa de Títulos a Receber
