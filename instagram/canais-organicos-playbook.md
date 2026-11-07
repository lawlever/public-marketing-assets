# Canais orgânicos da LawLever — playbook operacional (zero verba)

Este arquivo é o "como fazer" da seção "Além do Instagram" do doc *Virada do Instagram LawLever*. Cada bloco cabe em 10 a 30 minutos por dia de alguém que não é o Eduardo. O Eduardo só grava e aprova.

---

## 1. O mesmo vídeo em cinco vitrines (TikTok, YouTube Shorts, Kwai, Facebook Reels, Instagram)

**Regra de ouro:** um vídeo gravado, cinco uploads nativos no mesmo dia, nenhum deles com marca-d'água de outra plataforma. O arquivo final sai da edição (MP4 1080×1920, sem logo do TikTok/Instagram) e é subido direto em cada app.

| Vitrine | Como publicar | Legenda e detalhes | Link para o bot |
| --- | --- | --- | --- |
| Instagram (Reel) | Buffer, como hoje | Primeira linha = a dúvida; pergunta de comentário no fim; 3 a 5 hashtags | Bio (lawlever.ai/fale/ig-bio) e DM por palavra-chave |
| TikTok | App do TikTok (Studio permite agendar) | Título com a dúvida em palavras-chave de busca ("cliente não pagou o que fazer"); 3 hashtags; texto na tela já está no vídeo | Bio (link liberado para contas business); comentário fixado com "lawlever.ai/fale" |
| YouTube Shorts | YouTube Studio (agendável) | Título = a dúvida; descrição = resposta em 3 linhas + link; é o único canal em que o link na descrição é clicável e indexado pelo Google | Descrição e comentário fixado |
| Kwai | App do Kwai | Mesmo título do TikTok; legenda curta; público mais popular (classes C e D), tema de consumo e trabalho rende mais | Bio |
| Facebook (Reel) | Meta Business Suite, compartilhando o Reel do Instagram para a Página | Mesma legenda; Facebook é onde os grupos de MEI vivem, e o Reel pode ser repostado nos grupos | Bio da Página e comentário |

**Ordem de publicação no dia:** TikTok e Kwai de manhã (9h), Instagram e Facebook ao meio-dia, Shorts às 18h. Cada plataforma avalia o vídeo pelos próprios sinais; o que dá certo em uma vira indício para as outras.

**Perfil igual em todas:** nome "LawLever · Dr. Eduardo responde", mesma foto (rosto do Eduardo), mesma bio de três linhas, mesmo link. Quem descobre o Eduardo no TikTok procura "lawlever" no Instagram; a consistência é o que faz a conta ser encontrada.

**Códigos de campanha:** `tt-bio`, `yt-bio`, `kw-bio`, `fb-bio` (registrar na API antes de colocar os links — regra da skill lawlever-experimentos). Assim o funil /fale mostra qual vitrine traz gente de verdade.

## 2. O WhatsApp como canal próprio

O produto mora no WhatsApp; a distribuição tem que morar lá também. Três peças, todas gratuitas (diferente de mensagem de marketing iniciada pela empresa, que é paga por conversa):

1. **Canal do WhatsApp "LawLever Responde"** (Atualizações → Canais → Criar canal). Um post por dia útil: a dúvida do Reel do dia, a resposta em 3 linhas, o link do bot e o link do vídeo. Pedir para seguir o canal no fim de cada Reel e no fecho de cada conversa do bot ("quer receber uma resposta dessas por dia? segue o canal"). Canais aparecem na busca de canais e em "canais sugeridos"; crescem pelo nome e pelo compartilhamento do link.
2. **Rodapé em todo documento gerado:** "Documento criado na LawLever, seu advogado no bolso · lawlever.ai/fale". Cada contrato, proposta ou notificação que o usuário manda para o cliente dele é um impacto em alguém que ainda não conhece a LawLever, no momento exato em que essa pessoa está lidando com um problema jurídico. São 135 documentos a cada 90 dias hoje; é o loop mais barato que existe e só precisa de uma linha de código (prompt na seção 10 do doc).
3. **"Manda pra um amigo" depois da resposta:** ao fim de uma resposta bem avaliada, o bot oferece um link pronto (`https://wa.me/?text=...`) com uma frase na primeira pessoa ("Esse bot me respondeu uma dúvida de graça, olha: lawlever.ai/fale"). Compartilhar é um toque. Medir com o código `wa-share`.

Status do WhatsApp Business: repostar o Reel do dia como status (gratuito, alcança quem tem o número salvo).

## 3. Google: cada resposta vira uma página

Toda dúvida respondida vira uma página em lawlever.ai/responde/<slug> com: a pergunta como título (H1), a resposta do Eduardo em 150 a 300 palavras, o vídeo incorporado, o bloco "Na dúvida, pergunta pra LawLever" com o link do bot, e marcação de FAQ (schema.org/FAQPage). São 29 páginas no primeiro mês, uma por roteiro; depois, uma por Reel novo. O Google também indexa os posts públicos do Instagram desde julho de 2025, então a primeira linha da legenda deve ter a pergunta inteira, do jeito que as pessoas digitam.

