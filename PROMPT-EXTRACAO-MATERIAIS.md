# Prompt 2 — Mapear materiais, links e descrições (sem legenda)

Cole o bloco abaixo na extensão Claude in Chrome, com a aba do curso aberta e logada.

---

Estou logado no curso "Profissão Google Meu Negócio com IA" (https://hotmart.com/pt-br/club/escoladeseo/products/8137903). O índice já foi mapeado (20 módulos, 105 aulas).

NÃO transcreva legendas e NÃO use screenshots de legenda. Já sei que isso é inviável. Sua missão agora é mapear tudo que existe em TEXTO na plataforma, aula por aula, dos módulos 00 a 17 (pule 16, 18 e 19, que estão vazios).

## O que capturar em cada aula

Abra a aula e leia a página (get_page_text / read_page), principalmente a seção "Informações da aula" e a aba de materiais:

1. Texto completo da descrição da aula, copiado como está.
2. Todos os links que aparecem na descrição ou nos materiais: guarde o texto do link e a URL completa (ex.: SE Ranking, GPT Personalizado, Skills, planilhas, grupos).
3. Todos os materiais anexos: nome do arquivo, tipo (PDF, planilha, imagem, zip), e a URL se estiver visível. NÃO baixe nenhum arquivo.
4. Texto visível na tela do vídeo que dê para ler em UM único screenshot (ex.: slide de título, lista de passos). No máximo 1 screenshot por aula, no meio do vídeo.
5. Nome de cada ferramenta, skill, GPT ou prompt citado no título ou na descrição.

Não invente conteúdo. Se a aula não tem descrição nem material, escreva exatamente "sem texto na plataforma".

## Formato da entrega (um bloco por módulo)

```markdown
# Módulo XX — Nome

## [MXX-AYY] Título da aula (duração)
**Descrição:** (texto copiado, ou "sem texto na plataforma")
**Links:**
- texto do link — URL
**Materiais anexos:**
- nome do arquivo (tipo) — URL se houver
**Ferramentas/skills citadas:** lista
**Texto visto no vídeo:** (ou "não capturado")
```

## Regras

- Entregue um módulo por vez e espere meu "continua" só se houver erro. Se tudo correr bem, siga direto para o próximo módulo.
- Se a Hotmart pedir login ou aparecer captcha, pare e me avise.
- No final, entregue um bloco `MATERIAIS-CONSOLIDADO.md` com duas listas: (a) todos os links únicos, agrupados por ferramenta; (b) todos os materiais anexos do curso inteiro.
- Também liste as aulas em que o título indica algo valioso (skills, prompts, GPTs, modelos de proposta e contrato, scripts de abordagem), para eu priorizar a gravação de áudio depois.

---

## Onde salvar (no seu PC)

- Cada módulo → `01-MODULOS\<pasta-do-modulo>\MATERIAIS.md`
- Consolidado → `00-INDICE\MATERIAIS-CONSOLIDADO.md`
