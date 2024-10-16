import requests

USERNAME = "lululululu"
TOKEN = "lalalalala"

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

responce_graph = requests.post(url=graph_endpoint, json=graph_config, headers=header)
print(responce_graph.text)