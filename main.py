import pandas as pd
import matplotlib.pyplot as plt

class Main: 

    def sanitize_data(self): 
        ''' 
        Combing through data from the CSV and extracting it 
        '''
        # Read the data from CSV file and extract the price, date of the stock 
        data_frame = pd.read_csv('APPL_Stocks.csv', usecols=['Open', 'Date'])

        return self.plot_data(data_frame['Open'], data_frame['Date'])


    def plot_data(self, prices, date): 
        ''' 
        Graphing the extracted data visually 
        ''' 
        # From extracted data plot the date (x-axis) and stock price (y-axis) 
        plt.plot(date, prices) 

        plt.title("APPL Stock Price")
        # Add the titles and label to the graph 
        plt.xlabel("Date")
        plt.ylabel("Open Price")

        #Display the plot 
        plt.show() 

        #save the plot as a PDF file 
        return plt.savefig("APPL Stock Prices.pdf")
    

# Instantiate and run the class 
if __name__ == "__main__":
    Main().sanitize_data()