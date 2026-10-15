"""src/template.html → index.html. 로고 SVG 를 페이지 안에 넣는다(외부 요청 없음).

    python build.py
"""
import pathlib
import re
import urllib.parse

root = pathlib.Path(__file__).parent
brand = root / 'src' / 'brand'


def svg(name):
    s = (brand / name).read_text(encoding='utf8').strip()
    s = re.sub(r'<\?xml[^>]*>\s*', '', s)
    # 크기는 CSS 가 정한다. 로고 이름은 감싼 링크의 aria-label 이 말한다.
    s = re.sub(r'\s(width|height)="[^"]*"', '', s, count=2)
    s = re.sub(r'<title>.*?</title>', '', s)
    return s.replace('role="img"', 'aria-hidden="true" focusable="false"', 1)


heights = [30, 55, 80, 45, 95, 60, 35, 70, 90, 50, 65, 85, 40, 75, 55, 95, 45, 60, 80, 35, 70, 50, 90, 40, 65, 55, 30, 45]
out = (root / 'src' / 'template.html').read_text(encoding='utf8')
out = (out.replace('{{LOGO_REVERSE}}', svg('lockup-reverse.svg'))
          .replace('{{LOGO_PRIMARY}}', svg('lockup-primary.svg'))
          .replace('{{SYMBOL_WHITE}}', svg('symbol-white.svg'))
          .replace('{{WAVE}}', ''.join(f'<i style="height:{h}%"></i>' for h in heights))
          .replace('{{FAVICON}}', urllib.parse.quote((brand / 'symbol-blue.svg').read_text(encoding='utf8').strip(), safe='')))
assert '{{' not in out, 'unreplaced placeholder'
(root / 'index.html').write_text(out, encoding='utf8', newline='\n')
print(f'index.html {len(out.encode("utf8")):,} bytes')
