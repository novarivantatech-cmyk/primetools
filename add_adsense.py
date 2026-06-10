import os

adsense = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9463360133738403" crossorigin="anonymous"></script>'

files = [f for f in os.listdir('.') if f.endswith('.html')]
count = 0

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()
        if '</head>' in content and adsense not in content:
            content = content.replace('</head>', adsense + '\n</head>')
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(content)
            count += 1
            print(f"Updated: {f}")
        else:
            print(f"Skipped: {f}")
    except Exception as e:
        print(f"Error in {f}: {e}")

print(f"\nDone! Updated {count} files.")