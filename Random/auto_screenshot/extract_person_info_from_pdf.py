"""
This is a script for Yilin to save some effort during her internship
Hope it helps :)
"""

import pandas as pd
import pdfquery

# read the PDF
pdf = pdfquery.PDFQuery('your_website_screen_capture.pdf')
print(pdf.load())

# convert the pdf to XML
pdf.tree.write('customers.xml', pretty_print=True)
print(pdf)

# access the data using coordinates
customer_name = pdf.pq('LTTextLineHorizontal:in_bbox("68.0, 231.57, 101.990, 234.893")').text()

print(customer_name)

#output: Brandon James
