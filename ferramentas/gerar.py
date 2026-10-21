"""Gera a galeria (a partir de fotos.json) e as perguntas frequentes da oficina.
Uso: python3 ferramentas/gerar.py   (na raiz do repositório). Pode rodar várias vezes."""
import json, re, html, pathlib
from PIL import Image
R = pathlib.Path(__file__).resolve().parent.parent
fotos = json.loads((R / "ferramentas/fotos.json").read_text(encoding="utf-8"))

def bloco(texto, nome, conteudo):
    ini, fim = f"<!--{nome}:inicio-->", f"<!--{nome}:fim-->"
    if f"<!--{nome}-->" in texto:
        texto = texto.replace(f"<!--{nome}-->", ini + fim)
    return re.sub(re.escape(ini) + ".*?" + re.escape(fim), lambda m: ini + "\n" + conteudo + "\n" + fim, texto, flags=re.S)

for site, d in fotos.items():
    pag = R / site / "index.html"
    s = pag.read_text(encoding="utf-8")
    itens = []
    for i, alt in enumerate(d["galeria"], 1):
        nome = f"img/galeria-{i:02d}"
        w, h = Image.open(R / site / f"{nome}.jpg").size
        itens.append(
            f'          <li><picture><source srcset="{nome}.webp" type="image/webp">'
            f'<img src="{nome}.jpg" alt="{html.escape(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async"></picture></li>')
    s = bloco(s, "GALERIA", "\n".join(itens))
    # texto alternativo da foto de destaque
    s = re.sub(r'(<img src="img/destaque\.jpg" alt=")[^"]*(")', lambda m: m.group(1) + html.escape(d["destaque"]) + m.group(2), s)
    pag.write_text(s, encoding="utf-8")

faq = [
  ("Quanto custa um orçamento?", "O orçamento é gratuito. Você traz o carro, fazemos a avaliação e enviamos o valor por escrito pelo WhatsApp, sem compromisso."),
  ("Em quanto tempo o carro fica pronto?", "Serviços simples, como troca de óleo e alinhamento, ficam prontos no mesmo dia. Reparos maiores dependem das peças; o prazo vem junto com o orçamento."),
  ("Vocês dão garantia?", "Sim. Todo serviço tem garantia de 90 dias em peças e mão de obra, registrada na nota."),
  ("Quais formas de pagamento vocês aceitam?", "Pix, dinheiro e cartão de débito ou crédito, pagos na oficina na hora da retirada. Parcelamos no cartão serviços acima de R$ 500."),
  ("Posso levar as peças que foram trocadas?", "Pode e deve. Devolvemos todas as peças substituídas para você conferir o que foi feito."),
  ("Precisa agendar?", "Para revisão e serviços maiores, sim: chame no WhatsApp e marcamos o melhor horário. Para avaliação rápida, pode vir sem agendar."),
]
pag = R / "oficina/index.html"
s = pag.read_text(encoding="utf-8")
s = bloco(s, "FAQ-HTML", "\n".join(
    f"        <details>\n          <summary>{html.escape(q)}</summary>\n          <p>{html.escape(a)}</p>\n        </details>" for q, a in faq))
s = bloco(s, "FAQ-JSON", ",\n".join(
    "      " + json.dumps({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}, ensure_ascii=False) for q, a in faq))
pag.write_text(s, encoding="utf-8")
print("ok")
