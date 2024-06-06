## Report generator

Report generator is a python program that takes input from an sql database and returns multiple graphs inside an easy-to-share, easy-to-read PDF file.
In this case, we create a fictional database from a sales department with its' products, customers and sales data, and make 3 graphs: total sales per month (in a determined timeline), top customers and sales per product.
These graphs get inserted into a PDF file and saved to your computer.


# Dependencies used:
```bash
pip install pandas
pip install plotly-express kaleido
pip install fpdf1
pip install faker
```
