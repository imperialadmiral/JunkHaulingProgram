import pandas as pd

MILEAGE = 10
GAS_PRICE = 4.39
CPM = GAS_PRICE / MILEAGE
DUMP_FEE = 16

class JunkHauler:

    def __init__(self, job_index, mileage, loads, load_fee, labor_fee):
        self.job_index = job_index
        self.mileage = mileage
        self.loads = loads
        self.load_fee = load_fee
        self.dump_fee = DUMP_FEE
        self.labor_fee = labor_fee

    def calculate(self):
        gas_cost = CPM * self.mileage
        gas_cost = round(gas_cost, 1)
        dump_cost = DUMP_FEE * self.loads
        labor_cost = self.labor_fee * self.loads
        total_load_fee = self.load_fee * self.loads

        revenues = (gas_cost + labor_cost + dump_cost + total_load_fee)
        expenses = (gas_cost + labor_cost + dump_cost)
        net_income = revenues - expenses

        revenues = {
                        'Job ID' : self.job_index,
                        'Gas' : gas_cost,
                        'Labor' : labor_cost,
                        'Dump' : dump_cost,
                        'Load' : total_load_fee,
                        'Total' : (gas_cost + labor_cost + dump_cost + total_load_fee)}

        expenses = {
                        'Job ID' : self.job_index,
                        'Gas' : gas_cost,
                        'Labor' : labor_cost,
                        'Dump' : dump_cost,
                        'Total' : (gas_cost + labor_cost + dump_cost)}

        financials = {
                        'Job ID' : self.job_index,
                        'Revenues' : revenues['Total'],
                        'Expenses' : expenses['Total'],
                        'NI' : net_income}

        rev_df = pd.DataFrame(revenues, index = [self.job_index])
        exp_df = pd.DataFrame(expenses, index = [self.job_index])
        fin_df = pd.DataFrame(financials, index = [self.job_index])

        book_name = (f'{self.job_index}financials.xlsx')

        rev_df.T
        exp_df.T
        fin_df.T

        writer = pd.ExcelWriter(book_name, engine='xlsxwriter')

        # Write each dataframe to a different worksheet.
        rev_df.to_excel(writer, sheet_name='Revenues', index = False)
        exp_df.to_excel(writer, sheet_name='Expenses', index = False)
        fin_df.to_excel(writer, sheet_name='Financials', index = False)

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()


        




        


        



        