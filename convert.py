import re


conversion_rate = 1.37


with open("books.txt", "r", encoding="utf-8") as infile:
    lines = infile.readlines()


with open("books.txt", "w", encoding="utf-8") as outfile:
    for line in lines:
        match = re.search(r'£(\d+\.\d{2})', line)
        if match:
            gbp_price = float(match.group(1))
            usd_price = gbp_price * conversion_rate
            usd_text = f" (${usd_price:.2f})"
            line = line.rstrip() + usd_text + "\n"
        outfile.write(line)

print(" books.txt updated with USD prices.")
