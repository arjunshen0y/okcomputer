from django.conf import settings

def getPredictions(Transactiontest):
    import pickle
    import os
    import xgboost
    import numpy as np
    import pandas as pd
    print(Transactiontest._meta.get_fields())
    print(type(Transactiontest._meta.get_fields()))
    lst=[]
    lst=[Transactiontest.amount,Transactiontest.old_balance_org,Transactiontest.new_balance_org ,Transactiontest.old_balance_dest,Transactiontest.new_balance_dest,Transactiontest.cat]
    print(lst)
    print('aaaaaaaaaaaaaaaaaaa')
    arr = np.array(lst).reshape(1,-1)
    type(arr)
    arr.shape
    import os
    cwd = os.getcwd()
    print(cwd)

    df = pd.DataFrame(data = arr,
                  columns = ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'cat'])


    model = pickle.load(open(os.path.join(settings.MODELS, 'testing_model.sav'),'rb'))



    prediction= model.predict(df)


    print(prediction)
    if prediction[0]==1:
        return "fraud"
    elif prediction[0] ==0:
        return "safe"

print('yayayyy')
