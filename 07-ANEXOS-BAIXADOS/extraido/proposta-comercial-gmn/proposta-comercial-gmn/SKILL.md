---
name: proposta-comercial-gmn
description: Monta a proposta comercial do serviço de Perfil da Empresa no Google (Google Meu Negócio) em PDF, com a logo e as cores da agência do próprio consultor, a partir dos dados do GBPCheck e do preço que o consultor já definiu na Calculadora de Preços. Trabalha em quatro modos: criação de perfil novo, reivindicação de perfil sem dono, correções em perfil existente, e apenas o acompanhamento mensal. Entrega o PDF da proposta e a mensagem de WhatsApp para enviar junto, além da versão de entrega presencial. Use SEMPRE que o consultor pedir para "montar a proposta", "fazer a proposta do cliente", "gerar o PDF da proposta", "proposta comercial de Google Meu Negócio", ou quando anexar o relatório de Ranking do GBPCheck e falar em fechar o cliente. NÃO use para o relatório mensal do cliente (skill relatorio-mensal-cliente-gmn) nem para criar o conteúdo do perfil (skill perfil-google-negocio).
---

# Proposta comercial de Google Meu Negócio (Escola de SEO)

Esta skill transforma o diagnóstico que o consultor já levantou em uma proposta comercial pronta para entregar, em PDF, com a marca da agência dele.

A lógica da proposta é uma só: **primeiro o cliente vê onde ele está, depois vê o que será feito, e só então vê o preço.** Proposta que abre com serviço e valor é orçamento. Proposta que abre com diagnóstico é consultoria.

Dois insumos vêm prontos do consultor e a skill nunca inventa:

1. **Os dados do GBPCheck**, do relatório de Ranking e da análise de saúde do perfil. A skill lê o que foi enviado e escreve a leitura. Ela não estima posição, não deduz número e não completa lacuna com suposição.
2. **O preço**, que o consultor definiu na Calculadora de Preços do módulo 12. A skill não sugere valor, não opina se está caro ou barato e não calcula desconto. Se o consultor não trouxer o preço, ela para e manda ele voltar à planilha.

## Passo 0: descobrir o modo antes de qualquer coisa

A primeira pergunta define o documento inteiro, porque a redação muda completamente. Pergunte antes de tudo:

**"O que será orçado nesta proposta?"**

A pergunta é sobre o que vai ser vendido, não sobre o desfecho da venda. Nada foi fechado ainda: quem vai receber este documento é um prospect, um possível cliente.

1. **Criação de um perfil novo:** o negócio não tem perfil no Google. O diagnóstico é a ausência, e a página 2 mostra o que os concorrentes já ocupam enquanto ele não aparece. O prazo inclui a verificação pelo Google.
2. **Reivindicação de um perfil que existe sem dono:** o perfil está no ar, criado pelo Google ou por usuários, e ninguém o administra. A primeira entrega do setup é a reivindicação, e só depois vêm as correções. Diga com clareza que o prazo dessa etapa **depende do Google**, e nunca prometa que a reivindicação será aprovada: a decisão não é do consultor.
3. **Correções em um perfil que já existe:** o perfil está no ar e tem dono. É o caso mais comum na prospecção, e o diagnóstico é o mais forte, porque existe nota, histórico e comparação com concorrentes. O setup inclui a transferência de acesso, caso ele feche. Como o perfil já está verificado, não existe espera do Google.
4. **Apenas o acompanhamento mensal:** o perfil já está ajustado e não há setup a orçar. A proposta traz **opção única** de preço, e a página de plano de trabalho mostra só a rotina do mês.

Quando há setup a orçar (criação, reivindicação ou correções), a proposta traz sempre duas opções de preço. No modo apenas acompanhamento, uma só.

Depois disso, faça as perguntas em **três blocos, um por mensagem**, uma lista numerada por vez. Espere as respostas de um bloco antes de mandar o próximo. Nada de parágrafo de explicação entre as perguntas.

## Passo 1: bloco 1, a marca da agência

Este bloco o consultor preenche uma vez só. No fim da entrega, devolva tudo em um bloco pronto para ele colar na próxima proposta e pular direto para o bloco 2.

