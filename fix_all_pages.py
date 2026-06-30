import os

adsense = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9463360133738403" crossorigin="anonymous"></script>'

analytics = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-NMS3GFQ1M0"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-NMS3GFQ1M0');
</script>"""

# Files to SKIP (not real content pages)
skip_files = ['index.html', 'sitemap.xml', 'robots.txt', 'ads.txt', '.gitignore']

results = {
    'fixed_both': [],
    'fixed_adsense_only': [],
    'fixed_analytics_only': [],
    'already_ok': [],
    'too_thin': [],
    'errors': []
}

for filename in os.listdir('.'):
    if not filename.endswith('.html') or filename in skip_files:
        continue
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()

        original_len = len(html)
        changed = False

        if '</head>' not in html:
            results['errors'].append(f"{filename} - no </head> tag found")
            continue

        has_adsense = 'pagead2.googlesyndication.com' in html
        has_analytics = 'G-NMS3GFQ1M0' in html

        if not has_adsense or not has_analytics:
            inject = ''
            if not has_analytics:
                inject += analytics + '\n'
            if not has_adsense:
                inject += adsense + '\n'
            html = html.replace('</head>', inject + '</head>')
            changed = True

        # Check content length (rough heuristic for "thin content")
        text_only = html
        for tag in ['<script', '<style']:
            while tag in text_only:
                start = text_only.find(tag)
                end_tag = '</script>' if tag == '<script' else '</style>'
                end = text_only.find(end_tag, start)
                if end == -1:
                    break
                text_only = text_only[:start] + text_only[end+len(end_tag):]

        visible_text_len = len(text_only.replace('<', ' <').split())

        if changed:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)
            if not has_adsense and not has_analytics:
                results['fixed_both'].append(filename)
            elif not has_adsense:
                results['fixed_adsense_only'].append(filename)
            else:
                results['fixed_analytics_only'].append(filename)
        else:
            results['already_ok'].append(filename)

        if visible_text_len < 300:
            results['too_thin'].append(f"{filename} ({visible_text_len} words)")

    except Exception as e:
        results['errors'].append(f"{filename} - {e}")

print("=" * 60)
print(f"FIXED BOTH (AdSense + Analytics): {len(results['fixed_both'])}")
for f in results['fixed_both']: print(f"  + {f}")

print(f"\nFIXED ADSENSE ONLY: {len(results['fixed_adsense_only'])}")
for f in results['fixed_adsense_only']: print(f"  + {f}")

print(f"\nFIXED ANALYTICS ONLY: {len(results['fixed_analytics_only'])}")
for f in results['fixed_analytics_only']: print(f"  + {f}")

print(f"\nALREADY OK: {len(results['already_ok'])}")
for f in results['already_ok']: print(f"  = {f}")

print(f"\n⚠️  PAGES WITH THIN CONTENT (need FAQ/content sections): {len(results['too_thin'])}")
for f in results['too_thin']: print(f"  ! {f}")

if results['errors']:
    print(f"\nERRORS: {len(results['errors'])}")
    for f in results['errors']: print(f"  X {f}")

print("=" * 60)
print(f"\nTOTAL HTML FILES PROCESSED: {len(results['fixed_both']) + len(results['fixed_adsense_only']) + len(results['fixed_analytics_only']) + len(results['already_ok'])}")