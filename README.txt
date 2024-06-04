Hi! In this project, I create a sqlite database populated with random made-up data from a sales department, composed of its' customers, products, and all sales (data_creation, db_creation)
Then, in graph.py I connect to the db, write a couple of simple sql queries that will fetch the data used to make the graphs, and put them into a business-ready PDF.
These graphs are customisable: instead of graphs they could be lines or maps, or also exported to .csv

I'm uploading the random database that was created along with the graphs and pdf in the 'output' folder
Dependencies used:

py -m pip install pandas
py -m pip install plotly-express kaleido
py -m pip install fpdf1
py -m pip install faker