1. Nome da agência ou do seu negócio, como ele aparece para quem contrata.
2. Anexe a logo (PNG ou JPG, de preferência com fundo transparente).
3. Cor principal da marca, em código hexadecimal, se souber. Se não souber, diga a cor e eu escolho um tom.
4. Site, telefone ou WhatsApp e e-mail de contato.
5. Nome de quem assina a proposta.

Se o consultor não tiver logo, siga sem ela e monte o cabeçalho apenas com o nome, em tipografia limpa. Não invente marca, não gere logo e não sugira nome de agência.

## Passo 2: bloco 2, o prospect e o diagnóstico

6. Nome do negócio, segmento e cidade.
7. O que o dono do negócio disse que quer (mais clientes, aparecer no Maps, sair na frente de um concorrente específico). Use as palavras dele.
8. Qual termo de busca foi analisado (ex.: "dentista em Brusque").
9. Anexe os arquivos do GBPCheck. **O que pedir depende de o perfil já estar publicado ou não:**

**Quando o perfil já está publicado** (reivindicação, correções ou apenas acompanhamento), os arquivos são do próprio prospect. Perfil sem dono também está no ar, aparece nas buscas e tem posição medível: peça a grade dele normalmente.

**Quando o perfil não existe** (modo criação), não há grade dele. Aí o relatório é **opcional** e, se vier, é o do concorrente mais forte da cidade para o termo principal. Veja abaixo como a proposta se comporta com e sem ele. O Pre Health Check não se aplica, porque não há perfil para analisar.

Os arquivos:

**a) O Pre Health Check do perfil**, em PDF, gerado pela extensão. É de onde saem a nota do perfil e os pontos que estão faltando. Não se aplica no modo criação.

**b) O PDF de exportação da grade da palavra principal**, em Ranking, Histórico. Do próprio prospect quando o perfil já está publicado, do concorrente mais forte no modo criação (e aí é opcional). É a base do diagnóstico: dele saem em quantos pontos da grade o perfil foi encontrado, o compartilhamento de voz local, a posição na lista de concorrentes e o total de concorrentes. **É este arquivo que sustenta os números da proposta.**

**c) O print da grade em PNG**, tirado direto da tela, em Ranking, Histórico. A grade que vem dentro do PDF fica borrada quando ampliada, e esta é a imagem que o cliente mais olha. Por isso vem separada, em boa resolução.

Se quiser, mande também prints de outras palavras que você rodou. Eles entram como apoio quando mostram um padrão, por exemplo o perfil bem posicionado numa palavra e ausente em outra. **Use no máximo uma palavra de apoio além da principal:** quatro grades diferentes na mesma proposta confundem o leitor e diluem o argumento.
10. Como você trata essa pessoa: por você ou por senhor? (mantenha o mesmo tratamento no PDF e nas mensagens)
11. Quer incluir o volume de busca da região? Se sim, me diga de dois a quatro termos além do principal (ex.: "dentista", "implante dentário", "clínica odontológica"). Se não quiser, seguimos sem essa página.

Se o consultor pular o bloco de dados e pedir a proposta assim mesmo, **não invente diagnóstico**. Ou ele traz os números, ou a página de diagnóstico sai fora e a proposta fica mais fraca. Diga isso claramente e deixe ele escolher.

## Passo 3: bloco 3, escopo, preço e prazo

12. Preço do **setup avulso**, sem acompanhamento. No modo apenas acompanhamento, pule esta e a próxima.
13. Preço do **setup dentro do contrato**, quando o cliente fecha o acompanhamento junto.
14. Preço da mensalidade, e por quantos meses vai o contrato.
15. O que entra no mês: quantas postagens, se responde avaliação, se entrega relatório e em que dia, com que frequência fala com ele.

**O grupo de WhatsApp é item fixo da rotina mensal e precisa aparecer na página do plano de trabalho.** É o que diferencia o serviço de quem some por trinta dias e reaparece com um PDF, e é o mesmo compromisso que vai para o contrato. Descreva como um grupo com o dono e a equipe, onde toda semana é avisado o que foi feito, as avaliações que chegaram e o que foi respondido. Se o consultor não trabalhar assim, ele pede para tirar.
16. Formas de pagamento que você aceita (boleto, Pix, cartão, parcelamento) e em que momento o pagamento acontece.
17. O acompanhamento tem fidelidade ou pode ser cancelado a qualquer momento? Se tiver alguma condição (por exemplo, devolver o desconto do setup em caso de saída antecipada), me diga qual.
18. Validade da proposta em dias.
19. Alguma condição especial combinada com ele (desconto, escopo diferente)?

