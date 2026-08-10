# LawLever — dados de marketing do Instagram

Esta pasta é a **memória do ciclo de experimentos**. O ambiente onde as skills
rodam reseta o disco entre sessões; só o repositório persiste. Tudo aqui é
escrito por máquina — edite à mão só as notas em prosa, nunca as linhas de dados.

## Os quatro arquivos

| Arquivo | Papel | Quem lê | Escrito por |
|---|---|---|---|
| `launched_posts.md` | índice legível: histórico + impacto por post | humano, no browser | `consolidate_metrics.py` |
| `experiments.jsonl` | **fonte de verdade**: engajamento + negócio + normalizados | a skill | `consolidate_metrics.py` |
| `conclusions.md` | digesto por ciclo (**append**, um bloco por rodada) | humano | `draw_conclusions.py` |
| `hypotheses.jsonl` | livro-razão dos experimentos e baselines | ambos | `propose_next.py` |

A separação existe porque um markdown de 20 colunas não é lido por ninguém e um
JSONL não é navegável no browser. Cada arquivo serve a um leitor.

`conclusions.md` é **anexado**, nunca sobrescrito: a trajetória do aprendizado
vale mais que o retrato de hoje, e permite ver quando uma conclusão mudou de
sinal.

## Como ler os números (importa)

- **Ranqueie por receita da janela, não vitalícia.** A receita vitalícia sempre
  favorece o que está no ar há mais tempo — vira medida de antiguidade
  disfarçada de mérito.
- **Só ranqueie quem amadureceu.** Um público tocado ontem teve um dia para
  converter, não trinta. O campo `business.rankable` já materializa esse gate.
- **Clique não é conversão.** Crawler de preview de link infla clique, mas não
  infla mensagem no WhatsApp. Por isso `bot_clicks` é exposto — para o filtro
  ficar auditável.
- **`documents` e `inbound_messages` são descritivos**, não proxy de receita.
- **A atribuição é first-touch.** A receita de um usuário credita a campanha que
  o trouxe pela **primeira** vez. Consequência: um post que faz um seguidor
  antigo finalmente pagar marca **R$ 0**. O ranking de receita mede
  **aquisição**, não persuasão — então posts de meio e fundo de funil são
  estruturalmente subavaliados por ele e devem ser julgados por documentos,
  mensagens e craft.

## A coluna `Campanha`

É o código `/fale/<code>` que liga o post à receita. `-` significa post publicado
antes da instrumentação — sem atribuição possível, e isso não é recuperável
depois.

O código precisa casar `^[a-z0-9][a-z0-9-]{0,31}$` e **ser registrado na API
antes da publicação**. Um link que vai ao ar sem registro falha duas vezes: o
clique colapsa em `other` e o marcador `Ref: ll-<code>` não é removido da
mensagem, chegando ao agente como se o cliente tivesse escrito.

Convenção: `<aaaammdd>-<serie>-<tema>` — `resp` (LawLever Responde), `caso` (O
Caso da Semana), `dep` (Depende do Seu Caso), `flex` (slot flexível).

## Estado atual

Primeiro registro consolidado em **2026-08-10**: 116 posts publicados
(2025-01-29 → 2026-08-07), 30.522 views, 16.922 reach, 133 sends, 43 saves.
Nenhuma campanha registrada ainda, então o primeiro ciclo roda em **cold-start**
(ranking por engajamento). O modo troca sozinho para receita assim que houver
campanhas maduras.

Gerado pela skill `lawlever-experimentos`.
