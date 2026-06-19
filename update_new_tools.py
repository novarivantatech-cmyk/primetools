import os

adsense = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9463360133738403" crossorigin="anonymous"></script>'

analytics = '''<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-NMS3GFQ1M0"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-NMS3GFQ1M0');
</script>'''

new_files = [
    'percentage-calculator.html',
    'age-calculator.html',
    'discount-calculator.html'
]

for f in new_files:
    if os.path.exists(f):
        try:
            with open(f, 'r', encoding='utf-8') as fh:
                content = fh.read()
            if '</head>' in content:
                content = content.replace('</head>', analytics + '\n' + adsense + '\n</head>')
                with open(f, 'w', encoding='utf-8') as fh:
                    fh.write(content)
                print(f"Updated: {f}")
        except Exception as e:
            print(f"Error: {f} - {e}")
    else:
        print(f"Not found: {f} - make sure file is in PrimeTools folder")

print("\nDone!")