Se o preço não vier, pare: "Volte na Calculadora de Preços e me traga os valores. Eu não defino preço, porque o número precisa fechar a sua conta, não a minha."

**A regra dos dois setups.** O setup avulso é sempre mais caro que o setup dentro do contrato. Não é castigo ao cliente, é preço honesto: trabalho pontual não tem continuidade, não gera previsibilidade e ainda obriga o consultor a prospectar outro cliente no mês seguinte. Com essa diferença no papel, o cliente enxerga sozinho que assinar o acompanhamento sai melhor, e o consultor não precisa de nenhum argumento de venda.

Se o consultor informar um setup avulso **igual ou menor** que o do contrato, pare e avise antes de gerar: assim a proposta empurra o cliente para a opção avulsa, que é justamente o que faz o serviço recorrente morrer.

## Passo 4: como ler os dados do GBPCheck (a parte mais importante)

O texto do diagnóstico é escrito para um dono de negócio, não para um profissional de SEO.

**Nunca use sigla no texto do cliente.** ARP, ATRP, SoLV e PE não entram na proposta. Eles podem aparecer dentro do print, porque o print é a evidência, mas a conclusão vem escrita em português comum.

**A regra da ordenação.** Na lista de concorrentes do GBPCheck, a ordem de 1 até o último não é qualidade de perfil: é compartilhamento de voz local, com desempate por posição média. Por isso um perfil sem avaliação nenhuma pode aparecer acima de um perfil bem cuidado. Ao citar a posição, escreva **"posição X de Y em visibilidade para o termo pesquisado"**, nunca "posição X em qualidade de perfil" e nunca "posição X no Google".

**A leitura que convence é o contraste.** Procure sempre a tensão entre o que o cliente já tem e o resultado que ele não tem. Os padrões mais fortes:

- Aparece em muitos pontos da grade e nunca entre os três primeiros.
- Tem mais avaliações que um concorrente que está na frente dele.
- Aparece bem só no ponto do próprio endereço e some conforme a busca se afasta.
- Tem nota alta e aparece em poucos pontos da cidade.

Escreva de três a cinco frases curtas, cada uma com um fato verificável no material enviado. Exemplo de tom:

> "Hoje o seu perfil aparece nas 49 buscas feitas em Brusque, ou seja, na cidade inteira. Em nenhuma delas ele aparece entre os três primeiros resultados. A clínica que hoje aparece em primeiro em quase toda a cidade tem 73 avaliações. A sua tem 116."

**O que nunca entra:** o mapa de calor (mostra concentração de concorrentes, não desempenho do cliente, e confunde o leigo), a tabela completa de 60 linhas (recorte de 5 a 8 linhas com o cliente e os concorrentes diretos) e qualquer coluna que precise de explicação.

### Quando o perfil não existe (modo criação)

**Nunca apresente a ausência como se fosse uma medição.** Escrever "você aparece em 0 dos 49 pontos" é dizer o óbvio: ele aparece em zero porque não tem perfil. Isso gasta o espaço mais nobre da página com a informação menos útil, e o dono percebe que não há descoberta nenhuma ali.

Atenção: isto vale **só para a criação**. Perfil não reivindicado está publicado, aparece nas buscas e tem grade própria, então ali o diagnóstico é normal, sobre o perfil dele mesmo. E costuma ser forte, porque perfil sem dono quase sempre está incompleto, sem postagem e sem resposta a avaliação.

**Com o relatório do concorrente.** O diagnóstico é **o mercado que ele não está disputando**, montado com três fatos:

1. **Quantos negócios competem** por aquele termo na cidade. É o número de impacto da página, no lugar do zero.
2. **O que têm os que lideram:** quantas avaliações, que nota, em quanto da cidade aparecem bem. Isso mostra a régua de entrada e prepara o preço.
3. **Que só existir não basta:** procure na lista um perfil com nota alta e muitas avaliações que mesmo assim aparece mal. É a prova de que o trabalho não é só criar a ficha, e é o que justifica o acompanhamento mensal.

Some a isso o volume de busca, quando consultado. Um número grande de buscas em uma cidade onde ele não aparece é a melhor abertura possível para a página de investimento.

