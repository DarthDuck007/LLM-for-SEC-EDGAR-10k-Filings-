# LLM-for-SEC-EDGAR-10k-Filings-

-The whole project was completed using Google Collab for data extraction and model training and VS Code was used to deploy Streamlit App.
#The project is divided into 3 stages:
-Stage 1: Extracting past 20-30 years SEC "Form 10K" data for Microsoft and Apple. Converting the data into a readable format and downloading the txt/pdf files
-Stage 2: Importing those PDF/TXT files, converting them into a model trainable data, fine tuning the LLM with Gemini API and the data and then extracting relevent insights from the LLM Based on the data.
-Stage 3: Visualizing the data and insights using Streamlit library for Python. 

#Stage 1: Colab File - AAPL,MSFT SEC edgar.ipynb

-We use edgartools library to import specificially form 10K filings for Apple and Microsoft. 
-Filings from 2003 onwards till 2023 were imported for Apple and 1994 onwards till 2023 were imported for Microsoft.
-They were then stored as txt files into a folder which was then downloaded.
-They were then converted into pdfs. All the files which were stored as txt's were converted into pdf's as a whole using online tools/python, python libraries can also be used however they were resulting in loss of data hence manual methods were applied, however libraries like reportlab and fpdf can be used for automation of this task. 

#Stage 2: Colab File - llm in 10k filings.ipynb
-We use langchain and Gemini API for fine tuning the model.
-We Initially import the data on colab, however the data can also be directly uploaded and will be available in the repository to directly upload to collab
-We then split the pdf's intp multiple pages and create chains which will be used as our training data.
-We train the Gemini-Pro model, since it has a limit of 1,000,000 tokens and each pdf contains ~20000-35000 letters, only 2-5 pdfs can be used for training/analysis at once
-We then extract insights from the model and download them as txt files.

#Stage 3:
-We create a new py file Stock_Dashboard.py and using streamlit deploy it as a locally hosted app.
-Insight data and numbers which were provided to us was raw data by Gemini-pro llm hence visualizations were created manually, the insights however can be directly imported from download txt files. They were however formatted and then written to preserve asthethics of the deployed app.
