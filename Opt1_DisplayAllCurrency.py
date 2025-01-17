def opt1():
    filePath = 'cryptoPortfolio.csv'
    file = open(filePath)
    data = file.readlines()
    print(data)
    file.close()