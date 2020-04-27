import requests

if __name__ == '__main__':
    filename = 'C:\\Users\\md705\\OneDrive\\Pictures\\ChiswickBridge.jpg'

    url = 'http://127.0.0.1:5000/v1/predict'
    files = {'image': open(filename, 'rb')}
    resp = requests.post(url, files=files)
    print(resp)