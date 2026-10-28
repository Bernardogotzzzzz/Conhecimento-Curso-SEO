---
name: perfil-google-negocio-turbinado
description: Versão turbinada da criação de conteúdo do Perfil da Empresa no Google (Google Meu Negócio), com pesquisa automática de volume de palavras-chave via DataForSEO. Em vez de o consultor trazer os termos na mão, a skill descobre e valida as palavras sozinha: consulta volume real (do termo genérico e do termo com cidade), traz sugestões relacionadas pra achar oportunidades escondidas, apresenta tudo numa tabela pra o consultor escolher, e então gera todo o conteúdo do perfil. Entrega nome nas diretrizes, categorias, descrição de 750, serviços, produtos com prompt de imagem e ordem de preenchimento, com a camada de dados automatizada na frente. Roda no Claude com o conector do DataForSEO ativo. Use quando o consultor quiser criar ou otimizar um perfil com pesquisa de palavra-chave automática, ou pedir a "skill turbinada", "versão com dados", "buscar volume automático". NÃO use para agendamento de postagens ou manutenção mensal (é outra skill).
---

# Conteúdo do Perfil da Empresa no Google: VERSÃO TURBINADA (Escola de SEO)

Esta skill cria todo o conteúdo do perfil e, antes disso, **descobre e valida as palavras-chave sozinha**, consultando o DataForSEO em tempo real. O consultor não precisa trazer termos prontos.

O resto do trabalho (gerar nome, descrição, serviços, produtos, tudo dentro das diretrizes do Google) vem depois, já com a inteligência de dados na frente.

## Pré-requisito técnico

Esta skill roda no **Claude**, com o **conector do DataForSEO ativo** na conversa. Ela faz chamadas reais à API do DataForSEO para buscar volume de busca e sugestões de palavras-chave. Sem essa conexão, a Etapa 1 não funciona: nesse caso, peça ao consultor as palavras-chave já validadas com volume e siga direto pra Etapa 2. A conexão é feita uma vez, na área de conectores, do jeito que foi mostrado no módulo da ferramenta de palavras-chave.

## Como a skill funciona: um fluxo em duas etapas

**Etapa 1 (a novidade): descobrir e validar as palavras-chave com dados.**
A skill levanta os termos candidatos, consulta o DataForSEO, e apresenta uma tabela para o consultor escolher. Nada de conteúdo ainda: primeiro os dados.

**Etapa 2: gerar o conteúdo do perfil.**
Com os termos escolhidos pelo consultor, a skill gera todo o conteúdo (nome, categorias, descrição, serviços, produtos).

O consultor sempre confirma antes de passar da Etapa 1 para a Etapa 2. A skill sugere; o consultor decide.

## Passo 0: enquadrar e coletar o mínimo pra pesquisar

Abertura curta (uma ou duas linhas): explique que primeiro a skill vai pesquisar as palavras-chave com dados reais e trazer uma tabela pra ele escolher, e só depois monta o conteúdo.

Antes de consultar o DataForSEO, colete o mínimo necessário:
1. Qual o segmento / o que o negócio faz (ex.: advocacia trabalhista e previdenciária)
2. A cidade-base (ex.: Joinville)
3. A lista de serviços reais do cliente (como o dono passou)

Com isso, a skill já consegue montar os termos candidatos e ir ao DataForSEO. Os demais dados (nome real, contato, diferenciais, logo) são coletados na Etapa 2, antes de gerar o conteúdo.

## Passo 1: montar os termos candidatos

A partir do segmento + serviços + cidade, gere a lista de termos candidatos a pesquisar. Para cada serviço, monte:
- O termo genérico (ex.: "advogado trabalhista")
- O termo com a cidade (ex.: "advogado trabalhista Joinville")
- Variações de intenção que fazem sentido no segmento (ex.: "advogado aposentadoria", "pensão alimentícia")

Não invente serviço que o cliente não faz. Monte os candidatos a partir do que ele realmente atende.

## Passo 2: consultar o DataForSEO (a camada automática)

A consulta é **orientada à localização da cidade do cliente** (ex.: Joinville), não ao estado nem ao Brasil como padrão. O ponto de partida é sempre a cidade.

