# Dependencies used:
import pandas as pd             # py -m pip install pandas
import plotly_express as px     # py -m pip install plotly-express kaleido
from fpdf import FPDF           # py -m pip install fpdf1
import sqlite3
from pathlib import Path


current_dir = Path.cwd()
db_path =  current_dir / "sales_dept.db"
Path("output").mkdir(parents = True, exist_ok = True)   # Creates output folder if it hasn't been created yet


# We start by writing the queries for our db, which then will be executed and stored into variables.
# We will reformat the total_sales_query a bit with pandas so the data returned can be transformed into the graph that we want

conn = sqlite3.connect(db_path)

total_sales_query = '''
SELECT sale_date, SUM(total_price) as total_sales
FROM sales
GROUP BY sale_date
ORDER BY sale_date ASC
'''

product_sales_query = '''
SELECT p.product_name, SUM(s.total_price) as total_sales
FROM sales s
INNER JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sales DESC
'''

top_customers_query = '''
SELECT c.first_name || ' ' || c.last_name as customer_name, SUM(s.total_price) as total_sales
FROM sales s
INNER JOIN customers c ON s.customer_id = c.customer_id
GROUP BY customer_name
ORDER BY total_sales DESC
LIMIT 15
'''

df1 = pd.read_sql(total_sales_query, conn)

# pandas converts date into object, let's convert it back to date so we can sort it correctly
df1['sale_date'] = pd.to_datetime(df1['sale_date'])   

# df1.info()   # To check data types 

df1 = df1.set_index('sale_date')
df1 = df1.resample('ME').sum() # https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects
df1['month'] = df1.index.strftime('%b %y')

df2 = pd.read_sql(product_sales_query, conn)
df3 = pd.read_sql(top_customers_query, conn)
#print(df2)
conn.close()


# Creating the graphs

#fig.show()
fig = px.bar(df1, x = 'month', y = 'total_sales', template = 'presentation', text = 'total_sales')
fig.update_layout(title = 'Total sales by month', xaxis_title='',yaxis_title = 'Total sales ($)',yaxis=dict(automargin=True), xaxis=dict(automargin=True))
fig.write_image(current_dir / 'output/Monthly sales.jpg', width = 1400, height = 500)

fig = px.bar(df2, x = 'product_name', y = 'total_sales', template = 'presentation', text = 'total_sales')
fig.update_layout(title = 'Total sales by product', xaxis_title='', yaxis_title = 'Total sales ($)',yaxis=dict(automargin=True), xaxis=dict(automargin=True))
fig.write_image(current_dir / 'output/Product sales.jpg', width = 1400, height = 500)

fig = px.bar(df3, x = 'customer_name', y = 'total_sales', template = 'presentation', text = 'total_sales')
fig.update_layout(title = 'Top customers by sales', xaxis_title='', yaxis_title = 'Total sales ($)',yaxis=dict(automargin=True), xaxis=dict(automargin=True))
fig.write_image(current_dir / 'output/Top customers.jpg', width = 1300, height = 500)

# Creating a PDF with all the graphs we made

pdf = FPDF()
pdf.add_page()
pdf.set_font(family = 'Arial', size = 21)
pdf.set_text_color(64,64,64)
pdf.cell(0, 20, '2021-2023 Sales Report', align='C', ln=1)

graph_files = [str(graph_file) for graph_file in current_dir.glob('output/*.jpg')]

for graph_file in graph_files:
    pdf.ln(10)
    pdf.image(graph_file, x=None, y=None, w=pdf.w - 20, h=0)


pdf.output(current_dir / 'output/Sales report.pdf', dest='F')