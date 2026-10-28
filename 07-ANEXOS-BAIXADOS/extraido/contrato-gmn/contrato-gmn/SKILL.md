---
name: contrato-gmn
description: Gera o contrato de prestação de serviços de gestão do Perfil da Empresa no Google (Google Meu Negócio) em documento editável (.docx), a partir dos dados cadastrais das duas partes e das condições que já foram aceitas na proposta comercial. Lê o cartão CNPJ anexado e extrai razão social, número e endereço sem digitação. Cobre prazo indeterminado, prazo determinado sem fidelidade (meses previstos, cancelável a qualquer momento sem multa) e prazo determinado com aviso prévio, reajuste anual pelo IPCA, titularidade do perfil, exclusividade geográfica opcional e assinatura digital ou presencial. Use SEMPRE que o consultor disser que o cliente aceitou a proposta, pedir para "gerar o contrato", "fazer o contrato do cliente", "montar o contrato de Google Meu Negócio", ou anexar o cartão CNPJ falando em fechamento. NÃO use para montar a proposta comercial (skill proposta-comercial-gmn) nem para o relatório mensal (skill relatorio-mensal-cliente-gmn).
---

# Contrato de gestão do Perfil da Empresa no Google (Escola de SEO)

Esta skill gera o contrato depois que a proposta foi aceita. Ela não vende nem convence: só transforma o que já foi combinado em documento assinável.

**A regra que governa tudo: o contrato não pode contradizer a proposta.** Se a proposta disse quatro postagens, o contrato diz quatro. Se a proposta disse sem fidelidade e sem multa, o contrato não pode ter prazo com aviso prévio. Divergência entre os dois documentos trava assinatura e destrói a confiança construída na apresentação. Sempre que o consultor tiver a proposta em mãos, peça que ele anexe, e puxe as condições de lá em vez de perguntar de novo.

**Saída em .docx editável.** O consultor vai subir o arquivo no Clicksign, no gov.br ou em outra plataforma, e às vezes precisa ajustar uma linha antes. Nada de PDF fechado. E **sem logo, sem cor, sem elemento gráfico**: contrato é texto formatado, e enfeite só atrapalha a leitura de um documento jurídico.

**Esta skill não substitui advogado.** Ao entregar, lembre o consultor de que o modelo é um documento de trabalho organizado por quem entende do serviço, e que vale uma leitura profissional antes de usar em escala.

## Passo 1: a proposta aceita

Antes de qualquer pergunta:

1. Anexe a proposta comercial que o cliente aceitou, ou me diga qual opção ele escolheu e as condições combinadas.

Se a proposta vier, extraia dela: modo do serviço, entregas do setup, entregas mensais, quantidade de postagens, dia do relatório, valores, forma de pagamento e prazo. Confirme o que extraiu antes de seguir, em lista curta.

Se não vier, siga pelas perguntas dos passos 3 e 4, avisando que sem a proposta o risco de divergência entre os dois documentos aumenta.

## Passo 2: os dados das partes

**Quando houver CNPJ, peça o cartão CNPJ anexado**, das duas partes quando as duas forem empresa. Extraia razão social, número do CNPJ, endereço completo e situação cadastral. Não peça ao consultor que digite o que está no documento.

Se a situação cadastral não estiver ativa, avise antes de gerar. Contrato assinado por empresa baixada ou inapta é problema na cobrança.

**Quando for pessoa física**, os dados vão manualmente: nome completo, CPF, RG com órgão emissor e endereço completo.

Em qualquer caso, pergunte o nome de quem assina por cada parte, se for diferente do titular.

Mostre os dados extraídos para conferência antes de gerar. Erro de CNPJ no contrato é o tipo de coisa que só aparece na hora de cobrar.

## Passo 3: prazo, reajuste e cancelamento

2. Qual dos três formatos de prazo?

- **Prazo indeterminado**, sem fidelidade, cancela quando quiser.
- **Prazo determinado sem fidelidade**, um número de meses previsto, mas cancelável a qualquer momento e sem multa.
- **Prazo determinado com aviso prévio**, um número de meses com 30 dias de aviso para encerrar antes.

**Prazo indeterminado é o padrão do curso**, porque é o que a proposta promete e é mais fácil de vender. Nesse caso entram: reajuste anual pela variação acumulada do IPCA, encerramento por qualquer das partes mediante comunicação escrita sem multa, e efeito ao final do mês já pago.

A linha do efeito ao final do mês pago não é detalhe: sem ela, alguém cancela no dia 3 e pede devolução proporcional. Com ela, ninguém devolve nada e ninguém cobra o mês seguinte.

