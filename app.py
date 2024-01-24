from flask import Flask, render_template, request,  redirect, url_for,jsonify
import requests

app=Flask(__name__)

# @app.route('/')
# def welcome():
#     return "Welcome"

@app.route("/",methods=["GET","POST"])
def weather():
    if request.method=="GET":
        return render_template("index.html")
    else:
        city = request.form["city"]
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?key=VKKUQ6APVMMSX79QYT5LMEJFX"
        response = requests.get(url)
        if response.status_code == 200:
            # API call was successful
            data = response.json()  # Parse the JSON response
            # print(data)
        else:
            # API call failed
            print(f"Error {response.status_code}: {response.text}")
        lat=data["latitude"]
        long=data["longitude"]
        temp=round((data["days"][0]["temp"]-32)*(5/9),2)
        flike=round((data["days"][0]["feelslike"]-32)*(5/9),2)  
        desc=data["description"]
        alerts=data["alerts"]

        return render_template("result.html", city=city, lat=lat, long=long, temp=temp, flike=flike, desc=desc, alerts=alerts)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
