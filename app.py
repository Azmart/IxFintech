import streamlit as st
import pickle
import pandas as pd
import requests

API_KEY = 'sandbox-api-key'
API_URL = 'https://api.deshe.ai/v2'

# company_list = pickle.load(open('company_list.pkl', 'rb'))
company_list = pd.read_csv('identifier_mapper.csv')
companies = pd.DataFrame(company_list)

st.title('Desche App')

selected_company_name = st.selectbox(
    'Select a company to view details!',
    companies['company_name'].values
)

selected_option = st.selectbox(
    'Select a API request to carry',
    ('Get Lookup Data', 'Get Company Data', 'Get Fundamental Analysis', 'Get Technical Analysis', 'Get Key Developments',
     'Get Historical Market Data',
     )
)


class Stock:

    def __init__(self, identifier="", stock_symbol=""):

        self.identifier = identifier
        self.stock_symbol = stock_symbol

    def getIndentifier(self):

        params = {
            'identifier': self.stock_symbol
        }
        url = f'{API_URL}/lookup'
        headers = {'Api-Key': API_KEY}

        r = requests.get(url, headers=headers, params=params)
        result = r.json()
        return result

    def getCompanyData(self):

        params = {
            'identifier': self.stock_symbol
        }
        url = f'{API_URL}/company-data'
        headers = {'Api-Key': API_KEY}

        r = requests.get(url, headers=headers, params=params)
        result = r.json()
        return result

    def getKeyDevelopments(self):

        params = {
            'identifier': self.identifier
        }
        url = f'{API_URL}/key-developments'
        headers = {'Api-Key': API_KEY}

        r = requests.get(url, headers=headers, params=params)
        result = r.json()
        return result['data']

    def getTechnicalAnalysis(self):

        params = {
            'identifier': self.identifier
        }
        url = f'{API_URL}/technical-analysis'
        headers = {'Api-Key': API_KEY}

        r = requests.get(url, headers=headers, params=params)
        result = r.json()
        return result['data']

    def getFundamentalAnalysis(self):

        params = {
            'identifier': self.identifier
        }
        url = f'{API_URL}/fundamental-analysis'
        headers = {'Api-Key': API_KEY}

        r = requests.get(url, headers=headers, params=params)
        result = r.json()
        return result['data']

    def getHistoricalMarketData(self):

        params = {
            'identifier': self.identifier
        }
        url = f'{API_URL}/historical-market-data'
        headers = {'Api-Key': API_KEY}

        r = requests.get(url, headers=headers, params=params)
        result = r.json()
        return result['data']['historical_market_data']


company_id = ""


def getCompanyIdentifier(company_name):
    company_id = companies.loc[companies['company_name']
                               == company_name, 'company_id']


def getData(option):
    if (option == 'Get Lookup Data'):
        company = Stock(identifier=company_id)
        return company.getIndentifier()
    elif (option == 'Get Company Data'):
        company = Stock(identifier=company_id)
        print(company.getCompanyData())
    elif (option == 'Get Fundamental Analysis'):
        company = Stock(identifier=company_id)
        print(company.getFundamentalAnalysis())
    elif (option == 'Get Technical Analysis'):
        company = Stock(identifier=company_id)
        print(company.getTechnicalAnalysis())
    elif (option == 'Get Key Developments'):
        company = Stock(identifier=company_id)
        print(company.getKeyDevelopments())
    else:
        company = Stock(identifier=company_id)
        print(company.getHistoricalMarketData())


if st.button('Get'):
    getCompanyIdentifier(selected_company_name)
    company_data = getData(selected_option)
    st.write('Details are as follows:')
    st.write(company_data)