**Sem o relatório do concorrente.** O consultor não é obrigado a levantar isso, e a proposta precisa funcionar bem assim. Nesse caso:

- **Não invente número nenhum.** Nada de estimar quantos concorrentes existem, quantas avaliações eles têm ou como a cidade se comporta. Sem dado, não há afirmação.
- A página 2 deixa de ser diagnóstico e passa a ser **o que existe hoje sobre o negócio no Google**: que não há perfil, que quem procura por aquele termo na cidade encontra outros negócios, e o que um perfil bem feito precisa ter para entrar nessa disputa.
- Se o volume de busca foi consultado, ele vira o número de impacto da página e carrega o argumento sozinho: tantas pessoas procuram por mês na cidade, e hoje o negócio não aparece para nenhuma delas.
- Se não houver volume nem relatório, **a página 2 sai da proposta**. O documento começa direto no plano de trabalho, e fica com cinco páginas. Proposta mais curta e honesta é melhor que página de diagnóstico preenchida com suposição.
- A página do mapa também sai, porque não existe grade para mostrar.

Ao entregar sem o relatório, diga ao consultor em uma linha o que ele ganharia levantando a grade do concorrente, para ele decidir se vale refazer. Não insista mais que isso.

**Quando o mapa do concorrente entrar, ele exige cuidado redobrado.** Ele é do concorrente, não do prospect, e precisa estar rotulado assim já no título, algo como "como a cidade se comporta nessa busca hoje". Sem isso, o dono olha uma grade cheia de primeiros lugares e leva alguns segundos achando que é dele, o que é confuso e parece desonesto quando ele entende. Se o rótulo não couber com clareza, é melhor tirar a página do mapa e deixar o argumento com a tabela e o volume.

Uma frase que resume bem o espírito desta página: o objetivo não é mostrar que ele está mal, é mostrar que ele **ainda não entrou** em uma disputa que já está acontecendo sem ele.

## Passo 4b: volume de busca (opcional, via DataForSEO)

Só faça esta consulta se o consultor pediu na pergunta 11. Ela não é obrigatória, e a proposta funciona bem sem ela. Quando entra, é um diferencial forte na apresentação, porque tira a conversa do "aparecer no Google" abstrato e coloca um número de pessoas procurando.

Consulte o volume via DataForSEO com a localização da cidade do cliente, para o termo principal e para os termos que o consultor listou. Traga o volume mensal de cada um.

**Como apresentar, sem enganar:**

- O volume é da **cidade ou região**, nunca do bairro ou da quadra. Diga isso em uma linha de rodapé, porque um número inflado destrói a confiança se o cliente conferir depois.
- Some os termos e apresente o total como **oportunidade mensal da região**, não como visitas garantidas ao perfil.
- Nunca converta volume em clientes, em faturamento ou em retorno estimado. "300 pessoas procuram por mês, então você vai ganhar X" é promessa que não se sustenta.
- Ligue o volume ao diagnóstico numa frase só: quantas pessoas procuram por mês e o fato de que hoje o perfil não aparece entre os primeiros para elas.
- Se um termo tiver volume muito baixo ou zero, mostre assim mesmo. Omitir dado ruim é o começo da proposta desonesta.

Essa página entra logo depois do mapa e antes do plano de trabalho.

**Nunca cite o nome da ferramenta de dados na proposta nem na conversa com o cliente.** O número é seu levantamento, e a fonte é informação interna do consultor.

## Passo 5: o que a proposta nunca promete

Estas regras valem para todo o documento e não têm exceção:

- **Nunca prometa posição.** Nada de "vamos te levar ao top 3", "primeira página garantida" ou "posição 1 em 90 dias". A proposta promete **trabalho**, não resultado de terceiro.
- **Nunca prometa prazo de resultado.** Você não controla o algoritmo do Google nem o movimento dos concorrentes.
- **Nunca cite ganho financeiro estimado** ("você vai faturar X a mais"). Não há como sustentar.
- **Nunca compare preço com concorrente** nem diga que o serviço é barato.
- Em cliente de profissão regulamentada (saúde, advocacia, contabilidade), mantenha o tom informativo e sóbrio, sem superlativo e sem linguagem de venda agressiva.

O que a proposta pode afirmar com segurança: o que está errado hoje (é verificável), o que será feito (depende de você) e com que frequência (depende de você).

## Passo 6: estrutura do PDF (sempre esta)

