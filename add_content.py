import os

# Content to add before </body> on each page
content_map = {
    'gst-calculator.html': '''
<section style="max-width:640px;margin:0 auto 40px;padding:0 16px;font-family:'Segoe UI',sans-serif;">
  <h2 style="font-size:22px;font-weight:700;color:#1a1a2e;margin-bottom:16px;">How to Use the GST Calculator</h2>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Our free GST Calculator helps you calculate Goods and Services Tax instantly. Simply enter the amount, select the GST rate (5%, 12%, 18%, or 28%), and choose whether you want to add GST to a price or remove GST from a GST-inclusive price.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Steps to Calculate GST</h3>
  <ol style="font-size:15px;color:#555;line-height:2;padding-left:20px;">
    <li>Enter the original amount in the Amount field</li>
    <li>Select the applicable GST rate — 5%, 12%, 18%, or 28%</li>
    <li>Choose "Add GST to amount" or "Remove GST from amount"</li>
    <li>Click Calculate GST to see the result instantly</li>
  </ol>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">GST Rates in India</h3>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">India has four main GST slabs: 5% for essential goods, 12% for standard goods, 18% for most services and goods, and 28% for luxury items. CGST and SGST are each half of the total GST rate for intra-state transactions.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Frequently Asked Questions</h3>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">What is GST?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">GST (Goods and Services Tax) is an indirect tax levied on the supply of goods and services in India. It replaced multiple indirect taxes like VAT, service tax, and excise duty.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">What is the difference between CGST and SGST?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">CGST (Central GST) goes to the central government and SGST (State GST) goes to the state government. Together they make up the total GST. For example, 18% GST = 9% CGST + 9% SGST.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How to calculate GST on ₹10,000 at 18%?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">GST amount = ₹10,000 × 18/100 = ₹1,800. Total price with GST = ₹10,000 + ₹1,800 = ₹11,800. CGST = ₹900, SGST = ₹900.</p>
  </div>
</section>''',

    'emi-calculator.html': '''
<section style="max-width:640px;margin:0 auto 40px;padding:0 16px;font-family:'Segoe UI',sans-serif;">
  <h2 style="font-size:22px;font-weight:700;color:#1a1a2e;margin-bottom:16px;">How to Use the EMI Calculator</h2>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Our EMI Calculator helps you calculate the monthly loan instalment for home loans, car loans, personal loans, and education loans. Enter the loan amount, interest rate, and tenure to instantly see your EMI, total interest, and full payment schedule.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">EMI Formula</h3>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">EMI = P × r × (1+r)^n / ((1+r)^n - 1) where P = Principal loan amount, r = Monthly interest rate, n = Number of monthly instalments.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Frequently Asked Questions</h3>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">What is EMI?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">EMI stands for Equated Monthly Instalment. It is the fixed amount paid every month to repay a loan. Each EMI consists of a principal component and an interest component.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">What is the EMI for ₹10 lakh home loan at 8.5% for 20 years?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">For a ₹10,00,000 loan at 8.5% per annum for 20 years, the EMI would be approximately ₹8,678 per month. You can use our calculator above to calculate for your specific loan details.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How can I reduce my EMI?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">You can reduce your EMI by increasing the loan tenure, making a larger down payment, negotiating a lower interest rate, or making prepayments to reduce the outstanding principal.</p>
  </div>
</section>''',

    'income-tax.html': '''
<section style="max-width:640px;margin:0 auto 40px;padding:0 16px;font-family:'Segoe UI',sans-serif;">
  <h2 style="font-size:22px;font-weight:700;color:#1a1a2e;margin-bottom:16px;">How to Calculate Income Tax in India</h2>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Our Income Tax Calculator helps salaried individuals, self-employed professionals, and business owners calculate their income tax for FY 2025-26. Compare the old regime and new regime to find which saves you more tax.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">New Tax Regime Slabs FY 2025-26</h3>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Up to ₹3 lakh: Nil | ₹3–6 lakh: 5% | ₹6–9 lakh: 10% | ₹9–12 lakh: 15% | ₹12–15 lakh: 20% | Above ₹15 lakh: 30%. Income up to ₹7 lakh is fully tax-free under the new regime due to Section 87A rebate.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Frequently Asked Questions</h3>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">Which tax regime is better — old or new?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">If you have significant deductions like HRA, 80C, home loan interest totalling more than ₹3.75 lakh, the old regime may save more tax. Otherwise, the new regime with lower slab rates is generally better. Use our Compare tool above.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How much tax on ₹10 lakh salary in FY 2025-26?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Under the new regime, tax on ₹10 lakh salary after standard deduction of ₹75,000 = ₹9,25,000 taxable income. Total tax = approximately ₹60,000 + 4% cess = ₹62,400.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">What is the standard deduction for salaried employees?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">The standard deduction for salaried employees is ₹75,000 per year under the new tax regime and ₹50,000 under the old tax regime for FY 2025-26.</p>
  </div>
</section>''',

    'sip-calculator.html': '''
<section style="max-width:640px;margin:0 auto 40px;padding:0 16px;font-family:'Segoe UI',sans-serif;">
  <h2 style="font-size:22px;font-weight:700;color:#1a1a2e;margin-bottom:16px;">How to Use the SIP Calculator</h2>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">A SIP (Systematic Investment Plan) Calculator helps you estimate the future value of your monthly mutual fund investments. Enter your monthly SIP amount, expected annual return rate, and investment period to calculate your total corpus.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">SIP Formula</h3>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">M = P × ({[1 + i]^n – 1} / i) × (1 + i) where M = Maturity amount, P = Monthly SIP amount, i = Monthly interest rate, n = Number of months.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Frequently Asked Questions</h3>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">What is SIP?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">SIP or Systematic Investment Plan is a method of investing a fixed amount regularly in mutual funds. It helps build wealth through the power of compounding and rupee cost averaging.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How much will ₹5,000 SIP grow in 10 years?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">A monthly SIP of ₹5,000 at 12% annual return for 10 years will grow to approximately ₹11.6 lakhs. You invest ₹6 lakhs and earn about ₹5.6 lakhs as returns.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">Is SIP safe?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">SIP in mutual funds is subject to market risks. However, investing regularly over long periods (5+ years) generally reduces risk through rupee cost averaging. Always read scheme documents before investing.</p>
  </div>
</section>''',

    'fd-calculator.html': '''
<section style="max-width:640px;margin:0 auto 40px;padding:0 16px;font-family:'Segoe UI',sans-serif;">
  <h2 style="font-size:22px;font-weight:700;color:#1a1a2e;margin-bottom:16px;">How to Use the FD Calculator</h2>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Our Fixed Deposit Calculator helps you calculate the maturity amount and interest earned on your FD. Enter the principal amount, interest rate, tenure, and compounding frequency to see your returns instantly.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">FD Interest Rates 2026</h3>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">FD rates in India range from 6.5% to 9% depending on the bank and tenure. Senior citizens get an additional 0.25% to 0.75% interest. Small Finance Banks typically offer higher rates than large banks.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Frequently Asked Questions</h3>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">What is a Fixed Deposit?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">A Fixed Deposit is a financial instrument where you deposit a lump sum amount with a bank for a fixed period at a predetermined interest rate. It is one of the safest investment options in India with guaranteed returns.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How is FD interest calculated?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">FD interest is usually compounded quarterly. Formula: A = P(1 + r/n)^(nt) where P = Principal, r = Annual rate, n = Compounding frequency (4 for quarterly), t = Time in years.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">Is FD interest taxable in India?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Yes, FD interest is fully taxable as per your income tax slab. If interest exceeds ₹40,000 per year (₹50,000 for senior citizens), the bank deducts TDS at 10%. Tax Saver FDs with 5-year lock-in qualify for Section 80C deduction.</p>
  </div>
</section>''',

    'currency-converter.html': '''
<section style="max-width:640px;margin:0 auto 40px;padding:0 16px;font-family:'Segoe UI',sans-serif;">
  <h2 style="font-size:22px;font-weight:700;color:#1a1a2e;margin-bottom:16px;">How to Use the Currency Converter</h2>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Our live Currency Converter lets you convert between 30+ world currencies instantly with real-time exchange rates. Select your source currency, target currency, enter the amount, and get the converted value immediately.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Popular Currency Pairs for India</h3>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">The most popular currency conversions for Indian users include USD to INR, Euro to INR, GBP to INR, AED to INR (UAE Dirham), and SGD to INR. Rates are updated daily from live forex markets.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Frequently Asked Questions</h3>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">What is today's USD to INR rate?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">The USD to INR exchange rate fluctuates daily based on RBI guidelines and global forex markets. Use our live converter above to get the current rate instantly.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">Are the exchange rates accurate?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Our rates are sourced from live forex APIs and updated regularly. However, bank and money transfer rates may differ slightly due to their own margins. Use these rates as a reference.</p>
  </div>
</section>''',

    'salary-slip.html': '''
<section style="max-width:640px;margin:0 auto 40px;padding:0 16px;font-family:'Segoe UI',sans-serif;">
  <h2 style="font-size:22px;font-weight:700;color:#1a1a2e;margin-bottom:16px;">How to Generate a Salary Slip</h2>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Our free Salary Slip Generator creates professional payslips for employees in India. Fill in company details, employee information, earnings (Basic, HRA, allowances) and deductions (PF, TDS) to generate a printable salary slip instantly.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Components of a Salary Slip</h3>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">A salary slip includes earnings like Basic Salary, HRA, Conveyance, Medical Allowance, and Special Allowance, and deductions like PF (12% of Basic), Professional Tax, and TDS. Net Salary = Total Earnings - Total Deductions.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Frequently Asked Questions</h3>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">Is this salary slip valid for official use?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">This tool generates salary slip templates for reference and internal use. For official purposes like loan applications, the salary slip should be issued by your employer on company letterhead with authorised signature.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How is PF calculated on salary slip?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">PF (Provident Fund) is calculated at 12% of the Basic Salary. Both employee and employer contribute 12% each. The employee's contribution is deducted from salary and shown as a deduction on the salary slip.</p>
  </div>
</section>''',

    'invoice-generator.html': '''
<section style="max-width:640px;margin:0 auto 40px;padding:0 16px;font-family:'Segoe UI',sans-serif;">
  <h2 style="font-size:22px;font-weight:700;color:#1a1a2e;margin-bottom:16px;">How to Create a GST Invoice</h2>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Our GST Invoice Generator creates professional tax invoices compliant with Indian GST law. Fill in seller and buyer details, add items, select GST rate, and download a printable GST invoice as PDF instantly — completely free.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Mandatory Fields in a GST Invoice</h3>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">A valid GST invoice must include: Supplier name and GSTIN, Buyer name and address, Invoice number and date, Description of goods/services, HSN/SAC code, GST rate and amount (CGST+SGST or IGST), and total amount.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Frequently Asked Questions</h3>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">Who needs to issue a GST invoice?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Any GST registered business supplying goods or services must issue a GST invoice. If your annual turnover exceeds ₹20 lakh (₹10 lakh in special category states), GST registration and invoicing is mandatory.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">What is the difference between CGST, SGST, and IGST?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">For intra-state sales (within the same state), CGST and SGST apply equally. For inter-state sales (between states), IGST applies. Our invoice generator automatically splits GST into CGST and SGST.</p>
  </div>
</section>''',

    'unit-converter.html': '''
<section style="max-width:640px;margin:0 auto 40px;padding:0 16px;font-family:'Segoe UI',sans-serif;">
  <h2 style="font-size:22px;font-weight:700;color:#1a1a2e;margin-bottom:16px;">How to Use the Unit Converter</h2>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Our Unit Converter supports 8 categories: Length, Weight, Temperature, Area, Volume, Speed, Data, and Time. Select a category, choose your units, enter the value and get instant conversion with all equivalent values shown at once.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Common Unit Conversions</h3>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">1 kilometre = 1000 metres | 1 kilogram = 1000 grams | 1 litre = 1000 millilitres | 0°C = 32°F | 1 mile = 1.609 km | 1 inch = 2.54 cm | 1 acre = 4047 sq metres | 1 GB = 1024 MB.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Frequently Asked Questions</h3>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How to convert Celsius to Fahrenheit?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Formula: °F = (°C × 9/5) + 32. Example: 37°C = (37 × 9/5) + 32 = 98.6°F. Use our temperature converter above for instant results.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How many feet in a metre?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">1 metre = 3.28084 feet. So 10 metres = 32.8 feet. Use our length converter to convert between metres, feet, inches, centimetres and more.</p>
  </div>
</section>''',

    'hra-calculator.html': '''
<section style="max-width:640px;margin:0 auto 40px;padding:0 16px;font-family:'Segoe UI',sans-serif;">
  <h2 style="font-size:22px;font-weight:700;color:#1a1a2e;margin-bottom:16px;">How to Calculate HRA Exemption</h2>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">HRA (House Rent Allowance) exemption under Section 10(13A) is the least of three amounts: actual HRA received, 50% of basic salary for metro cities (40% for non-metro), or actual rent paid minus 10% of basic salary.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Metro vs Non-Metro Cities</h3>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Metro cities for HRA exemption are Delhi, Mumbai, Kolkata, and Chennai — these get 50% of basic salary. All other cities including Pune, Bangalore, Hyderabad, Ahmedabad are classified as non-metro — getting 40% of basic salary.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Frequently Asked Questions</h3>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">Can I claim HRA under the new tax regime?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">No. HRA exemption is only available under the old tax regime. Under the new tax regime, HRA received is fully taxable as part of your salary income.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">Do I need rent receipts to claim HRA?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Yes. You need rent receipts to submit to your employer. If annual rent exceeds ₹1 lakh, you also need the landlord's PAN card. Keep receipts for all 12 months to claim full exemption.</p>
  </div>
</section>''',

    'rd-calculator.html': '''
<section style="max-width:640px;margin:0 auto 40px;padding:0 16px;font-family:'Segoe UI',sans-serif;">
  <h2 style="font-size:22px;font-weight:700;color:#1a1a2e;margin-bottom:16px;">How to Use the RD Calculator</h2>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">A Recurring Deposit (RD) is a savings scheme where you deposit a fixed amount every month and earn interest. Our RD Calculator shows you the maturity amount and total interest for any monthly deposit, interest rate, and tenure.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">RD Interest Rates 2026</h3>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Current RD rates in India range from 6.5% to 8.25% depending on the bank. SBI offers 7%, HDFC offers 7.4%, and small finance banks offer up to 8.5%. Senior citizens get an additional 0.5% interest rate.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Frequently Asked Questions</h3>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">What is the difference between RD and FD?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">In a Fixed Deposit you deposit a lump sum once, while in a Recurring Deposit you deposit a fixed amount every month. RD is ideal for those who want to save regularly from their monthly salary.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">Is RD interest taxable?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Yes. RD interest is fully taxable as per your income tax slab. TDS is deducted if total interest from all deposits in a bank exceeds ₹40,000 per year (₹50,000 for senior citizens).</p>
  </div>
</section>''',

    'ppf-calculator.html': '''
<section style="max-width:640px;margin:0 auto 40px;padding:0 16px;font-family:'Segoe UI',sans-serif;">
  <h2 style="font-size:22px;font-weight:700;color:#1a1a2e;margin-bottom:16px;">About Public Provident Fund (PPF)</h2>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">PPF is one of India's most popular long-term savings schemes backed by the Government of India. It offers tax-free returns under the EEE (Exempt-Exempt-Exempt) status — investment, interest, and maturity are all tax-free.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">PPF Key Features</h3>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Lock-in period: 15 years | Current interest rate: 7.1% per annum | Minimum deposit: ₹500/year | Maximum deposit: ₹1,50,000/year | Tax benefit: Section 80C deduction up to ₹1.5 lakh | Available at: Post offices and major banks.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Frequently Asked Questions</h3>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">Can I withdraw PPF before 15 years?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Partial withdrawal is allowed from the 7th year onwards — up to 50% of the balance at the end of the 4th year. Full premature closure is only allowed in specific circumstances like medical emergencies after 5 years.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">How much will ₹1.5 lakh/year in PPF grow in 15 years?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">At current rate of 7.1%, investing ₹1,50,000 per year for 15 years will give you approximately ₹40.68 lakhs at maturity. Total investment = ₹22.5 lakh, total interest earned = ₹18.18 lakh, all completely tax-free.</p>
  </div>
</section>''',

    'interest-calculator.html': '''
<section style="max-width:640px;margin:0 auto 40px;padding:0 16px;font-family:'Segoe UI',sans-serif;">
  <h2 style="font-size:22px;font-weight:700;color:#1a1a2e;margin-bottom:16px;">Simple Interest vs Compound Interest</h2>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Simple Interest is calculated only on the principal amount, while Compound Interest is calculated on the principal plus accumulated interest. Compound interest grows faster over time — this is why Albert Einstein called it the "eighth wonder of the world".</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Formulas</h3>
  <p style="font-size:15px;color:#555;line-height:1.8;margin-bottom:12px;">Simple Interest: SI = P × R × T / 100 | Compound Interest: CI = P × (1 + R/n)^(n×T) - P where P = Principal, R = Rate per annum, T = Time in years, n = Compounding frequency per year.</p>
  <h3 style="font-size:18px;font-weight:700;color:#1a1a2e;margin:20px 0 10px;">Frequently Asked Questions</h3>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">Where is simple interest used in India?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">Simple interest is used in short-term personal loans, vehicle loans, and some government schemes. Most bank savings accounts and FDs use compound interest which gives higher returns.</p>
  </div>
  <div style="border:1px solid #e0f7f3;border-radius:10px;padding:16px;margin-bottom:10px;">
    <p style="font-weight:700;color:#1a1a2e;margin-bottom:6px;">What is the Rule of 72?</p>
    <p style="font-size:14px;color:#555;line-height:1.7;">The Rule of 72 is a quick way to estimate how long it takes to double your money. Divide 72 by the interest rate. Example: At 8% interest, your money doubles in 72/8 = 9 years.</p>
  </div>
</section>'''
}

count = 0
for filename, content in content_map.items():
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                html = f.read()
            if '</body>' in html and 'Frequently Asked Questions' not in html:
                html = html.replace('</body>', content + '\n</body>')
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(html)
                count += 1
                print(f"Updated: {filename}")
            else:
                print(f"Skipped (already has content): {filename}")
        except Exception as e:
            print(f"Error in {filename}: {e}")
    else:
        print(f"File not found: {filename}")

print(f"\nDone! Updated {count} files with rich content.")