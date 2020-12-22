from django.conf import settings

def getPredictions(Transactiontest):
    import pickle
    import os
    import xgboost
    from sklearn.ensemble import RandomForestClassifier
    import numpy as np
    import pandas as pd
    print(Transactiontest._meta.get_fields())
    print(type(Transactiontest._meta.get_fields()))
    lst=[]
    lst = [
        Transactiontest.step,
        Transactiontest.amount,
        Transactiontest.nameOrig,
        Transactiontest.old_balance_org,
        Transactiontest.new_balance_org ,
        Transactiontest.nameDest,
        Transactiontest.old_balance_dest,
        Transactiontest.new_balance_dest,
        Transactiontest.transaction_type
    ]
    print(lst)
    print('aaaaaaaaaaaaaaaaaaa')
    arr = np.array(lst).reshape(1,-1)
    type(arr)
    arr.shape
    import os
    cwd = os.getcwd()
    print(cwd)

    def data_preprocessing(data):
        
       droplist=['type','nameDest','nameOrig']
       #Ivde extracting nameOrig and nameDest where C is present
       data['OrigC']=data['nameOrig'].apply(lambda x: 1 if str(x).find('C')==0 else 0)
       data['DestC']=data['nameDest'].apply(lambda x: 1 if str(x).find('C')==0 else 0)
       #Ivde creating new feature for transfer and cash_out
       data['TRANSFER']=data['type'].apply(lambda x: 1 if x=='TRANSFER' else 0)
       data['CASH_OUT']=data['type'].apply(lambda x: 1 if x=='CASH_OUT' else 0)
       #Ivde extracting error in account balances
       data['Amount Error']=(abs(data['oldbalanceOrg']-data['newbalanceOrig'])-data['amount'])
       data = data.drop(labels=droplist,axis=1)
       return data

    
    df = pd.DataFrame(data = arr,
                  columns = ['step', 'amount', 'nameOrig','oldbalanceOrg', 'newbalanceOrig', 'nameDest', 
                  'oldbalanceDest', 'newbalanceDest', 'type'])

    df['step'] = df['step'].astype(int)
    df['amount'] = df['amount'].astype(float)
    df['oldbalanceOrg'] = df['oldbalanceOrg'].astype(float)
    df['newbalanceOrig'] = df['newbalanceOrig'].astype(float)
    df['oldbalanceDest'] = df['oldbalanceDest'].astype(float)
    df['newbalanceDest'] = df['newbalanceDest'].astype(float)


    df = data_preprocessing(df)
    
    model = pickle.load(open(os.path.join(settings.MODELS, 'randomforest.sav'),'rb'))
    prediction = model.predict(df)
    print(prediction)
    if prediction[0]==1:
        return "fraud"
    elif prediction[0] ==0:
        return "safe"

print('yayayyy')