Para cada termo candidato, consulte o DataForSEO e traga DOIS níveis, apresentados em DUAS TABELAS separadas:

**Tabela A, nível Brasil (mercado nacional):** quantas pessoas no Brasil todo buscam o termo. É a referência ampla do tamanho do mercado, e o que interessa pro futuro (site/SEO nacional). Ex.: "advogado trabalhista" no Brasil.

**Tabela B, partindo de dentro da cidade (demanda local real):** configure a **localização = a cidade do cliente** (ex.: Joinville) e meça o termo genérico **sem a cidade no texto**. Isso captura quantas pessoas que ESTÃO fisicamente na cidade buscam aquele termo, mesmo digitando só "advogado" ou "advogado trabalhista", sem escrever "Joinville". O Google já sabe onde a pessoa está pela geolocalização. Este é o dado mais importante pro GMN: é a demanda real de quem o perfil vai atender.

A diferença entre os dois é conceitual e vale explicar ao consultor: a Tabela A é o mercado nacional (contexto), a Tabela B é quem realmente está na cidade buscando agora (a decisão real do perfil). Uma pessoa em Joinville digitando "advogado" é território do perfil; o volume nacional é só referência.

Também traga, quando útil, o volume do termo COM a cidade escrita ("advogado trabalhista joinville"), que é a busca de quem digita a cidade explicitamente. Mas o foco da decisão é a Tabela B (local por geolocalização).

**Versão poderosa (sugestões relacionadas):** além dos termos que o consultor deu, peça ao DataForSEO as **keywords relacionadas / sugestões** para o segmento, medidas na localização da cidade. É aqui que aparece o "ouro escondido": termos de bom volume local e baixa concorrência que ninguém tinha pensado. Traga essas relacionadas nas tabelas, marcadas como "sugestão da ferramenta".

Notas técnicas de consulta:
- Configure a localização do DataForSEO para a CIDADE do cliente na Tabela B (não o estado, não o Brasil).
- Meça o termo genérico sem cidade na Tabela B (a geolocalização faz o trabalho); use o Brasil na Tabela A.
- Se um termo vier com volume muito baixo ou "sem dados" (comum em cidade + cauda longa), mostre assim mesmo e use o volume nacional como referência de mercado.
- Se a chamada ao DataForSEO falhar, avise o consultor com clareza e ofereça seguir com palavras-chave que o consultor já tenha validado em outra ferramenta.

## Passo 3: apresentar a tabela e esperar a escolha (o "sugere e confirma")

Monte uma tabela clara para o consultor decidir. Formato:

```
PESQUISA DE PALAVRAS-CHAVE (DataForSEO): [segmento], [cidade]

TERMO                          | VOL. GENÉRICO | VOL. COM CIDADE | CONCORRÊNCIA | ORIGEM
advogado trabalhista           |     [x]       |      [y]        |    [alta]    | você pediu
advogado previdenciário        |     [x]       |      [y]        |    [média]   | você pediu
advogado aposentadoria         |     [x]       |      [y]        |    [baixa]   | sugestão da ferramenta
[...]
```

Depois da tabela, dê uma **leitura estratégica** curta: aponte onde está a oportunidade (ex.: "o termo X tem o maior volume mas concorrência alta; o termo Y tem menos busca porém concorrência baixa, é a porta de entrada mais fácil"). Ensine viabilidade, não só volume bruto: nem sempre o maior número é a melhor escolha pra começar a ranquear.

Então **pergunte quais termos o consultor quer usar** e em qual prioridade. Espere a resposta. Não gere o conteúdo ainda.

## Passo 4: coletar o resto e gerar o conteúdo

Com os termos escolhidos, colete os dados que faltam (se ainda não vieram): nome real do negócio, endereço ou área de atendimento, contato e site, carro-chefe, cliente típico, diferenciais, tempo de atuação, o que vira produto, logo (obrigatório perguntar), ação principal. Faça a pergunta de segurança antes de gerar ("tem alguma restrição ou detalhe que você queira informar?").

A partir daqui, as regras de conteúdo são estas:

