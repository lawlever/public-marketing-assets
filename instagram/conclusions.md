# LawLever — conclusões do ciclo de experimentos

Escrito por APPEND pela Fase P3 (`draw_conclusions.py`). Cada bloco é um ciclo.
O mais recente fica no fim do arquivo — leia de baixo para cima para ver o
estado atual, e de cima para baixo para ver como o aprendizado evoluiu.

---

## 2026-08-09 — ciclo

**Modo: COLD-START (sem receita atribuída).** 116 posts no histórico, 0 com código de campanha. Ranking por interação (sends+saves) por 1.000 views — indicador antecedente, não a verdade de solo. Assim que houver campanhas maduras, o ranking troca sozinho para R$/1k views.

**Top 12 posts:**

| # | post | série | fmt | camada | sends/1k | saves/1k | views |
|---|---|---|---|---|---|---|---|
| 1 | parem de gastar dinheiro com burocracia desnecessári | - | reel | topo | 93.53 | 7.19 | 139 |
| 2 | Todo grupo da família tem um. 😂🚨 | - | imagem | topo | 52.24 | 0.00 | 134 |
| 3 | Comprou e se arrependeu? A lei te dá mais poder do q | - | carrossel | topo | 15.38 | 30.77 | 65 |
| 4 | A LawLever em 3 passos 👇 | - | carrossel | meio | 0.00 | 33.33 | 30 |
| 5 | Fale com o bot da LawLever agora! Link na bio | - | reel | topo | 27.86 | 0.00 | 682 |
| 6 | No #OCasoDaSemana de hoje, falo sobre pontos que inq | caso-da-semana | reel | topo | 18.87 | 3.77 | 265 |
| 7 | EI, VOCÊ ADVOGADO! ☝🏼 | - | carrossel | topo | 6.10 | 12.20 | 164 |
| 8 | Vai emprestar dinheiro pra um amigo ou parente? Ante | - | carrossel | topo | 0.00 | 17.24 | 58 |
| 9 | Pode usar a bandeira do Brasil como roupa? Pode toca | - | reel | topo | 15.20 | 1.69 | 592 |
| 10 | Da Deepseek à acusação da OpenAI: a competição acirr | - | reel | topo | 10.86 | 2.80 | 2855 |
| 11 | O COMBINADO PODE SAIR CARO | - | reel | topo | 8.55 | 4.27 | 234 |
| 12 | A inteligência artificial está revolucionando o mund | - | reel | topo | 2.99 | 8.98 | 334 |

**Por série**

| corte | n | sends/1k | saves/1k | interação/1k | views méd. |
|---|---|---|---|---|---|
| caso-da-semana | 4 | 8.28 | 1.30 | 9.59 | 525 |
| - | 100 | 3.40 | 1.71 | 5.11 | 277 |
| lawlever-responde | 4 | 0.00 | 0.00 | 0.00 | 90 |
| depende-do-seu-caso | 3 | 0.00 | 0.00 | 0.00 | 118 |

**Por formato**

| corte | n | sends/1k | saves/1k | interação/1k | views méd. |
|---|---|---|---|---|---|
| reel | 55 | 4.64 | 0.98 | 5.62 | 262 |
| imagem | 23 | 3.71 | 1.20 | 4.92 | 284 |
| carrossel | 33 | 0.99 | 2.86 | 3.85 | 290 |

**Por camada de funil**

| corte | n | sends/1k | saves/1k | interação/1k | views méd. |
|---|---|---|---|---|---|
| topo | 93 | 3.80 | 1.53 | 5.33 | 301 |
| meio | 14 | 1.11 | 2.38 | 3.50 | 147 |
| fundo | 4 | 1.13 | 0.00 | 1.13 | 116 |

**Por área**

