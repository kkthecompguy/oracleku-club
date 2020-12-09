import os
from django.conf import settings
from .models import Event


BASE_DIR = settings.BASE_DIR
templates_dir = os.path.join(BASE_DIR, 'templates')
filename = os.path.join(templates_dir, 'email.html')

event = Event.objects.last()

welcome_html_str = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA_Compartible" content="IE edge">
  <title>Kenyatta University Oracle Club</title>
</head>
<body style="max-width: 1140px; margin: auto; overflow-x: hidden;">
  <div style="display: flex; justify-content: center; align-items: center;">
    <img src="https://oracleku-club.herokuapp.com/static/images/ku-oracle-logo.png" alt="Ku Club logo" style="width: 5rem; height: 5rem; object-fit: cover;">
  </div>
  <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; padding: 3rem;">
    <h1>Welcome To Kenyatta University Oracle Club</h1>
    <p>To help get you started on your new exciting journey, we’re hosting free online events or at times physical events to help you and guide you on your development career</p>
    <a href="https://oracleku-club.herokuapp.com" style="text-decoration: none; border: 1px solid #ccc; border-radius: 5px; color: dimgray; padding: 1rem; background-color: whitesmoke;">View Site</a>
  </div>
  <div style="display: flex; justify-content: center; align-items: center; padding: 1rem;">
    <div style="width: 400px; height: 300px;">
      <img src="https://oracleku-club.herokuapp.com/media/images/2020/07/31/programmers_13.jpeg" alt="" style="width: 100%; height: 100%; object-fit: cover;">
    </div>
  </div>
  <div>
    <h3 style="text-align: center; font-size: 2rem; margin: 0; margin-top: 2rem;">Events you might be intereted in</h3>
    <div>
      <div style="display: flex; justify-content: center;align-items: center; flex-direction: column; padding: 3rem;">
        <div>
          <img src="{image_url}" alt="Image" style="width: 200px; height: 200px;">
        </div>
        <div style="text-align: center; ">
          <p>{overview}</p>
        </div>
        <a href="https://oracleku-club.herokuapp.com/events" style="text-decoration: none; border: 1px solid #ccc; border-radius: 5px; color: dimgray; padding: 1rem; background-color: whitesmoke;">View All</a>
      </div>
    </div>
  </div>
  <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; text-align: center; padding: 2rem; background: #ccc;">
    <blockquote>“We’re so excited to have you start your journey here with us.
      I hope this club teaches you everything you need to know and more!”</blockquote>
    <img src="/media/images/2020/07/31/IMG_0612.jpg" alt="" style="width: 5rem; height: 5rem; border-radius: 50%;">
    <p>
      John Burghman (Club President)
    </p>
  </div>
  <div style="display: flex; align-items: center; justify-content: center; flex-direction: column; padding: 1rem;">
    <div style="padding: 1rem; display: flex; justify-content: center; align-items: center; flex-direction: column;">
      <span>You are receiving this email because you are part of the Kenyatta University Oracle Club</span>
      <span style="margin: 20px;">43844-00100 KENYATTA UNIVERSITY NAIROBI</span>
      <span><a href="#!">Unsubscribe</a></span>
    </div>
  </div>
</body>
</html>"""


def welcome_template(html_context=welcome_html_str, event=event):
  html_str = html_context.format(image_url=event.thumbnail.url, overview=event.overview)
  return html_str
