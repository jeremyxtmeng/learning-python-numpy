import csv
from pathlib import Path
def read_portfolio(filename):
    portfolio = []
    with open(filename) as file:
        #  with statement that precedes it
        #  declares a block of statements (or context) where the file (file) is going to be used
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            try:
                name = row[0]
                shares = int(row[2])
                price = float(row[3])
                holding = (name, shares, price)
                portfolio.append(holding)
            except ValueError as err:
                print('Bad row:', row)
                print('Reason:', err)
    print('I am here')
    return portfolio



def main():
    file_path=Path('public')
    portfolio = read_portfolio(file_path/'portfolio.csv')
    for name, shares, price in portfolio:
        print(f'{name:>10s} {shares:10d} {price:10.2f}')

if __name__ == '__main__':
    main()  