Seis páginas, ou sete quando entra o volume de busca. Nunca mais que isso: proposta longa não é lida.

**Regra de impressão, vale para o documento inteiro.** A proposta é feita para ser impressa e entregue na mão. **Nunca use fundo chapado de cor em página inteira**: gasta tinta, sai manchado em impressora comum e o texto claro sobre cor forte fica ilegível em papel comum. A cor da agência entra em títulos, linhas, ícones, bordas e blocos pequenos, sobre fundo branco. Blocos coloridos, quando houver, ocupam no máximo um quarto da página e usam tom claro com texto escuro.

**Página 1, capa.** Fundo branco. Logo da agência no topo, título grande em cor da marca, nome do prospect em bloco com borda, o termo analisado, a data e a validade. Uma faixa fina de cor no topo é suficiente para dar identidade.

O título precisa dizer **de qual Google se trata**. "Posicionamento no Google" é ambíguo e faz o leitor pensar em anúncio pago. Escreva sempre "Perfil da Empresa no Google" ou "Google Meu Negócio" no título ou no subtítulo. E **não use a logo do Google** em nenhuma página: dá a entender uma parceria ou credenciamento que não existe, e as diretrizes de marca do Google não permitem esse uso. O texto resolve com segurança total.

Na diagramação da capa, o bloco central (kicker, título e subtítulo) fica **centralizado verticalmente** no espaço entre a logo e o rodapé. Preso ao topo, sobra um vazio grande no meio da página e a capa parece inacabada.

**Página 2, onde você está hoje.** O número de impacto em destaque (a posição em visibilidade), a leitura em três a cinco frases e o quadro comparativo com o cliente e os concorrentes diretos. No modo criação, o número de impacto **não é o zero dele**, é o tamanho do mercado ou o volume de busca, e a página pode até sair da proposta. Veja a seção "Quando o perfil não existe".

**Página 3, o mapa.** A imagem da grade ocupa a página quase inteira, com uma linha explicando que cada círculo é uma busca e o número é a posição. No modo criação, quando houver grade de concorrente, o título precisa deixar claro que ela é do concorrente e serve para mostrar como a cidade se comporta. Sem grade, esta página não existe. Espremida junto do diagnóstico, ela fica pequena demais para o cliente ler os números, e é justamente o que ele mais olha. Sempre em página própria.

**Página 4, o que vamos fazer.** Duas colunas. À esquerda, o setup, com as entregas listadas (na reivindicação começa por ela, nas correções pela transferência de acesso). À direita, o mês a mês, com o que se repete. Uma linha final: "o setup arruma o perfil, a rotina mensal é o que mantém e melhora a posição".

**O grupo de WhatsApp é item fixo da rotina mensal**, e não pode faltar. É o que diferencia o serviço de quem some por trinta dias e reaparece com um PDF. Descreva assim: um grupo com o dono e a equipe dele, onde toda semana é avisado o que foi feito, as avaliações que chegaram, o que foi respondido e o que está previsto. Quem acompanha semana a semana não questiona a mensalidade no fim do mês. Se o consultor não trabalhar dessa forma, ele pede para tirar.

**Página 5, investimento.** Sempre duas opções, lado a lado, com a segunda destacada:

- **Opção 1, avulsa:** somente o ajuste ou a criação do perfil, entrega única, sem acompanhamento. Valor cheio, à vista.
- **Opção 2, completa:** o mesmo trabalho mais o acompanhamento mensal pelo período do contrato. Mostre o setup reduzido, a mensalidade, o total do período e a forma de pagamento.

**O total do período vem sempre acompanhado da condição de saída.** Um número cheio sozinho assusta, e omiti-lo é pior, porque o cliente faz a conta de cabeça e conclui que você escondeu. Quando não há fidelidade, escreva a liberdade ao lado do total, na mesma linha de leitura: sem fidelidade, sem multa, cancele quando quiser. É isso que desarma o valor grande. Quando houver alguma condição de saída, ela aparece com a mesma clareza, nunca em letra miúda.

Não escreva nenhuma frase empurrando a opção 2. A diferença de valor entre os dois setups já faz esse trabalho, e quem decide sozinho fecha mais. No modo apenas acompanhamento, opção única.

Nesta mesma página, em destaque visível, as condições de prazo. **Elas mudam conforme o modo:**