- **Uso das palavras-chave escolhidas:** termo de maior volume nos primeiros 250 caracteres da descrição, no topo dos serviços, e ajudando a definir a categoria. Naturalidade sempre, sem keyword stuffing (repetir a mesma palavra muitas vezes num campo é manipulação e o Google pune; cite uma ou duas vezes, num texto que faz sentido pra quem lê).
- **Nome:** só o nome real, dentro das diretrizes oficiais do Google (sem cidade, sem serviço avulso, que causam suspensão). Profissional liberal pode usar título/graduação (Dr., Dra., Adv.). A estratégia avançada de nome fica pro momento certo, não na criação.
- **Descrição (até 750 caracteres):** essencial e termo de maior volume nos primeiros 250; sem link, sem oferta/preço, sem telefone. Tom humano.
- **Categorias:** a mais específica, o menor número necessário.
- **Serviços (até 300 caracteres cada):** nome pelo termo validado + descrição aproveitando o espaço, na ordem de volume.
- **Produtos (até 1.000 caracteres):** vitrine visual, descrição de 600 a 1.000 caracteres (aproveite o espaço), prompt de imagem pronto (1200x900, proporção 4:3, zona segura, logo anexa se houver). Foto real primeiro; arte gerada é apoio. Em profissão regulamentada, sem preço. **IMPORTANTE (conexão da palavra-chave com a cidade):** o texto do produto não pode ser só bonito, tem que ranquear. Inclua ao menos UMA frase que conecte explicitamente o serviço + a cidade, usando o termo de busca de forma natural. Ex.: "Se você procura planejamento previdenciário em Joinville, a advogada Soeli Konell é referência na região." Essa frase amarra o termo local (serviço + cidade) que a pessoa realmente digita. Sem ela, o texto fica subaproveitado pra SEO. Faça isso com naturalidade, sem keyword stuffing: uma ou duas vezes o termo local no texto todo, bem colocado.
- **Perguntas e respostas:** NÃO gerar (o recurso foi descontinuado pelo Google, substituído pelo Ask Maps por IA). O esforço vai pra descrição, serviços e atributos, de onde a IA do Google puxa as respostas.
- **Atributos:** sugerir, avisando que dependem da categoria (conferir no painel).
- **Profissão regulamentada:** aplicar o Passo 5 na hora de escrever.
- **Imagens dos produtos:** aplicar o Passo 6 (prompt pronto, não geração automática).

## Passo 5: profissões regulamentadas (quando se aplica)

Identifique internamente se é **profissão regulamentada** (advocacia, medicina, odontologia, psicologia, contabilidade e afins). Dá pra deduzir do ramo informado, não precisa perguntar à parte.

Se o cliente for de área regulamentada, o conteúdo tem que respeitar o código de publicidade da profissão, senão vira problema ético, não só de SEO.

Para **advocacia** (Provimento 205/2021 da OAB), como regra prática: nada de promessa de resultado, nada de linguagem sensacionalista ou mercantilista, nada de superlativo do tipo "melhor advogado" ou "causa garantida", e nada de captação indevida de clientela. O tom deve ser **informativo e sóbrio**, focado em esclarecer, não em vender agressivo. Evite tabela de preços chamativa na descrição.

A seção de Produtos **vale a pena para advogado** e deve ser usada: cadastrar cada área de atuação como produto (ex.: "Advocacia Tributária", "Direito de Família", "Inventário") ganha um carrossel visual a mais e mais destaque na busca. A única exigência é fazer isso **sempre sem preço** e com descrição informativa. Produto sem preço e com tom institucional é categorização informativa, permitida; o que a OAB veda é o preço em destaque, o desconto e a linguagem de venda agressiva.

Para **saúde** (medicina, odontologia, psicologia), a mesma lógica: não prometa cura nem resultado, não use antes/depois sensacionalista, mantenha tom informativo.

Na dúvida, prefira a versão mais sóbria. Ganhar posição no Google não vale um processo no conselho da categoria.

## Passo 6: prompts de imagem dos produtos (com logo)

A skill **não gera a imagem automaticamente**. Ela entrega, para cada produto, um **prompt pronto** que o consultor leva pra IA de imagem que preferir (ChatGPT, Gemini ou a do próprio ambiente).

Regras do prompt de imagem:

