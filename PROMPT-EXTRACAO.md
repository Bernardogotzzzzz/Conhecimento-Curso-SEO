# Prompt para a extensão Claude in Chrome — Extração Escola de SEO

Cole o bloco abaixo no chat da extensão, com a aba do curso aberta e você já logado na Hotmart.

---

Abra https://hotmart.com/pt-br/club/escoladeseo/products/8137903 (sou aluno, já estou logado).

Sua missão: extrair o conhecimento deste curso em notas estruturadas, módulo por módulo, aula por aula. O objetivo é que eu use esse conhecimento para montar um serviço de posicionamento no Google. Sintetize tudo com suas próprias palavras — quero conhecimento acionável, não transcrição literal.

## FASE 1 — Mapeamento (faça primeiro, antes de abrir qualquer aula)

1. Navegue pela área de membros e liste TODOS os módulos e aulas, na ordem.
2. Me devolva um bloco markdown chamado `INDICE.md` com: número do módulo, nome do módulo, lista de aulas (número, título, duração se visível).
3. Pare e aguarde meu OK antes de começar a Fase 2.

## FASE 2 — Extração aula a aula

Para CADA aula, nesta ordem:

1. Abra a aula.
2. Procure texto disponível: aba/botão de transcrição do player, legendas (CC), descrição da aula, materiais complementares, PDFs anexos, links.
3. Se houver transcrição ou legenda: ative, leia o conteúdo e sintetize.
4. Se a aula for só vídeo sem nenhum texto: dê play, deixe as legendas automáticas ativadas se o player oferecer; se nada textual existir, registre a aula como PENDENTE (vou assistir manualmente) e siga para a próxima. Não invente conteúdo.
5. Me devolva UM bloco markdown por aula, no formato abaixo, para eu salvar no arquivo correspondente.

## Formato de saída por aula

```markdown
# [M01-A03] Título da aula

**Módulo:** 01 — Nome do módulo
**Fonte do conteúdo:** transcrição / descrição / material anexo / PENDENTE
**Duração:** XX min

## Ideia central
(1-3 frases: o que esta aula ensina e por quê importa)

## Conceitos-chave
- Conceito: explicação curta

## Passo a passo prático
1. (ações concretas ensinadas na aula, em ordem)

## Ferramentas citadas
- Ferramenta — para que serve no processo

## Erros/avisos que o instrutor destaca
- ...

## Aplicação para vender posicionamento no Google
(como isso vira entregável, processo ou argumento de venda para cliente)

## Materiais anexos
- nome do arquivo/link (se houver)
```

## Regras

- Síntese com suas palavras, nunca transcrição palavra por palavra.
- Não pule a seção "Aplicação para vender" — é a mais importante para mim.
- A cada 5 aulas, pare e me entregue o lote; aguarde meu "continua".
- Mantenha uma lista corrente `PENDENTES.md` com as aulas sem texto extraível.
- Se a Hotmart pedir login ou aparecer captcha, pare e me avise — eu resolvo.

---

## Onde salvar cada bloco (no seu PC)

- `INDICE.md` → `00-INDICE\INDICE.md`
- Cada aula → `01-MODULOS\<NN-nome-do-modulo>\<MXX-AYY-titulo>.md`
- Pendentes → `00-INDICE\PENDENTES.md`
