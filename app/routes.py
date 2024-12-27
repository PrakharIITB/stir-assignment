from flask import Blueprint, render_template, jsonify,request
from app.services.selenium_service import get_ip_address, login_and_fetch_X_trends
from app.services.mongodb_service import save_to_mongodb
import os

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/fetch_trends', methods=['GET','POST'])
def fetch_trends():
    try:
        twitter_username = os.getenv("TWITTER_USERNAME")
        twitter_password = os.getenv("TWITTER_PASSWORD")

        ip_address = get_ip_address()
        # ip_address = "20.206.106.192"

        print("ip_address : ",ip_address)

        if not ip_address:
            return render_template('index.html', trends=None, error="Failed to fetch IP address.")

        trends = login_and_fetch_X_trends(twitter_username, twitter_password)
        print("The trends are : ",trends)
        # trends = ["Trendx1","Trendx2","Trendx3","Trendx4","Trendx5"]

        if trends:
            object_id = save_to_mongodb(trends, ip_address)
            return render_template('index.html', trends=trends,object_id=object_id,ip_address=ip_address)
        else:
            return render_template('index.html', trends=None)
    except Exception as e:
        return render_template('index.html', trends=None, error=str(e))



