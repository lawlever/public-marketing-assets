#!/usr/bin/env python3
"""Serie 'Frase de Cliente' — 10 episodios de topo, formato demo do WhatsApp.

Estrutura fixa de episodio (o ritual da serie):
  1. Rafa cola no chat da LawLever a frase que o cliente falou.
  2. A LawLever diz o que aquela frase realmente significa (o custo escondido).
  3. A LawLever diz o que vira prova / o que muda o jogo.
  4. A LawLever fecha com o que fazer da proxima vez (ganho emocional/social).

Camada: TOPO. Sem link, sem preco, sem "validar por advogado", sem status card.
"""
import json
import pathlib

BASE = pathlib.Path("/home/claude/serie")

# (ep, data_iso, frase_curta_capa, hook_categoria, momento, sub_nicho, msgs, legenda)
EPISODIOS = [
    dict(
        ep=1, data="2026-08-14T21:00:00.000Z", dia="sex 14/08",
        caption='"Pago semana que vem" — já são três.',
        hook="promessa específica", momento="receber", nicho="geral",
        bpm=85, trilha="SS_LD_85_keys_loop_trackstarter_sundaze_warm_wurli_g#.wav",
        query="warm mellow electric piano chords loop, reassuring and simple, documentary explainer bed",
        msgs=[
            ("user", 'Entreguei o projeto e o cliente falou "pago semana que vem". Já são 3 semanas.', "18:02"),
            ("bot", "Sem data combinada por escrito, não existe atraso — existe só um pedido seu. É isso que tira a sua força na hora de cobrar.", "18:02"),
            ("bot", 'Junte o que virou aceite: o "pode seguir" no WhatsApp, o orçamento aprovado e o comprovante da entrega. Isso é prova.', "18:03"),
            ("bot", "No próximo, combine data certa e o que acontece se atrasar. Aí o atraso tem consequência — e cobrar deixa de ser favor.", "18:03"),
        ],
        legenda=(
            'Cliente não paga e some depois da entrega? "Pago semana que vem" é a frase '
            "mais cara do prestador de serviço — e o problema quase nunca é o cliente: é "
            "não ter data nem consequência combinadas por escrito.\n\n"
            "O que segura: data certa de pagamento, o que acontece em caso de atraso, e o "
            "aceite registrado (o \"pode seguir\" no WhatsApp já conta).\n\n"
            "🎬 EP 01/10 da série FRASE DE CLIENTE — as 10 frases que todo prestador ouve, "
            "e o que cada uma custa quando não tem nada escrito.\n"
            "👉 Segue o perfil pra não perder a EP 02 (terça): a frase que faz você começar "
            "o serviço sem nada assinado.\n"
            "✉️ Manda pro colega que tá esperando pagamento agora.\n\n"
            "Conteúdo educativo — cada caso pode exigir análise específica.\n\n"
            "#FraseDeCliente #prestadordeservico #freelancer #mei #autonomo #cobranca "
            "#calote #contratos #lawlever"
        ),
    ),
    dict(
        ep=2, data="2026-08-18T21:00:00.000Z", dia="ter 18/08",
        caption='"Depois a gente assina, pode começar"',
        hook="choque numérico", momento="fechar", nicho="obra e reforma",
        bpm=80, trilha="SS_LD_80_keys_loop_kit05_dusk_electric_piano_f#.wav",
        query="warm mellow electric piano chords loop, reassuring and simple, documentary explainer bed",
        msgs=[
            ("user", 'O cliente disse "depois a gente assina, pode começar". Já comprei material e comecei.', "17:40"),
            ("bot", "Você adiantou material, hora e risco. Se ele desistir amanhã, a conta do que já saiu do seu bolso é sua.", "17:40"),
            ("bot", "Formalizar não é cartório. Uma proposta com escopo, prazo e valor + o \"aceito\" dele por escrito já é o combinado documentado.", "17:41"),
            ("bot", "Leva minutos e não atrasa o começo. O que atrasa mesmo é refazer o combinado no meio da obra.", "17:41"),
        ],
        legenda=(
            'Vai começar serviço sem contrato assinado? "Depois a gente assina" costuma '
            "custar caro para quem adianta material e mão de obra: sem nada escrito, o "
            "prejuízo do cliente desistir é todo seu.\n\n"
            "E formalizar não é cartório — proposta com escopo, prazo e valor mais o "
            '"aceito" por escrito já documenta o combinado.\n\n'
            "🎬 EP 02/10 da série FRASE DE CLIENTE.\n"
            "👉 Segue pra pegar a EP 03 (sexta): a frase de três palavras que come a sua "
            "margem sem você perceber.\n"
            "✉️ Manda pro colega que começa obra no fio do bigode.\n\n"
            "Conteúdo educativo — cada caso pode exigir análise específica.\n\n"
            "#FraseDeCliente #prestadordeservico #obraereforma #pedreiro #mei #autonomo "
            "#orcamento #contratos #lawlever"
        ),
    ),
    dict(
        ep=3, data="2026-08-21T21:00:00.000Z", dia="sex 21/08",
        caption='"É só um ajustezinho" (o terceiro)',
        hook="confissão", momento="operar", nicho="criativos/digital",
        bpm=90, trilha="SS_LD_90_keys_loop_kit03_eve_electric_piano_amp_f.wav",
        query="warm mellow electric piano chords loop, reassuring and simple, documentary explainer bed",
        msgs=[
            ("user", 'Terceiro "é só um ajustezinho" desse cliente. Já refiz o trabalho quase inteiro.', "19:10"),
            ("bot", "Ajustezinho nunca é um: é a soma. Um aqui, outro ali, e no fim do mês foi a sua margem que pagou a conta.", "19:10"),
            ("bot", "O que muda o jogo é o escopo fechado por escrito: quantas rodadas de revisão entram, e o que passa a ser trabalho novo.", "19:11"),
            ("bot", "Com isso combinado, o extra vira aditivo com preço e prazo. Cobrar deixa de ser climão e vira etapa normal do projeto.", "19:11"),
        ],
        legenda=(
            'Cliente pedindo alteração fora do escopo? "É só um ajustezinho" é a frase que '
            "mais corrói a margem de designer, dev, fotógrafo e social media — porque "
            "ajustezinho nunca é um só.\n\n"
            "O que resolve: escopo por escrito com número de revisões incluídas, e o extra "
            "virando aditivo com preço e prazo próprios.\n\n"
            "🎬 EP 03/10 da série FRASE DE CLIENTE.\n"
            "👉 Segue pra ver a EP 04 (terça): a frase de quem trabalha com hora marcada e "
            "leva bolo.\n"
            "✉️ Manda pro colega refém do ajustezinho.\n\n"
            "Conteúdo educativo — cada caso pode exigir análise específica.\n\n"
            "#FraseDeCliente #freelancer #designer #socialmedia #escopo #mei "
            "#prestadordeservico #vidadefreelancer #lawlever"
        ),
    ),
    dict(
        ep=4, data="2026-08-25T21:00:00.000Z", dia="ter 25/08",
        caption='"Cancelei, surgiu um imprevisto"',
        hook="pergunta provocativa", momento="operar", nicho="saúde/agenda",
        bpm=85, trilha="TL_Keys_Loops_WonderingKeys_A#_85.wav",
        query="warm mellow electric piano chords loop, reassuring and simple, documentary explainer bed",
        msgs=[
            ("user", "Terceiro cancelamento em cima da hora do mesmo cliente. Quem paga essa hora vaga?", "18:25"),
            ("bot", "Hoje, você. Quem trabalha com agenda vende tempo — e horário vazio não volta nem se remarca sozinho.", "18:25"),
            ("bot", "A política de cancelamento resolve antes de acontecer: prazo mínimo pra desmarcar e o que vale se cancelar depois disso.", "18:26"),
            ("bot", "O detalhe que faz funcionar é avisar no agendamento, não na hora do problema. Regra combinada antes não gera climão depois.", "18:26"),
        ],
        legenda=(
            "Cliente cancelou em cima da hora e deixou o horário vago? Quem atende com "
            "agenda — clínica, salão, personal, consultório — vende tempo, e tempo vago "
            "não volta.\n\n"
            "Política de cancelamento é o que transforma isso em regra: prazo mínimo pra "
            "desmarcar, o que vale depois do prazo, e o aviso feito no agendamento.\n\n"
            "🎬 EP 04/10 da série FRASE DE CLIENTE.\n"
            "👉 Segue pra pegar a EP 05 (terça): a frase mais cara da lista — e ela vem de "
            "um amigo.\n"
            "✉️ Manda pra quem tem agenda cheia de buraco.\n\n"
            "Conteúdo educativo — cada caso pode exigir análise específica.\n\n"
            "#FraseDeCliente #agenda #noshow #clinica #personaltrainer #salao "
            "#prestadordeservico #mei #lawlever"
        ),
    ),
    dict(
        ep=5, data="2026-09-01T21:00:00.000Z", dia="ter 01/09",
        caption='"A gente acerta na amizade"',
        hook="paradoxo", momento="sociedade", nicho="sócios",
        bpm=80, trilha="SS_LD_80_keys_loop_kit06_cloud_electric_piano_b.wav",
        query="warm mellow electric piano chords loop, reassuring and simple, documentary explainer bed",
        msgs=[
            ("user", 'Vou abrir CNPJ com um amigo. Ele falou "a gente acerta tudo na amizade".', "20:05"),
            ("bot", "Combinar por escrito não é desconfiança — é o contrário. O acordo existe pro dia em que a conversa ficar difícil.", "20:05"),
            ("bot", "Três perguntas que ninguém faz enquanto está tudo bem: quem trabalha mais ganha igual? se um sair, quem fica com o quê? e a carteira de clientes é de quem?", "20:06"),
            ("bot", "Respondam agora, enquanto vocês ainda concordam. É a hora mais barata de combinar.", "20:06"),
        ],
        legenda=(
            'Vai abrir empresa com amigo ou parente? "A gente acerta na amizade" é a frase '
            "que mais termina em sociedade quebrada — não por má-fé, mas porque ninguém "
            "combinou a regra enquanto estava tudo bem.\n\n"
            "As três perguntas que o acordo de sócios responde: dedicação x retirada, "
            "entrada e saída de sócio, e de quem é a carteira de clientes.\n\n"
            "🎬 EP 05/10 da série FRASE DE CLIENTE — metade da lista.\n"
            "👉 Segue pra ver a EP 06 (sexta): a frase educada que trava o seu orçamento "
            "por semanas.\n"
            "✉️ Manda pro seu futuro sócio antes de abrir o CNPJ.\n\n"
            "Conteúdo educativo — cada caso pode exigir análise específica.\n\n"
            "#FraseDeCliente #socios #sociedade #abrirempresa #cnpj #empreendedorismo "
            "#pequenosnegocios #mei #lawlever"
        ),
    ),
    dict(
        ep=6, data="2026-09-04T21:00:00.000Z", dia="sex 04/09",
        caption='"Vou ver com meu sócio e te falo"',
        hook="promessa específica", momento="fechar", nicho="geral",
        bpm=95, trilha="oc_key95_double_Abm7.wav",
        query="clean minimal explainer loop, soft keys and light percussion, calm confident business mood",
        msgs=[
            ("user", 'Mandei o orçamento e ele respondeu "vou ver com meu sócio e te falo". Sumiu.', "16:50"),
            ("bot", "Orçamento sem validade vira lembrete que ninguém lê. Ele fica em aberto, e o seu preço envelhece parado.", "16:50"),
            ("bot", "Coloque três coisas: até quando a proposta vale, o que exatamente está incluído, e como ele aceita (um \"aceito\" por escrito basta).", "16:51"),
            ("bot", "Prazo de validade não é pressão — é organização. E dá um motivo educado pra você voltar a falar com ele.", "16:51"),
        ],
        legenda=(
            "Mandou orçamento e o cliente sumiu? Proposta sem prazo de validade fica em "
            "aberto pra sempre — e o seu preço envelhece esperando resposta.\n\n"
            "Três itens que mudam isso: até quando a proposta vale, o que está incluído "
            '(e o que não está), e como o aceite é registrado. Um "aceito" por escrito '
            "já serve.\n\n"
            "🎬 EP 06/10 da série FRASE DE CLIENTE.\n"
            "👉 Segue pra pegar a EP 07 (terça): a frase que parece parceria e termina em "
            "trabalho de graça.\n"
            "✉️ Manda pro colega que tem 5 orçamentos parados.\n\n"
            "Conteúdo educativo — cada caso pode exigir análise específica.\n\n"
            "#FraseDeCliente #orcamento #proposta #freelancer #mei #prestadordeservico "
            "#autonomo #vendas #lawlever"
        ),
    ),
    dict(
        ep=7, data="2026-09-08T21:00:00.000Z", dia="ter 08/09",
        caption='"Você faz o meu, eu faço o seu"',
        hook="pergunta provocativa", momento="fechar", nicho="criativos/digital",
        bpm=85, trilha="SS_LD_85_keys_loop_trackstarter_royks_phaser_elec_piano_d.wav",
        query="warm mellow electric piano chords loop, reassuring and simple, documentary explainer bed",
        msgs=[
            ("user", 'Fechei uma permuta: "você faz o meu, eu faço o seu". Já entreguei. E agora?', "19:30"),
            ("bot", "Permuta é negócio, não favor. A pergunta que quase ninguém faz na hora é: e se o outro lado não entregar?", "19:30"),
            ("bot", "Por escrito ficam quatro coisas: o que cada um entrega, o valor equivalente de cada lado, os dois prazos, e o que vale se um não cumprir.", "19:31"),
            ("bot", "Combinar isso não estraga a parceria. Estraga é descobrir seis meses depois que só um lado entregou.", "19:31"),
        ],
        legenda=(
            "Fechou permuta ou parceria com outro prestador? Troca de serviço também é "
            'negócio: "você faz o meu, eu faço o seu" costuma terminar com um lado '
            "entregando e o outro enrolando.\n\n"
            "O que colocar no papel: o que cada um entrega, o valor equivalente dos dois "
            "lados, os prazos de cada um e o que vale se alguém não cumprir.\n\n"
            "🎬 EP 07/10 da série FRASE DE CLIENTE.\n"
            "👉 Segue pra ver a EP 08 (sexta): a frase que troca o seu desconto por uma "
            "promessa que ninguém cumpre.\n"
            "✉️ Manda pro parceiro de troca.\n\n"
            "Conteúdo educativo — cada caso pode exigir análise específica.\n\n"
            "#FraseDeCliente #permuta #parceria #freelancer #criativos #mei "
            "#prestadordeservico #lawlever"
        ),
    ),
    dict(
        ep=8, data="2026-09-11T21:00:00.000Z", dia="sex 11/09",
        caption='"Faz por menos que eu te indico"',
        hook="paradoxo", momento="fechar", nicho="geral",
        bpm=100, trilha="dc_perc_100_castle.wav",
        query="clean minimal explainer loop, soft keys and light percussion, calm confident business mood",
        msgs=[
            ("user", 'O cliente pediu desconto: "faz por menos que eu te indico pra muita gente".', "18:15"),
            ("bot", "Indicação é consequência de trabalho bem feito, não moeda. Ela não paga material, hora nem imposto.", "18:15"),
            ("bot", "Se for dar desconto, troque por algo real e escrito: pagamento à vista, entrada maior, prazo mais folgado ou escopo menor.", "18:16"),
            ("bot", "Desconto que vira cláusula é negociação. Desconto por promessa é só preço menor com o mesmo trabalho.", "18:16"),
        ],
        legenda=(
            "Cliente pedindo desconto em troca de indicação? Indicação é consequência de "
            "trabalho bem feito — ela não paga material, hora nem imposto.\n\n"
            "Se for negociar preço, troque por contrapartida real e escrita: pagamento à "
            "vista, entrada maior, prazo mais folgado ou escopo reduzido. Desconto que "
            "vira cláusula é negociação; desconto por promessa é só trabalhar por menos.\n\n"
            "🎬 EP 08/10 da série FRASE DE CLIENTE.\n"
            "👉 Segue pra pegar a EP 09 (terça): a frase inocente que entrega a autoria do "
            "seu trabalho.\n"
            "✉️ Manda pro colega que dá desconto e se arrepende depois.\n\n"
            "Conteúdo educativo — cada caso pode exigir análise específica.\n\n"
            "#FraseDeCliente #precificacao #desconto #freelancer #mei #prestadordeservico "
            "#autonomo #lawlever"
        ),
    ),
    dict(
        ep=9, data="2026-09-15T21:00:00.000Z", dia="ter 15/09",
        caption='"Manda o arquivo aberto que eu ajusto"',
        hook="confissão", momento="operar", nicho="criativos/digital",
        bpm=85, trilha="SS_LD_85_keys_loop_trackstarter_easy_elec_keys_motif_g.wav",
        query="warm mellow electric piano chords loop, reassuring and simple, documentary explainer bed",
        msgs=[
            ("user", 'Entreguei e o cliente pediu: "manda o arquivo aberto que eu ajusto aqui". Mandei.', "21:05"),
            ("bot", "Já vi muita gente descobrir depois que o trabalho continuou circulando editado — e sem crédito nenhum.", "21:05"),
            ("bot", "Pagar pelo serviço não é automaticamente ser dono de tudo. O que ele pode usar, alterar ou revender depende do que foi combinado.", "21:06"),
            ("bot", "Defina antes de entregar: o que é cessão, o que é uso licenciado e o que continua seu. Uma cláusula curta resolve.", "21:06"),
        ],
        legenda=(
            "Cliente pediu o arquivo aberto do seu trabalho? Pagar pelo serviço não "
            "significa automaticamente ser dono de tudo: o que ele pode usar, alterar ou "
            "revender depende do que foi combinado.\n\n"
            "Vale muito pra quem faz logo, identidade visual, site, código, texto e foto. "
            "Defina antes de entregar o que é cessão, o que é uso licenciado e o que "
            "continua seu.\n\n"
            "🎬 EP 09/10 da série FRASE DE CLIENTE.\n"
            "👉 Segue pra ver a EP 10 (sexta) — a última, e é sobre o dia do pagamento.\n"
            "✉️ Manda pro colega criativo que entrega tudo sem cláusula.\n\n"
            "Conteúdo educativo — cada caso pode exigir análise específica.\n\n"
            "#FraseDeCliente #direitosautorais #design #arquivoaberto #freelancer "
            "#criativos #mei #prestadordeservico #lawlever"
        ),
    ),
    dict(
        ep=10, data="2026-09-18T21:00:00.000Z", dia="sex 18/09",
        caption='"Vou parcelar em 3x, tudo bem?"',
        hook="choque numérico", momento="receber", nicho="geral",
        bpm=97, trilha="_OSS_NC_97_percussion_drum_loop_bongorainstick_6-8.wav",
        query="clean minimal explainer loop, soft keys and light percussion, calm confident business mood",
        msgs=[
            ("user", 'Na hora de pagar o cliente avisou: "vou parcelar em 3x, tudo bem?". Combinamos à vista.', "17:20"),
            ("bot", "Isso não é forma de pagamento, é mudança do combinado no dia do pagamento — quando você já entregou e perdeu poder de negociar.", "17:20"),
            ("bot", "Se topar, vire regra: valor de cada parcela, datas e o que acontece se uma atrasar. Um aceite por escrito já formaliza.", "17:21"),
            ("bot", "E na próxima, combine antes: forma de pagamento faz parte do preço, não é detalhe do final.", "17:21"),
        ],
        legenda=(
            "Cliente quer parcelar depois do serviço entregue? Mudar a forma de pagamento "
            "no dia de pagar não é detalhe: é renegociar o combinado no momento em que "
            "você já entregou e tem menos poder de negociação.\n\n"
            "Se aceitar, transforme em regra: valor de cada parcela, datas e o que "
            "acontece se uma atrasar. E, no próximo, combine a forma de pagamento junto "
            "com o preço.\n\n"
            "🎬 EP 10/10 — fim da série FRASE DE CLIENTE.\n"
            "👉 Segue o perfil: semana que vem começa a próxima série, sobre o que fazer "
            "quando o cliente já sumiu com o seu dinheiro.\n"
            "✉️ Manda pro colega que ouviu essa essa semana.\n\n"
            "Conteúdo educativo — cada caso pode exigir análise específica.\n\n"
            "#FraseDeCliente #parcelamento #cobranca #freelancer #mei #prestadordeservico "
            "#autonomo #contratos #lawlever"
        ),
    ),
]


def roteiro(e):
    msgs = [{"id": 1, "kind": "date", "label": "HOJE"}]
    for i, (sender, text, time) in enumerate(e["msgs"], start=2):
        m = {"id": i, "kind": "text", "sender": sender, "text": text, "time": time}
        if i == len(e["msgs"]) + 1:
            m["pause"] = 1.5
        msgs.append(m)
    return {
        "hdr": {"title": "LawLever", "sub": "online", "caption": e["caption"]},
        "speed": 1.5,
        "msgs": msgs,
    }


if __name__ == "__main__":
    plano = []
    for e in EPISODIOS:
        p = BASE / f"ep{e['ep']:02d}.json"
        p.write_text(json.dumps(roteiro(e), ensure_ascii=False, indent=2))
        plano.append({k: v for k, v in e.items() if k != "msgs"})
        print(f"ep{e['ep']:02d} · {e['dia']} · {e['caption']}")
    (BASE / "plano.json").write_text(json.dumps(plano, ensure_ascii=False, indent=2))
    print(f"\n{len(EPISODIOS)} roteiros escritos.")
