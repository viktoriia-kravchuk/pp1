import json
komputer={
    "brand":"HP",
    "model":"desktop",
    "production_year":2017,
    "specification":
    {
        "procesor_model":"Intel Core i5 7th Gen",
        "CPU":"2.5GHz",
        "RAM":"16GB",
        "memory": "500GB SSD"
    },
    "used":False
}
with open("komputer.json","w") as file:
    json.dump(komputer,file,indent=4)
