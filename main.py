import jinja2
import pdfkit

from datetime import datetime

client_name = "my_name"

company_name = "my_company"

address = "my_location_street"

city = "my_city"

email = "my_email@gmail.com"

my_num = 1234

item1 = "TV"

subtotal1 = 19

item2 = "Couch"

subtotal2 = 20

item3 = "Washing Machine"

subtotal3 = 30

total = subtotal1 + subtotal2 + subtotal3

today_date = datetime.today().strftime("%d %b %Y")

month = datetime.today().strftime("%b")

account_num = "account_test"

invoice_num = 5

context = {"client_name": client_name,
           "company_name": company_name,
           "address": address,
           "city": city,
           "email": email,
           "my_num": my_num,
           "item1": item1,
           "subtotal1": subtotal1,
           "item2": item2,
           "subtotal2": subtotal2,
           "item3": item3,
           "subtotal3": subtotal3,
           "total": total,
           "today_date": today_date,
           "month": month,
           "account_num": account_num,
           "invoice_num": invoice_num
           }

#jinja2 is to prepare the template and the output text
template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

template = template_env.get_template("my_template.html")
output_text = template.render(context) #this is string

#pdfkit is to generate the pdf from the template (html) using wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf") #find the path on bash: which wkhtmltopdf
pdfkit.from_string(output_text, 'pdf_generated.pdf', configuration=config, css="my_style.css") # we use "from_string" method because the output_text is a string
