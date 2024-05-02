from django.shortcuts import render
from .modules.model import is_failure, failure_type
from django.http import FileResponse
import pandas as pd
import requests as rq

def index(request):
    if request.method == 'POST':
        f = request.FILES['file'].read()
        with open('uploaded/input.csv', 'wb') as f1:
            f1.write(f)

        df = pd.read_csv('uploaded/input.csv')

        df['is_failure'] = is_failure(df)
        df['failure_type'] = failure_type(df)

        df = df[df['is_failure'] == 1]

        df.to_csv('uploaded/output.csv', index=False)
        
        url = "http://localhost:3000/upload"

        payload = {}
        files=[('csvFile',('output.csv',open('uploaded/output.csv', 'rb'),'text/csv'))]
        headers = {}

        APIresponse = rq.request("POST", url, headers=headers, data=payload, files=files)
        print(APIresponse.text)
        
        response = FileResponse(open('uploaded/output.csv', 'rb'))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename=output.csv'

        return response
    
    return render(request, 'index.html')