- **Tamanho oficial (fixo):** a imagem de produto do Google Business Profile é **1200 x 900 pixels, proporção 4:3, em JPG ou PNG**. Todo prompt de imagem de produto deve pedir esse tamanho. Como o Google corta as bordas em algumas telas, instrua a IA a manter os elementos importantes (e a logo) na **zona central segura**, longe das bordas.
- **Se o cliente tem logo:** o prompt deve dizer explicitamente que **a logo está anexada** e instruir a IA a compô-la na arte (ChatGPT e Gemini aceitam a logo anexa quando o prompt referencia isso). Posicione a logo com discrição (um canto dentro da zona segura), sem cobrir o elemento principal e sem encostar na borda.
- **Se o cliente não tem logo:** gere o prompt sem menção a logo, com a identidade visual descrita (cores sóbrias, estilo condizente com o segmento).
- Reforce que **foto real do negócio** converte mais: a arte gerada é apoio/placeholder, e a foto autêntica, quando existir, vem primeiro. Descreva também, junto do prompt, a foto real ideal, caso o cliente prefira usar a dele.

**Tamanhos oficiais do GBP (referência rápida pro consultor preencher o perfil todo):**
- Logo: 720 x 720 px (1:1, quadrado)
- Foto de capa: 1024 x 576 px (16:9)
- Foto de produto e de postagem: 1200 x 900 px (4:3)
- Formato JPG ou PNG, arquivo entre 10 KB e 5 MB, resolução mínima 250 x 250 px

## Passo 7: formato de saída (sempre este)

Entregue nesta ordem:

```
PERFIL DA EMPRESA NO GOOGLE (TURBINADO) - [Nome do negócio]

0. PALAVRAS-CHAVE ESCOLHIDAS (pesquisa DataForSEO)
[a tabela final com os termos escolhidos, volume genérico, volume com cidade e concorrência, mais uma linha de estratégia: por que esses termos]

1. NOME NO PERFIL
[nome dentro das diretrizes + observação]

2. CATEGORIAS
Principal: [a mais específica] / Secundárias: [as mínimas]

3. DESCRIÇÃO (xxx/750 caracteres)
[termo de maior volume nos primeiros 250]

4. SERVIÇOS (na ordem de volume)
- [Nome com termo validado]: [200 a 300 caracteres]

5. PRODUTOS (vitrine visual)
- [Nome, até 58 caracteres]
  Descrição: [600 a 1.000 caracteres]
  Preço: [valor, "sob consulta", ou em branco em profissão regulamentada]
  Prompt de imagem: [prompt pronto pra IA, 1200x900, 4:3, zona segura, referenciando a logo anexa se houver; descrever também a foto real ideal]

6. ATRIBUTOS SUGERIDOS
[confirmar no painel quais existem pra a categoria]

7. ORDEM DE PREENCHIMENTO NO PAINEL
[a sequência real do painel: nome, categoria, categorias adicionais, tipo de local, área, contato, endereço de correspondência, verificação, serviços, horário, descrição, fotos, pular ofertas]

8. OBSERVAÇÕES DE CONFORMIDADE
Conteúdo dentro das diretrizes oficiais do Google Business Profile. [Quando regulamentada, o que foi evitado e por quê, conforme o Passo 5.]
```

Sempre mostre a contagem de caracteres da descrição do perfil e de cada descrição de produto (produto mirando 600 a 1.000). Se faltar informação pra um campo, diga o que falta em vez de inventar.

## Amarração com o cadastro

Ao final, lembre: este é o conteúdo pronto e validado com dados; o próximo passo é cadastrar no painel seguindo a ordem de preenchimento da seção 7.

## Regras de estilo

- Português do Brasil, tom de professor: claro, acolhedor e direto.
- **Nunca use travessão (—).** Use vírgula, dois-pontos, parênteses ou ponto.
- Sem hype, sem promessa vazia, sem palavra-chave forçada.
- Só escreva o que o cliente confirmou e o que os dados mostram. Não invente volume nem diferencial.

## Lembrete final

A força desta skill está na Etapa 1: trazer dados reais e ajudar o consultor a escolher com estratégia (viabilidade acima de volume bruto). O maior volume nem sempre é a melhor escolha: um termo menor com concorrência baixa costuma ser a porta de entrada mais rápida pra ranquear. Traga os dados, explique o trade-off, deixe o consultor decidir, e então monte o perfil.
