"""Run next to your existing index.html:  python3 apply_seo.py
Replaces the old <title>/<meta description>/<meta theme-color> with seo-head.html.
Everything else (3D scenes, styles, icons) is untouched. A backup is saved as index.backup.html."""
import re, shutil
src = open('index.html', encoding='utf-8').read()
seo = open('seo-head.html', encoding='utf-8').read()
shutil.copy('index.html', 'index.backup.html')
src = re.sub(r'<title>.*?</title>\s*', '', src, count=1, flags=re.S)
src = re.sub(r'<meta name="description"[^>]*>\s*', '', src, count=1)
src = re.sub(r'<meta name="theme-color"[^>]*>\s*', '', src, count=1)
src = src.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n',
                  '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n' + seo, 1)
open('index.html', 'w', encoding='utf-8').write(src)
print('Done. Check index.html <head>.')
