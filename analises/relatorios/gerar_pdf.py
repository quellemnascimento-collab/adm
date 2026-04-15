"""
Gerador de PDF para Instruções de Trabalho — Template Irigarr
Uso: python3 gerar_pdf.py <arquivo.md> <saida.pdf>
"""
import sys
import os
import re
import base64
import markdown
import yaml
from weasyprint import HTML, CSS


# ─── Utilitários ────────────────────────────────────────────────────────────

def parse_frontmatter(content):
    """Extrai frontmatter YAML do início do markdown."""
    if content.startswith('---'):
        end = content.find('\n---', 3)
        if end != -1:
            fm_text = content[3:end]
            body = content[end + 4:].strip()
            try:
                return yaml.safe_load(fm_text) or {}, body
            except yaml.YAMLError:
                pass
    return {}, content


def extract_etapas(content):
    """Extrai títulos das etapas (### Etapa N) para os blocos visuais."""
    return re.findall(r'^### (.+)$', content, re.MULTILINE)


def load_header_image(repo_root):
    """Carrega o cabeçalho como base64, se existir."""
    for ext in ('png', 'jpg', 'jpeg'):
        path = os.path.join(repo_root, 'assets', f'header_IT.{ext}')
        if os.path.exists(path):
            with open(path, 'rb') as f:
                b64 = base64.b64encode(f.read()).decode()
            mime = 'jpeg' if ext in ('jpg', 'jpeg') else 'png'
            return f'data:image/{mime};base64,{b64}'
    return None


# ─── Blocos visuais de etapas (setas douradas) ──────────────────────────────

def build_steps_html(etapas):
    if not etapas:
        return ''
    items = []
    for i, etapa in enumerate(etapas):
        # Remove prefixo "Etapa N — " para exibir só o nome
        label = re.sub(r'^Etapa\s+\d+\s*[—–-]\s*', '', etapa).strip()
        num = i + 1
        first = 'first' if i == 0 else ''
        last  = 'last'  if i == len(etapas) - 1 else ''
        items.append(f'''
        <div class="step {first} {last}">
            <span class="step-num">{num}</span>
            <span class="step-label">{label}</span>
        </div>''')
    return f'<div class="steps-row">{"".join(items)}</div>'


# ─── Cabeçalho HTML (imagem real ou fallback CSS) ───────────────────────────

def build_header_html(img_src):
    if img_src:
        return f'<div class="it-header"><img src="{img_src}" alt="Cabeçalho Irigarr"></div>'
    # Fallback estilizado quando a imagem ainda não foi adicionada
    return '''
    <div class="it-header it-header-fallback">
        <div class="header-left">
            <div class="header-title">INSTRUÇÕES DE TRABALHO - IT</div>
        </div>
        <div class="header-right">GRUPO <strong>Irigarr</strong></div>
    </div>'''


# ─── CSS do template ─────────────────────────────────────────────────────────

