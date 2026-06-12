import os

files = [f for f in os.listdir('.') if f.endswith('.html')]
count = 0

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as fh:
            content = fh.read()
        if 'G-NM33GFQ1M0' in content:
            content = content.replace('G-NM33GFQ1M0', 'G-NMS3GFQ1M0')
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(content)
            count += 1
            print(f"Fixed: {f}")
    except Exception as e:
        print(f"Error in {f}: {e}")

print(f"\nDone! Fixed {count} files.")