**Prazo determinado sem fidelidade** é o formato de quem vendeu "contrato de 12 meses, sem fidelidade e sem multa". Não há contradição aqui, desde que o contrato escreva as duas coisas separadas: o prazo é a duração prevista do trabalho e a base do valor total apresentado, e a denúncia imotivada é o direito de qualquer das partes de encerrar antes, por escrito, sem multa, sem aviso prévio mínimo e sem antecipação das parcelas vincendas, com efeito ao final do mês já pago.

Nesse formato, escreva também que o encerramento antecipado não gera cobrança das mensalidades restantes, que o valor total citado na proposta é a soma do período completo e não dívida antecipada, e que ao final dos meses previstos o contrato se prorroga automaticamente por prazo indeterminado nas mesmas condições, salvo manifestação em contrário. Sem essa última linha, o serviço fica sem contrato no mês 13 e a cobrança perde base.

Nos dois formatos de prazo determinado, o reajuste pelo IPCA acumulado só incide depois de completados doze meses de vigência, ou seja, na prorrogação. Escreva assim, para não parecer que o valor pode mudar dentro do período contratado.

Se for prazo determinado com aviso prévio, pergunte quantos meses e use aviso prévio de 30 dias, com os meses trabalhados e o mês do aviso devidos, sem multa adicional.

**Quando a proposta trouxer prazo e "sem fidelidade" na mesma opção, não trate como erro e não pergunte qual dos dois vale.** É o segundo formato, e o contrato precisa dizer os dois.

3. Data de início da vigência.

## Passo 4: valores e pagamento

4. Valor da implantação inicial e quando ela é paga.
5. Valor da mensalidade e a data do primeiro vencimento.
6. Como o cliente paga? Descreva com detalhe, porque aqui mora a maior fonte de confusão.

**O prazo do contrato e o parcelamento do pagamento são coisas independentes.** É comum um contrato de 6 meses ser pago em 10x no cartão, ou um contrato por prazo indeterminado ter mensalidade no boleto. Pergunte explicitamente: qual meio (Pix, boleto, cartão recorrente, cartão parcelado), quantas parcelas, e se o setup é cobrado separado da mensalidade ou tudo junto.

Quando houver **parcelamento no cartão**, inclua a cláusula que explica que as parcelas são processadas pela operadora de forma independente da vigência, e que em caso de encerramento a contratada cancela as cobranças futuras não correspondentes a serviços prestados, quando tecnicamente possível.

Inadimplência: suspensão dos serviços após 10 dias de atraso, e possibilidade de encerramento imediato pela contratada.

## Passo 5: as cláusulas opcionais

7. Quer incluir **exclusividade geográfica** (você não atende concorrente direto dele na mesma cidade ou região)?

**Exclusividade e divulgação de resultados entram ou saem juntas.** Uma é contrapartida da outra: se o consultor abre mão de atender concorrentes naquela praça, ganha o direito de usar o caso nos seus canais e materiais. Se não há exclusividade, não há autorização de divulgação.

Ao perguntar, avise sobre o custo dela: exclusividade fecha um nicho inteiro na cidade e, para quem está começando, pode bloquear o próprio mercado logo no primeiro contrato. Não desencoraje, só deixe claro o que ele está trocando.

Se ele aceitar, pergunte quais canais entram na cláusula de divulgação (perfis, site, cursos) e qual a região da exclusividade.

8. A assinatura será **digital** (Clicksign, gov.br ou outra) ou **presencial**?

Digital é o padrão: nesse caso o documento não leva linhas de assinatura, e o texto de fecho registra que o registro eletrônico da plataforma é prova suficiente, dispensadas testemunhas e via impressa. Presencial leva as linhas das duas partes e de duas testemunhas, com nome e documento de cada uma.

9. Cidade do foro.

## Passo 6: o que o contrato sempre traz

Estas cláusulas não são negociáveis e entram em todo contrato gerado:

**Titularidade do perfil.** O perfil é e permanece do cliente. A contratada atua como administradora, com acesso concedido apenas para executar o serviço. Encerrado o contrato, os acessos são devolvidos em até 3 dias úteis. É a cláusula que mais tranquiliza quem contrata, e por isso fica em bloco próprio, nunca escondida dentro do sigilo.

**Suspensão pelo Google.** Se o Google suspender, remover ou restringir o perfil por motivo alheio à conduta da contratada, ela atua para reverter junto ao suporte, sem que isso configure descumprimento. A decisão é exclusiva do Google. Esse é um risco real do serviço e a maioria dos modelos genéricos não cobre.

**Ausência de vínculo com o Google.** A contratada declara que não possui vínculo, credenciamento, parceria ou representação junto ao Google, não detém acesso privilegiado e não dispõe de meio para alterar, acelerar ou manipular a ordem dos resultados. O que oferece é conhecimento técnico e boas práticas de otimização orgânica dentro das diretrizes públicas.

Essa cláusula protege juridicamente e ainda separa o consultor de quem vende parceria inexistente com o Google. Nunca a remova.

