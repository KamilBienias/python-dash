# Etap7. Odcinek: Callback - Przygotowanie danych do aplikacji

def fetch_financial_data(company='AMZN'):
    """
    This function fetch stock market quotations.
    """
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')

df = fetch_financial_data()

# resetuje index ktory byl na poczatku data
df = df.reset_index()
df = df[df.Date > '2019-01-01']

df.to_csv('AMZN.csv')
# mozna debuggowac. Wstawic breakpoint i prawym na df "View as DataFrame"
print()