CSS_TEMPLATE = """
@page {
    size: A4;
    margin: 0 0 2cm 0;
    @bottom-right {
        content: "Página " counter(page) " de " counter(pages);
        font-size: 8pt;
        color: #999;
        margin-right: 2cm;
    }
}

* { box-sizing: border-box; }

body {
    font-family: Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.6;
    color: #1a1a1a;
    margin: 0;
    padding: 0;
}

/* ── Cabeçalho ── */
.it-header { width: 100%; margin-bottom: 0; }
.it-header img { width: 100%; display: block; }

.it-header-fallback {
    background: #1a1a1a;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 18px 28px;
    color: #F5A623;
}
.header-title {
    font-size: 16pt;
    font-weight: bold;
    letter-spacing: 1px;
}
.header-right {
    font-size: 13pt;
    color: #ffffff;
    text-align: right;
}
.header-right strong { color: #F5A623; }

/* ── Corpo do documento ── */
.doc-body {
    padding: 0 2.2cm;
}

/* ── Texto introdutório ── */
.intro-text {
    font-size: 9.5pt;
    color: #444;
    margin: 16px 0 10px 0;
    font-style: italic;
}

/* ── Título da IT ── */
.it-title {
    font-size: 15pt;
    font-weight: bold;
    text-align: center;
    margin: 14px 0 16px 0;
    color: #1a1a1a;
}

/* ── Metadados ── */
.metadata {
    list-style: disc;
    padding-left: 22px;
    margin: 0 0 20px 0;
    font-size: 10pt;
}
.metadata li { margin-bottom: 4px; }
.metadata li strong { color: #1a1a1a; }

/* ── Divisor ── */
.divider {
    border: none;
    border-top: 1.5px solid #ddd;
    margin: 18px 0;
}

/* ── Título de seção ── */
h2 {
    font-size: 14pt;
    font-weight: bold;
    color: #1a1a1a;
    margin: 22px 0 12px 0;
    border-left: 5px solid #F5A623;
    padding-left: 10px;
}

h3 {
    font-size: 11pt;
    font-weight: bold;
    color: #1a3a5c;
    margin: 18px 0 8px 0;
}

/* ── Setas douradas ── */
.steps-row {
    display: flex;
    align-items: stretch;
    margin: 18px 0 26px 0;
    gap: 0;
}

.step {
    flex: 1;
    background: #F5A623;
    color: #1a1a1a;
    padding: 12px 28px 12px 36px;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    clip-path: polygon(0 0, calc(100% - 16px) 0, 100% 50%, calc(100% - 16px) 100%, 0 100%, 16px 50%);
    margin-right: 4px;
}

.step.first {
    clip-path: polygon(0 0, calc(100% - 16px) 0, 100% 50%, calc(100% - 16px) 100%, 0 100%);
    padding-left: 20px;
    border-radius: 4px 0 0 4px;
}

.step.last {
    clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%, 16px 50%);
    margin-right: 0;
    border-radius: 0 4px 4px 0;
}

.step.first.last {
    clip-path: none;
    border-radius: 4px;
}

.step-num {
    display: block;
    background: #1a1a1a;
    color: #F5A623;
    font-weight: bold;
    font-size: 13pt;
    width: 28px;
    height: 28px;
    line-height: 28px;
    border-radius: 50%;
    text-align: center;
    margin-bottom: 5px;
    flex-shrink: 0;
}

.step-label {
    font-size: 8pt;
    font-weight: bold;
    line-height: 1.3;
}

/* ── Tabelas ── */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0 16px 0;
    font-size: 9.5pt;
    page-break-inside: avoid;
}

thead tr { background: #1a3a5c; color: #fff; }
thead th { padding: 8px 10px; text-align: left; font-weight: bold; }
tbody tr:nth-child(even) { background: #f5f7fa; }
tbody tr:nth-child(odd)  { background: #ffffff; }
tbody td { padding: 7px 10px; border-bottom: 1px solid #dde3ea; vertical-align: top; }

/* ── Listas ── */
ul, ol { padding-left: 20px; margin: 6px 0 12px 0; }
li { margin-bottom: 3px; }

/* ── Code inline ── */
code {
    background: #f0f4f8;
    padding: 1px 4px;
    border-radius: 3px;
    font-family: 'Courier New', monospace;
    font-size: 8.5pt;
    color: #c0392b;
}

/* ── Rodapé da IT ── */
.it-footer {
    margin-top: 30px;
    padding-top: 10px;
    border-top: 1.5px solid #ddd;
    font-size: 8pt;
    color: #888;
    display: flex;
    justify-content: space-between;
}
"""


# ─── Montagem do HTML final ──────────────────────────────────────────────────

def build_html(fm, body_html, etapas, header_img):
    titulo         = fm.get('titulo', '')
    nome_exibicao  = fm.get('nome_exibicao', titulo)
    objetivo       = fm.get('objetivo', '')
    responsavel    = fm.get('responsavel', '')
    sistema        = fm.get('sistema', '')
    revisao        = fm.get('revisao', '')

    header_block = build_header_html(header_img)
    steps_block  = build_steps_html(etapas)

    meta_items = []
    if titulo:        meta_items.append(f'<li><strong>Título:</strong> {titulo}</li>')
    if objetivo:      meta_items.append(f'<li><strong>Objetivo:</strong> {objetivo}</li>')
    if responsavel:   meta_items.append(f'<li><strong>Responsável:</strong> {responsavel}</li>')
    if sistema:       meta_items.append(f'<li><strong>Sistema:</strong> {sistema}</li>')
    meta_html = f'<ul class="metadata">{"".join(meta_items)}</ul>' if meta_items else ''

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>{titulo}</title>
</head>
<body>

  {header_block}

  <div class="doc-body">
    <p class="intro-text">
      Este documento visa facilitar as rotinas de trabalho do setor operacional,
      consulte sempre que necessário.
    </p>

    <p class="it-title">{nome_exibicao}</p>

    {meta_html}

    <hr class="divider">

    {steps_block}

    {body_html}

    <div class="it-footer">
      <span>Grupo Irigarr — Uso Interno</span>
      <span>Revisão: {revisao}</span>
    </div>
  </div>

</body>
</html>"""


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 3:
        print("Uso: python3 gerar_pdf.py <entrada.md> <saida.pdf>")
        sys.exit(1)

    md_path  = sys.argv[1]
    pdf_path = sys.argv[2]

    # Localiza raiz do repositório (pai de analises/)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root  = os.path.dirname(script_dir)

    with open(md_path, 'r', encoding='utf-8') as f:
        raw = f.read()

    fm, body = parse_frontmatter(raw)
    etapas   = extract_etapas(body)
    body_html = markdown.markdown(body, extensions=['tables', 'fenced_code'])

    header_img = load_header_image(repo_root)

    html_str = build_html(fm, body_html, etapas, header_img)

    HTML(string=html_str, base_url=repo_root).write_pdf(
        pdf_path,
        stylesheets=[CSS(string=CSS_TEMPLATE)]
    )
    print(f"PDF gerado: {pdf_path}")


if __name__ == '__main__':
    main()
