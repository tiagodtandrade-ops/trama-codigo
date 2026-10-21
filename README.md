# Trama Código — site e portfólio

Site da Trama Código, com três exemplos demonstrativos, um por pacote. HTML e CSS estáticos, sem dependências externas, sem rastreamento e sem JavaScript.

- **Endereço previsto:** https://tiagodtandrade-ops.github.io/trama-codigo/ (o GitHub Pages só é ativado depois da aprovação do QA)
- **Missão:** TC-DEV-001

## Estrutura

```
index.html            Página principal (quem somos, pacotes, como funciona, exemplos, contato)
assets/               CSS, fonte Fraunces e imagens da marca
salao/                Exemplo Essencial — Alecrim & Seda (3 seções, ilustração SVG)
doceria/              Exemplo Vitrine — Três Colheres Confeitaria (5 seções, 12 fotos, cardápio)
  cardapio.html       Cardápio completo (destino do link de cardápio)
oficina/              Exemplo Completo — Garagem Pistão Azul (5 seções + perguntas frequentes)
ferramentas/          gerar.py e fotos.json: montam as galerias e a FAQ (uso interno)
CREDITOS.md           Fontes, ilustrações e fotos, com licença
.nojekyll             Faz o GitHub Pages servir os arquivos como estão
```

## Ver localmente

```bash
# na pasta acima do repositório, para reproduzir o caminho /trama-codigo/ do GitHub Pages
python3 -m http.server 8000
# abrir http://localhost:8000/trama-codigo/
```

Abrir o `index.html` direto no navegador também funciona.

## Limites de cada pacote nos exemplos

| Exemplo | Pacote | Seções | Fotos | Extras |
|---|---|---|---|---|
| salao/ | Essencial | 3 (Início, Serviços e preços, Horário e contato) | 0 (ilustração) | — |
| doceria/ | Vitrine | 5 (Início, Cardápio, Sobre, Galeria, Localização e contato) | 12 (1 destaque + 11 na galeria) | links de cardápio e mapa |
| oficina/ | Completo | 5 (Início, Serviços, Como trabalhamos, Galeria, Contato) | 12 (1 destaque + 11 na galeria) | perguntas frequentes, título e descrição para buscadores, dados estruturados |

A faixa de aviso no topo e o rodapé de demonstração não contam como seção.

## Trocar fotos

1. Salve cada foto como `img/<nome>.jpg` e `img/<nome>.webp` (destaque e galeria-01: 1200×800; galeria-02 a 11: 800×800).
2. Ajuste o texto alternativo em `ferramentas/fotos.json`.
3. Rode `python3 ferramentas/gerar.py` na raiz do repositório. Ele atualiza as galerias, o texto alternativo e as dimensões declaradas.
4. Atualize o `CREDITOS.md`.

## Decisões técnicas

- **Fontes auto-hospedadas** (woff2, um peso por site), sem Google Fonts.
- **Exemplos com `noindex`**, para que negócios fictícios não apareçam em buscadores. Num cliente real, essa linha sai.
- **E-mail da página principal** escrito com entidades HTML, como proteção leve contra robôs de spam.
- **Contatos dos exemplos evidentemente fictícios:** DDD 00 e domínio `.invalid`, reservado e inexistente.
- **Mapas dos exemplos ilustrados em SVG.** O botão "Como chegar" mostra o formato do link real.
- **FAQ com `<details>`:** abre e fecha sem JavaScript e funciona pelo teclado.