- **Criação de perfil novo:** execução concluída em até 3 dias úteis; a confirmação do perfil pelo Google pode levar até 7 dias úteis, ou mais, se o Google pedir comprovação por vídeo ou outro método; **a cobrança é feita somente após a aprovação do perfil**. Essa última linha tira o risco de quem contrata e é argumento forte: nunca a esconda no meio das condições.
- **Reivindicação de perfil sem dono:** mesma lógica da criação, com uma ressalva escrita no documento: o prazo da reivindicação depende da análise do Google e não do consultor. As correções começam assim que o acesso for liberado.
- **Correções em perfil existente:** o perfil já está verificado, então não existe espera do Google. Prazo é só o de execução, e o pagamento acontece na entrega do perfil ajustado. Não cite verificação nem prazo do Google aqui, porque não se aplica e só gera dúvida.
- **Apenas acompanhamento:** não há prazo de setup. Informe a data de início da rotina e o dia do mês em que o relatório é entregue.

**Página 6, o combinado.** Três blocos curtos:
- **O que depende de você:** acesso ao perfil, fotos reais do negócio, aprovação dos temas dos posts, e pedir avaliação aos clientes no balcão. Este bloco protege o consultor quando o resultado demora.
- **O que não está incluso:** criação de site, gestão de redes sociais, anúncios pagos, produção de vídeo, e o que mais estiver fora do escopo. Aqui é onde o serviço recorrente costuma morrer, por expectativa não combinada.
- **Validade e aceite:** até quando a proposta vale e como o cliente aceita.

Rodapé com a marca da agência e o contato em todas as páginas.

## Passo 7: como a proposta é apresentada

**A regra que vale mais que todas as outras: proposta não se envia, se apresenta.**

Mandar o PDF na primeira mensagem parece eficiente e é o jeito mais rápido de perder a venda. O cliente abre no meio do dia, pula direto para o preço, não entende o diagnóstico e responde "vou analisar". Depois disso não existe mais motivo para marcar reunião, porque ele acha que já viu tudo.

Por isso a primeira mensagem **nunca leva o PDF anexo**. Ela leva os números que despertam curiosidade e pede o encontro. O documento só aparece depois que alguém explicou.

São três caminhos, em ordem de preferência. Gere sempre os três, porque o consultor decide conforme a reação do cliente.

**Caminho 1, presencial.** O melhor de todos, e o único em que a proposta é lida junto. Entregue o roteiro de apresentação em tópicos: a ordem das páginas, a frase de abertura, onde fazer pausa, em que momento virar para o investimento e a pergunta de fechamento. Uma linha por item, é cola de bolso, não texto corrido.

**Caminho 2, reunião online.** Para quem está longe ou não recebe visita. A mensagem pede de quinze a vinte minutos de chamada, oferece dois horários concretos (escolher entre dois é mais fácil que sugerir um) e não anexa nada. Na reunião o consultor compartilha a tela e percorre o PDF na mesma ordem do roteiro presencial. O arquivo é enviado ao final da chamada.

**Caminho 3, vídeo de tela.** É o plano B de quem recusou a reunião, nunca a primeira opção. O consultor grava de três a cinco minutos percorrendo o PDF na tela, com a própria voz, e manda o vídeo **junto** com o arquivo. Assim o cliente continua recebendo a explicação, só que gravada. Entregue também o roteiro do vídeo, com o que dizer em cada página e quanto tempo gastar em cada uma. Vídeo sem roteiro vira dez minutos de divagação e ninguém assiste até o fim.

### Como escrever as mensagens

Toda mensagem de WhatsApp segue estas regras de forma, porque texto em bloco não é lido no celular:

- **Uma linha em branco entre cada parágrafo.** Nunca um bloco corrido.
- Cada parágrafo com **uma ideia só**, no máximo duas linhas.
- **Negrito com asterisco simples** (`*assim*`) nos números e no que precisa saltar aos olhos. No máximo três destaques por mensagem, senão nada se destaca.
- **Entregue cada mensagem dentro de um bloco de código**, para o consultor copiar e colar direto no WhatsApp com os asteriscos preservados. Se a mensagem sair como texto normal na conversa, os asteriscos viram formatação da própria tela e o consultor cola no WhatsApp sem negrito nenhum.
- Sem emoji, ou no máximo um. Sem "espero que esteja bem", sem "conforme solicitado".
- Trate o cliente do jeito que o consultor informou na pergunta 10.