| corte | n | sends/1k | saves/1k | interação/1k | views méd. |
|---|---|---|---|---|---|
| trabalhista | 20 | 6.03 | 1.66 | 7.69 | 207 |
| consumidor | 10 | 3.24 | 3.08 | 6.32 | 139 |
| outro | 55 | 3.36 | 1.58 | 4.94 | 406 |
| familia | 5 | 0.00 | 3.45 | 3.45 | 116 |
| civil_contratos | 18 | 1.73 | 0.45 | 2.18 | 97 |
| empresarial | 3 | 1.50 | 0.00 | 1.50 | 106 |

⚠️ = menos de 3 posts no corte: sinal fraco, não vire recomendação.

---

## Ciclo 2026-08-11 — modo cold-start (aquisição de audiência)

**Amostra:** 77 posts publicados desde 01/06/2026 · 9.853 views.
Base ampliada: últimos 100 posts (abr/25 → ago/26) · 19.380 views.

**Conclusão 1 — o perfil não converte espectador em seguidor.**
0 seguidores em 77 posts. 0 também nos últimos 100. Não é amostra pequena: é
ausência de mecanismo. Nenhum post publicado promete continuidade, nomeia o
público ou serializa. Shares 7,7/1k · saves 1,1/1k.

**Conclusão 2 — carrossel está sem alcance nesta conta.**
reach médio 24 (n=21) contra 135 do Reel (n=45); shares/1k 0,7 contra 8,2.
Há 25 carrosséis agendados semanalmente até 16/12.

**Conclusão 3 — share vem de identificação, não de didática.**
Topo por shares/1k: demo do bot 93,5 (n=1, ⚠️), meme do grupo da família 52,2,
demo com link 27,9, Caso da Semana 18,9. Explicativo de lei fica em ~5.
Imagem tem o melhor shares/1k por formato (25,4) — mas n=4, ⚠️, não vira regra.

**Conclusão 4 — metade do conteúdo recente está fora da persona.**
Banco de horas, demitido sem justa causa, grávida, multa de trânsito, plano de
saúde, herança. Traz view e não traz seguidor: público sem motivo pra voltar.
`persona.md` já manda descartar tema de quem "perderia o emprego".

**Negócio (P1, com chave):** 12 campanhas, 0 rankeáveis, R$ 0, 0 first-touch.
Balde `other` vazio — nenhum link ao ar sem registro. Clique fortemente inflado
por bot (50 bot × 23 humanos no maior boost). Marcador `Ref:` chegando
corretamente; a ausência de first-touch é armadilha 5, não falha técnica.

**Proposta:** H001 — série "Frase de Cliente" (5 episódios, terças) + 5 posts de
apoio, todos de topo sem link. Variável: `cta` (CTA de seguir com promessa de
série numerada). Controle: baseline 0,0 seguidores/1k e 7,7 shares/1k.

---

## 2026-08-21 — ciclo

**Modo: COLD-START (sem receita atribuída).** 124 posts no histórico, 0 com código de campanha. Ranking por interação (sends+saves) por 1.000 views — indicador antecedente, não a verdade de solo. Assim que houver campanhas maduras, o ranking troca sozinho para R$/1k views.

**Top 10 posts:**

| # | post | série | fmt | camada | sends/1k | saves/1k | views |
|---|---|---|---|---|---|---|---|
| 1 | parem de gastar dinheiro com burocracia desnecessári | - | reel | topo | 93.53 | 7.19 | 139 |
| 2 | Todo grupo da família tem um. 😂🚨 | - | imagem | topo | 52.24 | 0.00 | 134 |
| 3 | NÃO CANCELE CONTRATOS E SAIA NO PREJUÍZO! | - | reel | topo | 51.72 | 0.00 | 232 |
| 4 | Comprou e se arrependeu? A lei te dá mais poder do q | - | carrossel | topo | 15.38 | 30.77 | 65 |
| 5 | A LawLever em 3 passos 👇 | - | carrossel | meio | 0.00 | 33.33 | 30 |
| 6 | Fale com o bot da LawLever agora! Link na bio | - | reel | topo | 27.70 | 0.00 | 686 |
| 7 | No #OCasoDaSemana de hoje, falo sobre pontos que inq | caso-da-semana | reel | topo | 18.87 | 3.77 | 265 |
| 8 | EI, VOCÊ ADVOGADO! ☝🏼 | - | carrossel | topo | 6.10 | 12.20 | 164 |
| 9 | Vai emprestar dinheiro pra um amigo ou parente? Ante | - | carrossel | topo | 0.00 | 17.24 | 58 |
| 10 | Pode usar a bandeira do Brasil como roupa? Pode toca | - | reel | topo | 15.20 | 1.69 | 592 |