Por que vale: as buscas são de cauda longa e repetem o que as pessoas perguntam no bot ("cliente não pagou o que fazer", "caução não devolvida o que fazer", "golpe do pix como recuperar"); a concorrência é JusBrasil e escritórios; uma página de resposta curta, com vídeo e um advogado identificado, é exatamente o que o Google favorece em "perguntas frequentes". Hoje a LawLever paga pelo Google (103 usuários em 90 dias pelo `gadsobra`); o orgânico compõe sem custo.

Prompt para o Claude Code: seção 10 do doc.

## 4. Comunidades: responder onde a dúvida já existe

**Onde:** grupos de Facebook de MEI, freelancers, designers, arquitetos, inquilinos e "direito do consumidor"; comunidades de WhatsApp e Telegram de prestadores; Reddit (r/brasil, r/empreendedorismo); JusBrasil (perguntas e respostas). A lista com tamanhos está no doc (seção 8).

**Como (OAB-safe):** o Eduardo (ou a conta LawLever) responde 3 dúvidas por dia, com a regra geral, sem link e sem "me contrata". O perfil faz o trabalho: foto, nome e bio com o caminho. Quem gostou da resposta clica no nome. Link só quando o grupo permite e quando alguém pede. Nunca copiar e colar a mesma resposta em vários grupos.

**O que responder:** as mesmas dúvidas dos roteiros. Cada resposta boa em grupo vira candidata a Reel ("essa pergunta apareceu três vezes essa semana").

## 5. Collabs e participações (2 por mês)

**Alvo:** contas de 5 mil a 300 mil seguidores que falam com prestadores de serviço (contadores para MEI, criadores de freelancer, arquitetura e obra, saúde autônoma) ou com o cidadão em apuros (consumo, aluguel, finanças pessoais). Lista no doc (seção 8).

**A proposta (DM ou e-mail, 5 linhas):**

> Oi, [nome]. Sou o Nicholas, da LawLever. O Dr. Eduardo Poletto responde dúvidas jurídicas de quem vive de vender serviço em vídeos de 30 segundos. Vi que sua audiência pergunta muito sobre [tema]. Proposta: ele grava uma resposta para a dúvida mais comum dos seus seguidores, vocês publicam como post em colaboração (aparece nos dois perfis) e você não gasta nada. Posso mandar 3 opções de pergunta?

**Formato:** post em colaboração (Collab) com a conta maior publicando; o Reel é o Eduardo respondendo a pergunta da audiência do parceiro, com o nome do parceiro na primeira frase. Podcasts e lives: o Eduardo como convidado respondendo dúvidas ao vivo, sempre com a regra geral.

## 6. Imprensa: o Eduardo como fonte

Quando sai uma lei nova (fim da 6x1, MEI de R$ 110 mil, regras da ANAC, Black Friday), jornalistas precisam de advogado para comentar no mesmo dia. Pitch de 4 linhas para a redação ou o jornalista do tema, nas primeiras 24 horas:

> Assunto: Fonte — [tema] explicado para o pequeno prestador de serviço
> Oi, [nome]. O Dr. Eduardo Poletto (OAB/SC 55.722), advogado da LawLever, pode comentar hoje [tema] do ponto de vista de quem é MEI ou autônomo: [uma frase com o ângulo e um dado]. Atende por telefone ou áudio em até 1 hora. Também temos [um número próprio: ex. "4.660 dúvidas recebidas no bot em 90 dias, 30% sobre cobrança"].

Toda citação na imprensa vira post ("o Eduardo explicou no [veículo]") e link para o site (ajuda o Google).

## 7. O perfil pessoal do Eduardo

Criar ou reativar @eduardopoletto.adv com a mesma foto e bio; todo Reel sai como colaboração entre @lawlever e o perfil pessoal (dois grids, dois públicos, um upload). Nos benchmarks e nos casos brasileiros, o rosto pessoal cresce mais rápido que a marca; a marca ganha pela associação.

## 8. Rotina semanal (quem faz o quê, sem o Eduardo)

| Dia | 30 minutos de operação |
| --- | --- |
| Segunda | Subir os 5 vídeos da semana nas cinco vitrines (agendados); post do canal do WhatsApp; 3 respostas em grupos |
| Terça | Responder comentários e DMs em todas as plataformas; 3 respostas em grupos; mandar 2 pitches de collab |
| Quarta | Escolher o comentário que vira o Reel de quarta; canal do WhatsApp; 3 respostas em grupos |
| Quinta | Pauta em alta da semana (pesquisa + briefing para a gravação); pitch de imprensa se houver lei nova |
| Sexta | Leitura da semana (Buffer + Insights nativo + TikTok Studio + YouTube Studio); registrar o que funcionou em conclusions.md |

Tudo isso cabe em 2 horas e meia por semana de uma pessoa, mais os 90 minutos de gravação do Eduardo.
