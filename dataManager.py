import json

def get_player_data(id):
    with open("./userData.json", "r") as file:
        data : dict = json.load(file)

    if data.get(str(id)) != None:
        return data[str(id)]
    else:
        data[str(id)] = {}
        return data[str(id)]
    
def update_player_data(id, newData):
    with open("./userData.json", "r") as file:
        data = json.load(file)

    print("Old Data:", data)

    data[str(id)] = newData

    print("New Data:", data)

    with open("./userData.json", "w") as file:
        json.dump(data, file)