import requests
import datetime

USERNAME = "lalalala"
TOKEN = "lululululu"

pixela_endpoint = "https://pixe.la/v1/users"

uer_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}


# responce = requests.post(url = pixela_endpoint, json= uer_params)
# print(responce.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : "graph1",
    "name" : "Being sad",
    "unit" : "hours",
    "type" : "float",
    "color" : "sora"
}

header = {
    "X-USER-TOKEN" : TOKEN
}
g_id = "graph1"

# responce_graph = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(responce_graph.text)

today = datetime.datetime.now()


pixel_config = {
    "date" : today.strftime("%y%m%d"),
    "quantity" : "5"
}

graph_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{g_id}"

# responce_pixel = requests.post(url= graph_pixel,json=pixel_config,headers=header )
# print(responce_pixel.text)

graph_config_update = {
    "unit" : "depression",
    "color" : "ajisai"
}

graph_pixel_update = f"{pixela_endpoint}/{USERNAME}/graphs/{g_id}"

update_pixel = requests.put(url=graph_pixel_update,json=graph_config_update,headers=header)
print(update_pixel.text)