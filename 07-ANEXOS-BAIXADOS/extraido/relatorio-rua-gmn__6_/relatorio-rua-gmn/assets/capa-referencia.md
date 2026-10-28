# Capa: layout de referência

Ponto de partida do CSS da capa descrita no Passo 6. Substitua `COR_MARCA` pela cor
principal da agência e `NAVY` pelo tom escuro do texto. As medidas assumem A4 com
15 mm de margem lateral.

Os dados abaixo são inventados, para servir de esqueleto. **Nunca guarde aqui o
material de um prospect real**, porque esta pasta é distribuída para outros consultores.

```css
.topo-capa   { display: flex; justify-content: space-between; align-items: center; }
.logo        { height: 12mm; width: auto; align-self: flex-start; flex: none; }
.selo        { font-size: 9.5pt; letter-spacing: .16em; text-transform: uppercase;
               color: COR_MARCA; font-weight: bold; }

.kicker      { font-size: 9.5pt; letter-spacing: .16em; text-transform: uppercase;
               color: COR_MARCA; font-weight: bold; }
.nome-negocio{ font-size: 24pt; font-weight: bold; color: NAVY;
               line-height: 1.1; margin: 1.5mm 0; }

/* a montagem entra aqui, largura 93% da caixa de texto, centralizada */

.destaque        { border-left: 4pt solid COR_MARCA; padding-left: 6mm; margin-top: 5mm; }
.destaque-titulo { font-size: 18pt; font-weight: bold; color: NAVY; line-height: 1.25; }
.destaque-frase  { font-size: 12pt; line-height: 1.55; margin-top: 3.5mm; }

.caixa-numero    { border: 1.6pt solid NAVY; border-radius: 3mm; padding: 4.5mm;
                   margin-top: 5mm; display: flex; gap: 6mm; align-items: center; }
.numero-gigante  { font-size: 34pt; font-weight: bold; color: NAVY;
                   background: #ffe86b; padding: 1mm 4mm; border-radius: 1.5mm;
                   line-height: 1.15; flex: none; }
.numero-texto    { font-size: 12pt; line-height: 1.5; }

.transicao   { font-size: 11.5pt; font-weight: bold; color: COR_MARCA;
               margin-top: 5mm; margin-bottom: 4mm; }

.grifo       { background: #ffe86b; padding: 1px 3px; }
```

Esqueleto do HTML, na ordem em que os blocos devem aparecer:

```html
<div class="topo-capa">
  <img class="logo" src="...">
  <div class="selo">Diagnóstico gratuito</div>
</div>

<div class="kicker">Preparado para</div>
<div class="nome-negocio">Nome do Negócio</div>
<div class="peq">Rua Exemplo, 100, Centro, Cidade, UF</div>

<img class="montagem" src="...">
<div class="peq">
  Busca por "termo pesquisado" feita em N pontos espalhados pela cidade, em DD/MM/AAAA.
  Cada círculo é uma pesquisa e o número é a posição em que o seu negócio apareceu
  naquele ponto. Ao lado, o seu perfil como o Google mostra hoje.
</div>

<div class="destaque">
  <div class="destaque-titulo">
    Quem aparece quando alguém procura<br><span class="grifo">termo pesquisado</span>?
  </div>
  <p class="destaque-frase">
    <span class="grifo"><b>Em nenhum dos N pontos da cidade o seu negócio aparece
    entre os três primeiros.</b></span>
    E não é por falta de avaliação: você tem mais avaliações que quem está em primeiro lugar.
  </p>
</div>

<div class="caixa-numero">
  <div class="numero-gigante">000</div>
  <p class="numero-texto">
    <span class="grifo"><b>pessoas procuram por [serviço] em [cidade] todos os meses</b></span>,
    e hoje o seu negócio não aparece entre as primeiras opções que elas veem.
  </p>
</div>

<div class="transicao">
  Veja nas próximas páginas o que os seus concorrentes mostram no mesmo mapa.
</div>
```

A segunda frase do bloco de destaque muda conforme o contraste que o material sustenta
(mais avaliações que o primeiro colocado, nota maior que quem está na frente, anos de
cidade, aparece só na porta). Escolha uma e escreva só o que os anexos comprovam.