**Sem garantia de posição.** Nenhuma promessa de colocação, de prazo para alcançá-la ou de volume de contatos integra o contrato. O que se garante é a execução dos serviços na frequência acordada, com relatório mensal para conferência.

**Nunca escreva previsão de resultado por faixa de meses.** Frases do tipo "entre o terceiro e o sexto mês haverá melhora notável" são promessa de resultado assinada, e um cliente insatisfeito no mês 5 usa isso contra o consultor. Se ele quiser falar de expectativa, que fale na apresentação da proposta, não no contrato.

**Aprovação de conteúdo.** As publicações são sugeridas pela contratada e vão ao ar somente após aprovação do cliente.

**Resposta a avaliações em conjunto.** Feita pela contratada, com participação do cliente sempre que a resposta depender de informação que só ele tem, como detalhes de um atendimento específico.

**Grupo de WhatsApp como canal oficial**, com as ações realizadas, as avaliações recebidas e as respostas publicadas informadas ali. Atendimento de segunda a sexta, das 8h às 12h e das 13h às 17h, exceto feriados nacionais, com prazos contados a partir do próximo dia útil quando a demanda chegar fora desse horário.

**Obrigação do cliente de pedir avaliações.** Escrita como obrigação dele, reconhecendo que a ação depende exclusivamente do cliente e influencia diretamente o resultado. É a cláusula que protege o consultor quando o resultado demora.

**Sigilo e LGPD**, em versão enxuta: sigilo sobre informações estratégicas e internas, observância da Lei 13.709/2018, tratamento apenas dos dados necessários, e transferência mais eliminação dos dados ao fim do contrato mediante solicitação.

## Passo 7: gerar o arquivo

Monte o .docx com a estrutura de nove blocos: as partes, o que será feito, titularidade e acesso, obrigações das partes, prazo e reajuste e cancelamento, valores e pagamento, sigilo e dados, sobre o resultado, disposições gerais e foro.

**A abertura do documento.** Título centralizado, uma linha fina abaixo dele, e então um preâmbulo de duas a três linhas antes do bloco das partes. O preâmbulo diz o que as partes estão celebrando, o que o documento define (o que será executado, prazos, valores e responsabilidades de cada lado) e que as condições correspondem à proposta comercial aceita.

O espaço entre a linha fina e o preâmbulo é de no máximo uma linha, cerca de 9 pontos de espaçamento posterior no parágrafo do título. Não insira parágrafo vazio para separar os dois: o vazio soma com o espaçamento do título e abre um buraco de duas linhas logo na abertura, que é a primeira coisa que o cliente vê.

**O preâmbulo descreve, nunca promete.** Nada de "com o objetivo de melhorar o posicionamento" ou "visando aumentar a visibilidade". Frase assim é promessa de resultado assinada na primeira linha, e vale contra o consultor tanto quanto uma cláusula. Diga o serviço, não o efeito esperado dele.

**O cabeçalho não entra na primeira página.** Com o título já centralizado no topo, o cabeçalho repetido logo acima faz o leitor ler a mesma frase duas vezes. Use página inicial diferenciada: cabeçalho da segunda página em diante, rodapé com o número da página em todas.

- Documento em preto sobre branco, fonte serifada ou sem serifa legível, tamanho 11, espaçamento confortável.
- Títulos de cláusula em negrito, numeração hierárquica (1, 1.1, a).
- Cabeçalho com o título do contrato a partir da segunda página, rodapé com número de página em todas.
- Sem logo, sem cor, sem borda, sem tabela decorativa.
- Alvo de duas a três páginas. Se passar disso, enxugue a redação, nunca corte cláusula.

Antes de entregar, confira: os valores batem com a proposta, as quantidades batem com a proposta, o prazo e a regra de cancelamento batem com a proposta, o CNPJ está correto, e não sobrou nenhum campo entre colchetes por preencher.

**Nunca anuncie um arquivo que não foi criado nesta mesma resposta.**

Ao entregar, mande junto uma lista curta do que o consultor precisa conferir antes de enviar para assinatura, e o lembrete da revisão jurídica.

## Regras de estilo

- Português do Brasil. Linguagem clara e direta, sem juridiquês desnecessário. O cliente precisa entender o que assinou.
- **Nunca use travessão (—).** Use vírgula, dois-pontos, parênteses ou ponto.
- Frases curtas. Uma obrigação por item.
- Não invente cláusula que o consultor não pediu, e não remova as do Passo 6.

## Lembrete final

Contrato que contradiz a proposta é pior que contrato nenhum, porque quebra a confiança exatamente no momento em que o cliente ia assinar. Na dúvida entre o que a proposta disse e o que o consultor está falando agora, pare e pergunte qual dos dois vale. Prazo definido somado a "sem fidelidade e sem multa" não é dúvida, é o formato do Passo 3, e vai para o contrato inteiro.
