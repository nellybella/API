from flask import Flask, jsonify, request, send_file
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/get_iris')
async def get_iris():
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)
    #return jsonify({"message": "Iris Dataset", "data":iris.to_dict()})
    plt.scatter(iris['sepal_length'], iris['sepal_width'])
    plt.savefig('iris.png')

    return send_file('iris.png')

if __name__ == "__main__":
    app.run(debug=True, port=8000)