**Por série**

| corte | n | sends/1k | saves/1k | interação/1k | views méd. |
|---|---|---|---|---|---|
| caso-da-semana | 4 | 8.28 | 1.30 | 9.58 | 526 |
| - | 107 | 3.75 | 1.59 | 5.35 | 267 |
| lawlever-responde | 4 | 0.00 | 0.00 | 0.00 | 90 |
| depende-do-seu-caso | 3 | 0.00 | 0.00 | 0.00 | 118 |

**Por formato**

| corte | n | sends/1k | saves/1k | interação/1k | views méd. |
|---|---|---|---|---|---|
| reel | 60 | 5.28 | 0.89 | 6.17 | 252 |
| imagem | 23 | 3.71 | 1.20 | 4.92 | 284 |
| carrossel | 35 | 0.94 | 2.70 | 3.64 | 277 |

**Por camada de funil**

| corte | n | sends/1k | saves/1k | interação/1k | views méd. |
|---|---|---|---|---|---|
| topo | 100 | 4.15 | 1.42 | 5.57 | 288 |
| meio | 14 | 1.11 | 2.38 | 3.50 | 148 |
| fundo | 4 | 1.12 | 0.00 | 1.12 | 116 |

**Por área**

| corte | n | sends/1k | saves/1k | interação/1k | views méd. |
|---|---|---|---|---|---|
| trabalhista | 17 | 9.58 | 0.93 | 10.51 | 171 |
| consumidor | 10 | 3.24 | 3.08 | 6.32 | 139 |
| outro | 62 | 3.31 | 1.68 | 4.99 | 395 |
| familia | 5 | 0.00 | 3.45 | 3.45 | 116 |
| civil_contratos | 17 | 1.75 | 0.44 | 2.19 | 89 |
| empresarial | 7 | 0.64 | 0.00 | 0.64 | 67 |

⚠️ = menos de 3 posts no corte: sinal fraco, não vire recomendação.

---

## Ciclo 2026-08-21 — modo cold-start · pergunta: qual post impulsionar PRA SEMPRE por seguidores/1k?

**Amostra:** 124 posts publicados (jan/25 → 21/08/26), 122 com métricas, 33.400 views.
**Negócio (P1):** sem chave no ambiente — ciclo em cold-start (só engajamento).

**Conclusão 1 — não existe "post que trouxe mais followers/1k". O dado é zero ou inexistente.**
O Buffer reporta `follows` em 84 dos 122 posts. Soma: **2 seguidores em 20.774 views**
(0,10/1k) — os dois no post de 29/01/2025 sobre IA na pesquisa jurídica, escrito para
ADVOGADOS (persona errada). Em 2026: **0 seguidores atribuídos em todos os posts** com
métrica. Ranquear por seguidores/1k hoje é ranquear zeros: qualquer "vencedor" seria
inventado. Escolher o post a impulsionar por este critério **não é possível com o
histórico atual**.