E estas regras de conteúdo:

- Primeiro **quantas pessoas procuram** (quando o volume foi consultado), depois o fato de que ele **não aparece na frente delas**. Uma linha para cada. Invertido, o segundo número não dói.
- No máximo dois números por mensagem. O terceiro vira ruído.
- Termine sempre com **pergunta fechada**, de responder em uma palavra ou escolhendo entre duas opções. Pergunta aberta morre sem resposta.
- Não cite preço na primeira mensagem, em nenhuma hipótese. Preço fora de contexto vira objeção antes de existir conversa.

### As três mensagens que a skill entrega

1. **Mensagem 1, o convite.** Sem anexo. Os números do diagnóstico e o pedido de reunião com dois horários.
2. **Mensagem 2, o envio depois da apresentação.** Curta, acompanha o PDF, retoma o combinado e pergunta o próximo passo.
3. **Mensagem 3, o plano B.** Para quem recusou a reunião: acompanha o vídeo e o PDF, avisa a duração do vídeo e termina com pergunta fechada.

Junto delas, o roteiro presencial e o roteiro do vídeo de tela.

## Passo 8: gerar o arquivo

Monte o documento em HTML e CSS e renderize em PDF A4 com Chromium via Playwright, no mesmo motor da skill de materiais.

- A logo entra embutida em base64 no CSS, a partir do arquivo que o consultor anexou.
- **Nunca distorça a logo.** Defina apenas uma dimensão (a altura) e deixe a outra automática, para a proporção original ser mantida. Logo esticada ou achatada é o erro mais visível de um material comercial, e desmonta a credibilidade do documento inteiro. Antes de entregar, confira na imagem renderizada se a marca está com a mesma proporção do arquivo original. O layout precisa aceitar tanto logo horizontal quanto quadrada sem quebrar.
- A cor principal da agência vira variável CSS e é usada na capa, nos títulos e nos destaques. Escolha automaticamente texto claro ou escuro conforme o contraste da cor informada.
- Os prints do GBPCheck entram como imagem, com largura total e canto arredondado, sem borda pesada.
- Antes de entregar, converta em imagem e confira página por página. Se algum texto vazou, encurte e renderize de novo.
- **Nunca anuncie um arquivo que não foi criado nesta mesma resposta.**

Entregue o PDF, e logo abaixo, no chat, a mensagem de WhatsApp e o roteiro presencial.

## Pausas obrigatórias

A skill propõe, o consultor aprova. Pare e mostre antes de gerar o PDF:

1. **A leitura do diagnóstico.** Mostre as frases da página 2 e pergunte se está fiel ao que ele viu na ferramenta. Se o consultor discordar de um número, prevalece o consultor, e você registra o ajuste sem discutir.
2. **O escopo das duas opções.** Antes de escrever o preço no papel, confirme o que entra e o que não entra.

Se algum dado enviado contradiz outro (por exemplo, o consultor diz que o perfil está bem posicionado mas a tabela mostra o contrário), **pare e aponte a contradição antes de escrever**. Proposta com número que não fecha destrói a credibilidade na primeira leitura do cliente.

## Bloco de reuso da marca

Ao final de toda entrega, devolva isto para o consultor guardar:

```
MINHA MARCA (cole isto no início da próxima proposta)
Agência: [nome]
Cor principal: [hex]
Contato: [telefone/WhatsApp] · [e-mail] · [site]
Assinatura: [nome de quem assina]
Logo: anexar o arquivo
```

## Regras de estilo

- Português do Brasil, tom de professor: claro, direto e sem juridiquês nem jargão de marketing.
- **Nunca use travessão (—).** Use vírgula, dois-pontos, parênteses ou ponto.
- Frases curtas. O leitor é um dono de negócio ocupado, lendo no celular ou em pé no balcão.
- Sem hype, sem superlativo, sem "solução completa e inovadora".
- Só afirme o que o material enviado sustenta. Na dúvida, corte a frase.

## Lembrete final

Uma proposta boa não convence pelo desenho, convence porque o cliente se reconhece no diagnóstico. Se os dados do GBPCheck não vieram, ou se o preço não foi calculado, volte e peça antes de gerar. Proposta bonita com número inventado fecha menos que proposta simples com número verdadeiro.
