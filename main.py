from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import matplotlib.pyplot as plt
import io
import pandas as pd

app = FastAPI()

@app.get("/iris")
async def get_iris():
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)
    plt.scatter(iris['sepal_length'],iris['sepal_width'])
    plt.title("Iris Data Visualisation")

    buffer = io.BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    plt.close()

    return StreamingResponse(buffer,media_type="image/png")

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)