**Conclusão 2 — `follows` está AUSENTE em 38 dos 64 Reels (10.589 views sem o dado).**
Não é zero, é nulo: o Instagram não devolve o campo para parte dos vídeos. Os maiores
Reels da conta ("Fale com o bot" 686 views/19 shares; "NÃO CANCELE CONTRATOS"
232/12; "O combinado pode sair caro" 275/3; todos os Caso da Semana) estão nesse
grupo. Ou seja, **justamente os candidatos mais fortes a impulsionamento não têm
seguidores medidos**. A medição de seguidores tem que vir do Insights nativo do
Instagram ou do painel de anúncios — o Buffer não serve para este objetivo.

**Conclusão 3 — H013 (Frase de Cliente) está falhando em DISTRIBUIÇÃO, antes de
falhar em conversão.** EP01 (14/08): 21 views, 13 reach, 0 follows. EP02 (18/08):
17 views, 12 reach, 0 follows. EP03 (21/08): sem métrica ainda. Mediana de views de
Reel desde julho: **152**. Os episódios estão a ~1/8 da mediana — nenhum CTA de seguir
converte 17 pessoas. Predição (≥3,0 seg/1k) **não é avaliável** com esse alcance; a
hipótese não foi refutada, foi sufocada. Suspeitos: formato demo 17s em tela de
WhatsApp (zero rosto, zero som falado) sendo rebaixado pelo algoritmo, e/ou o selo
verde fixo sendo lido como "anúncio". Carrosséis da mesma semana (34 e 67 views)
confirmam que o grid inteiro está em baixa de alcance.

**Conclusão 4 — o melhor proxy disponível de aquisição é shares/1k com n de views.**
Share é o único sinal que leva o post a quem não segue. Com views ≥ 100 em 2026:
1. demo WhatsApp 08/06 — 93,5 sh/1k (139 views, n baixo ⚠️)
2. meme "grupo da família" 27/06 — 52,2 sh/1k (134 views, imagem, ⚠️)
3. **"NÃO CANCELE CONTRATOS" 13/08 — 51,7 sh/1k (232 views, Dr. Eduardo)**
4. **"Fale com o bot" 23/07 — 27,7 sh/1k (686 views — maior base de views entre os
   fortes, demo com link)**
5. Caso da Semana inquilinos 03/07 — 18,9 sh/1k (265 views)
Reel explicativo de lei fica em ~5 sh/1k. Carrossel: 0,9 sh/1k (n=35) — fora da
conversa de aquisição.

**Conclusão 5 — tema que compartilha é o da persona (prestador/contrato), não o tema
"quente" genérico.** Os 4 do topo são: bot resolve burocracia, golpe de PIX em
família, cancelamento de contrato, demo do produto. Banco de horas, plano de saúde,
herança, trânsito: todos ≤ 1 share.

**Decisão recomendada sobre "impulsionar pra sempre":**
- Não há base para "pra sempre" hoje. Impulsionamento contínuo de um post escolhido
  com 0 dados de seguidor é gasto cego (armadilha 4: paid infla views, R$/view cai,
  e ainda por cima não teremos follows no Buffer para saber se funcionou).
- Proposta: **teste pareado de 14 dias**, dois candidatos com mecanismos diferentes
  — "NÃO CANCELE CONTRATOS" (rosto do advogado, autoridade) × "Fale com o bot"
  (demo do produto) — mesmo orçamento, objetivo "mais visitas ao perfil", com
  campanha `/fale` própria em cada um. Medir seguidores no Insights nativo (não no
  Buffer) e no painel de anúncios. O que ganhar em **seguidores por R$** vira o
  "sempre ligado"; o outro desliga. Reavaliar a cada 30 dias — "pra sempre" é uma
  decisão renovada, não uma decisão única.
- Paralelo obrigatório: **diagnosticar o alcance da H013** antes do EP04 (25/08).
  Ver no Insights se os EPs foram classificados como Reel e qual a taxa de
  "não-seguidores" no alcance. Se continuarem ≤ 30 views, pausar a série e
  retrabalhar o formato (rosto/voz) em vez de queimar os 7 episódios restantes.
