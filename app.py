from flask import Flask, request, render_template
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html',code = None)

@app.route('/submit', methods=['POST'])
def submit():
    url = "https://www.mirrativ.com/api/user/post_live_request"

    headers = {
        'Accept-Encoding': 'gzip',
        'Accept-Language': 'ja-JP',
        'Connection': 'Keep-Alive',
        'Content-Length': '39',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '',
        'Host': 'www.mirrativ.com',
        'HTTP_X_TIMEZONE': 'Asia/Tokyo',
        'User-Agent': 'MR_APP/10.97.0/Android/Switch/14',
        'x-ad': '3e817a49-fc1b-4189-b528-aa669dbff3b0',
        'x-adjust-adid': 'ae410de3406a5d6df75923be592e6a15',
        'x-client-unixtime': str(time.time()),
        'x-hw': 'nx',
        'x-idfv': 'd21578ba31e0e7e5',
        'x-network-status': '2',
        'x-os-push': '0',
        'x-referer': 'profile',
        'x-unity-framework': '5.19.0',
        'x-widevine-id': 'ZWFTZWFhYWFQZ3l0enRhaVFMTUJCaGN0U3RZY01qcgA='
    }

    user_id = request.form.get('user_id')
    count = request.form.get('count')

    data = {
        'user_id': user_id,
        'count': count,
        'where': 'profile'
    }

    response = requests.post(url, headers=headers, data=data)
    ut = time.time()
    code = response.status_code


    return render_template("result.html",code=code) 
    #sonify({"timestamp": ut, "response": response.text})
    
@app.route("/change",methods=['POST'])
def change():
    url = 'https://www.mirrativ.com/api/user/profile_edit'
    
    user_name = request.form.get('user_name')

    # フォームデータ
    data = {
        'user_id': '144854218',
        'name': user_name,
        'description': '',
        'links': '[{"url":""}]',
        'include_urge_users': '0',
        'dynamic_link': '',
        'birthday': '0101',
        'is_visible_birthday': '0',
        'is_vip_public': '1'
    }

    encoder = MultipartEncoder(fields=data, boundary='f014651e-7e09-4551-844f-6b8df29351b1')

    headers = {
        'Accept-Encoding': 'gzip',
        'Accept-Language': 'ja-JP',
        'Connection': 'Keep-Alive',
        'Content-Length': str(encoder.len),  
        'Content-Type': encoder.content_type,  
        'Cookie': '',
        'Host': 'www.mirrativ.com',
        'HTTP_X_TIMEZONE': 'Asia/Tokyo',
        'User-Agent': 'MR_APP/10.97.0/Android/Switch/14',
        'x-ad': '3e817a49-fc1b-4189-b528-aa669dbff3b0',
        'x-adjust-adid': 'ae410de3406a5d6df75923be592e6a15',
        'x-client-unixtime': '1734519201.257',
        'x-hw': 'nx',
        'x-idfv': 'd21578ba31e0e7e5',
        'x-network-status': '2',
        'x-os-push': '0',
        'x-referer': 'profile_edit',
        'x-unity-framework': '5.19.0',
        'x-widevine-id': 'ZWFTZWFhYWFQZ3l0enRhaVFMTUJCaGN0U3RZY01qcgA='
    }

    response = requests.post(url, headers=headers, data=encoder)
    code = response.status_code

    return render_template("form.html",code=code,name = user_name) 

if __name__ == '__main__':
    app.run(debug=True)
