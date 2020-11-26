from aiohttp import web
import json, urllib.request

async def handle(request):

  # default value
  backendServiceData = {"name": "failed to call backend service :("}
  try:
    data = urllib.request.urlopen("http://host.docker.internal:5858").read()
    # data = urllib.request.urlopen("http://localhost:5858").read()
    backendServiceData = json.loads(data)
  except:
    print("failed to call backend service :(");

  be_service_payload_decorated = '';
  for key in backendServiceData:
    value = backendServiceData[key]
    be_service_payload_decorated += '<li>' + value + '</li>';

  # styles
  styles = """
  <style>
  * {
    font-family: Roboto, HelveticaNeue-Light, "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 19px;
  }
  </style>
  """

  # body
  body = """
  <body>
  <h1>List of names (static)</h1>
  <ul>
    <li>Brian</li>
    <li>Hanna</li>
    <li>Bob</li>
    <li>Knut</li>
    <li>Jane</li>
  </ul>
  <h1>List of names (fetched from BE service)</h1>
  <ul id="be-fetch">
    {be_service_payload_decorated}
  </ul>
  </body>
  """
  body = body.format(be_service_payload_decorated = be_service_payload_decorated);

  # html
  html = "{styles} {body}".format(styles=styles, body=body)

  return web.Response(text=html, content_type='text/html')

app = web.Application()
app.router.add_get('/', handle)

web.run_app(app, port=5859)
