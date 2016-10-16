from urllib import request

goog_url = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=8&b=15&c=2016&d=9&e=15&f=2016&g=d&ignore=.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    #connect to web
    csv_str = str(csv)
    #set it as a string
    lines = csv_str.split("\\n")
    #break to each line
    dest_url = r'goog.csv'
    #save to a place and called goog.csv
    fx = open(dest_url, "w")
    #open a file(name of the file, 'what you want to do with it')
    for line in lines:
        fx.write(line + '\n')
    fx.close()

download_stock_data('http://chart.finance.yahoo.com/table.csv?s=GOOG&a=8&b=15&c=2016&d=9&e=15&f=2016&g=d&ignore=.csv')

