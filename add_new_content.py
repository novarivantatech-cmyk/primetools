import os

content_map = {
    'percentage-calculator.html': '''
<section style="max-width:700px;margin:0 auto 40px;padding:0 16px;font-family:'Segoe UI',sans-serif;">
  <h2 style="font-size:22px;font-weight:700;color:#1a1a2e;margin-bottom:16px;">How to Use the Percentage Calculator</h2>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Our free Percentage Calculator offers 6 types of percentage calculations in one place. Whether you are a student solving maths problems, a shopkeeper calculating discounts, a businessman computing GST, or an employee calculating appraisal percentages, this tool handles everything instantly.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">6 Types of Percentage Calculations</h3>
  <ul style="font-size:15px;color:#555;line-height:2;padding-left:20px;margin-bottom:16px;">
    <li><strong>What is X% of Y?</strong> Example: What is 18% of 10000? Answer: 1800</li>
    <li><strong>X is what % of Y?</strong> Example: 450 is what % of 1800? Answer: 25%</li>
    <li><strong>Percentage Increase/Decrease</strong> Example: Price went from 800 to 1000. Increase = 25%</li>
    <li><strong>Find original value</strong> Example: After 20% increase price is 1200. Original = 1000</li>
    <li><strong>Add % to number</strong> Example: 10000 + 18% GST = 11800</li>
    <li><strong>Subtract % from number</strong> Example: 2000 - 25% discount = 1500</li>
  </ul>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Percentage Formula</h3>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">The basic percentage formula is: Percentage = (Value / Total Value) x 100. To find a percentage of a number: Result = (Percentage / 100) x Number. For percentage change: Change% = ((New Value - Old Value) / Old Value) x 100.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Frequently Asked Questions</h3>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How to calculate percentage of marks?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Percentage of marks = (Marks obtained / Total marks) x 100. Example: If you scored 450 out of 600, your percentage = (450/600) x 100 = 75%.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How to calculate percentage increase in salary?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Salary increase % = ((New Salary - Old Salary) / Old Salary) x 100. Example: Salary increased from 50000 to 60000. Increase = (10000/50000) x 100 = 20%.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">What is 10% of 1000?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">10% of 1000 = (10/100) x 1000 = 100. A quick trick: To find 10% of any number, simply divide it by 10. So 10% of 5000 = 500, 10% of 25000 = 2500.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How to calculate profit percentage?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Profit % = (Profit / Cost Price) x 100. Example: Bought item for 800, sold for 1000. Profit = 200. Profit % = (200/800) x 100 = 25%.</p>
  </div>
</section>''',

    'age-calculator.html': '''
<section style="max-width:620px;margin:0 auto 40px;padding:0 16px;font-family:'Segoe UI',sans-serif;">
  <h2 style="font-size:22px;font-weight:700;color:#1a1a2e;margin-bottom:16px;">How to Use the Age Calculator</h2>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Our free Age Calculator calculates your exact age in years, months, days, hours, and minutes from your date of birth. You can also calculate age on a specific date, useful for checking age eligibility for government schemes, school admissions, job applications, and passport requirements.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Common Uses of Age Calculator in India</h3>
  <ul style="font-size:15px;color:#555;line-height:2;padding-left:20px;margin-bottom:16px;">
    <li><strong>Government jobs:</strong> Check age eligibility for UPSC, SSC, Railways, Bank exams</li>
    <li><strong>School admission:</strong> Check if child meets age criteria for Class 1 admission</li>
    <li><strong>Passport application:</strong> Verify age for minor or adult passport</li>
    <li><strong>Senior citizen benefits:</strong> Check if you qualify at 60 years</li>
    <li><strong>Insurance:</strong> Calculate age for premium calculation</li>
    <li><strong>Retirement planning:</strong> Know exactly how many years to retirement</li>
  </ul>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Frequently Asked Questions</h3>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How is age calculated exactly?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Age is calculated by finding the difference between the current date and your date of birth in years, months, and days. Our calculator accounts for leap years and varying month lengths to give you the most accurate result.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">What is the age limit for government jobs in India?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Age limits vary by exam: UPSC IAS is 21-32 years with relaxation for SC/ST/OBC, SSC CGL is 18-32 years, Bank PO is 20-30 years, Railways is 18-36 years. Use our calculator to verify your exact age eligibility.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How to calculate age from Aadhaar card?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Simply enter the date of birth mentioned on your Aadhaar card in the Date of Birth field above and click Calculate Age. The calculator will show your exact current age in years, months, and days.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">At what age are you a senior citizen in India?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">In India, a person aged 60 years and above is considered a senior citizen. They get benefits like higher FD interest rates (0.5% extra), higher income tax exemption limit of 3 lakh, and priority in government services.</p>
  </div>
</section>''',

    'discount-calculator.html': '''
<section style="max-width:640px;margin:0 auto 40px;padding:0 16px;font-family:'Segoe UI',sans-serif;">
  <h2 style="font-size:22px;font-weight:700;color:#1a1a2e;margin-bottom:16px;">How to Use the Discount Calculator</h2>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Our free Discount Calculator helps you instantly find the final price after discount, the amount saved, and the effective discount percentage. It supports simple discount, finding discount percentage from prices, and multiple stacked discounts, perfect for shopping, retail business, and ecommerce.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Discount Formula</h3>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Discount Amount = Original Price x Discount% / 100. Final Price = Original Price - Discount Amount. Discount% = ((Original Price - Sale Price) / Original Price) x 100.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Common Uses in India</h3>
  <ul style="font-size:15px;color:#555;line-height:2;padding-left:20px;margin-bottom:16px;">
    <li>Big Billion Days and Great Indian Festival sales on Flipkart and Amazon</li>
    <li>Calculating discount on electronics, clothing, and furniture</li>
    <li>Finding best deal when multiple discounts are offered</li>
    <li>Retail shopkeepers setting sale prices</li>
    <li>Festive season offers and coupon calculations</li>
  </ul>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Frequently Asked Questions</h3>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How to calculate 30% discount on 2000?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Discount amount = 2000 x 30/100 = 600. Final price = 2000 - 600 = 1400. You save 600 rupees on this purchase. Use our calculator above to calculate any discount instantly.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How do multiple discounts work?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Multiple discounts are applied one after another, not added together. Example: 20% off and 10% off on 1000 rupees. First: 1000 - 20% = 800. Then: 800 - 10% = 720. Total saved = 280 which is 28% effective discount, not 30%.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">What is MRP and discount in India?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">MRP (Maximum Retail Price) is the highest price a product can be sold at in India as per consumer protection laws. Discount is calculated on MRP. Many ecommerce sites show X% off on MRP and our discount calculator helps you verify the actual savings.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How to find original price before discount?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">If final price is 800 after 20% discount, original price = 800 / (1 - 20/100) = 800 / 0.8 = 1000 rupees. Use the Find Discount % mode in our calculator and enter both prices to find the discount percentage applied.</p>
  </div>
</section>'''
}

adsense = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9463360133738403" crossorigin="anonymous"></script>'

analytics = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-NMS3GFQ1M0"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-NMS3GFQ1M0');
</script>"""

count = 0
for filename, section_content in content_map.items():
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                html = f.read()

            # Add analytics and adsense if not present
            if 'G-NMS3GFQ1M0' not in html:
                html = html.replace('</head>', analytics + '\n' + adsense + '\n</head>')

            # Add content section before </body>
            if 'Frequently Asked Questions' not in html:
                html = html.replace('</body>', section_content + '\n</body>')

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)
            count += 1
            print(f"Updated: {filename}")
        except Exception as e:
            print(f"Error in {filename}: {e}")
    else:
        print(f"Not found: {filename} - please copy file to PrimeTools folder first")

print(f"\nDone! Updated {count} files.")