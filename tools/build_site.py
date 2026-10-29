#!/usr/bin/env python3
"""Build the static portfolio privacy/deletion pages from localized content."""
import html
import json
from pathlib import Path
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[1]
BASE = '/rainbow-jump-privacy/'
ORIGIN = 'https://tosoftwarestudio.github.io'
LOCALES = ('pt-BR', 'en', 'es')
NAMES = {'pt-BR': 'Português', 'en': 'English', 'es': 'Español'}
DATA = {key: json.loads((ROOT / 'content' / (key + '.json')).read_text()) for key in LOCALES}


def href(locale, deletion=False):
    data = DATA[locale]
    return BASE + data['prefix'] + (data['delete_path'] if deletion else '')


def render(locale, deletion):
    d = DATA[locale]
    title = d['deletion_title'] if deletion else d['policy_title']
    sections = d['delete_sections'] if deletion else d['sections']
    intro = d['delete_intro'] if deletion else d['intro']
    languages = '\n'.join(f'<a href="{href(key, deletion)}" lang="{DATA[key]["lang"]}" hreflang="{DATA[key]["lang"]}"' + (' aria-current="page"' if key == locale else '') + f'>{NAMES[key]}</a>' for key in LOCALES)
    alternates = '\n'.join(f'<link rel="alternate" hreflang="{DATA[key]["lang"]}" href="{ORIGIN}{href(key, deletion)}">' for key in LOCALES)
    toc = '\n'.join(f'<a href="#{sid}">{html.escape(heading)}</a>' for sid, heading, _ in sections)
    content = []
    for sid, heading, paragraphs in sections:
        body = []
        for text in paragraphs:
            text = text.replace('{deletion}', href(locale, True)).replace('{privacy}', href(locale))
            tag = 'div class="text-block"' if '<ul>' in text else 'p'
            closing = 'div' if '<ul>' in text else 'p'
            body.append(f'<{tag}>{text}</{closing}>')
        contact = ' id="contact" class="contact"' if sid in ('alteracoes', 'andamento') else ''
        content.append(f'<section id="{sid}">\n<h2>{html.escape(heading)}</h2>\n<div{contact}>\n' + '\n'.join(body) + '\n</div>\n</section>')
    email = 'mailto:tosoftwarestudio@gmail.com?' + urlencode({'subject': d['email_subject'], 'body': d['email_body']})
    summary = '' if deletion else '<div class="summary"><p>' + html.escape(d['summary']) + '</p></div>'
    action = f'<p><a class="button" href="{html.escape(email, quote=True)}">{html.escape(d["email_button"])}</a></p>' if deletion else ''
    return f'''<!doctype html>
<html lang="{d['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{html.escape(intro, quote=True)}">
<meta name="color-scheme" content="light">
<meta name="referrer" content="no-referrer">
<link rel="canonical" href="{ORIGIN}{href(locale, deletion)}">
{alternates}
<link rel="stylesheet" href="{BASE}assets/style.css">
<title>{html.escape(title)} — To Software</title>
</head>
<body>
<a class="skip" href="#conteudo">{html.escape(d['skip'])}</a>
<header><div class="brand"><a href="{href(locale)}"><span class="dot" aria-hidden="true"></span>TO SOFTWARE <span aria-hidden="true">/</span> <small>{html.escape(d['brand'])}</small></a><a href="mailto:tosoftwarestudio@gmail.com">{html.escape(d['contact'])}</a></div></header>
<div class="layout">
<aside><nav aria-label="{html.escape(d['nav'])}"><p>{html.escape(d['nav'])}</p>{toc}</nav></aside>
<main id="conteudo">
<nav class="languages" aria-label="Language / Idioma">{languages}</nav>
<div class="eyebrow">To Software · Games</div>
<h1>{html.escape(title)}</h1>
<p class="updated">{html.escape(d['updated'])}: <time datetime="2026-10-29">{d['date']}</time></p>
<p class="intro">{html.escape(intro)}</p>
{summary}
{action}
{chr(10).join(content)}
</main></div>
<footer><span>© 2026 To Software</span><span><a href="{href(locale)}">{html.escape(d['policy_title'])}</a> · <a href="{href(locale, True)}">{html.escape(d['deletion_title'])}</a></span></footer>
</body></html>
'''


for locale in LOCALES:
    for deletion in (False, True):
        relative = href(locale, deletion).removeprefix(BASE)
        output = ROOT / relative / 'index.html'
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(render(locale, deletion))
print('Built 6 static pages in pt-BR, en-US and es; legacy URLs retained.')
