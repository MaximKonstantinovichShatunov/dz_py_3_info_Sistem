import json

def open_file():
    with open("data.json", encoding="UTF-8") as file_in:
            records = json.load(file_in)
    return records

def rec_file(id,key ,values):
    with open("data.json", encoding="UTF-8") as file_in:
        records = json.load(file_in)

    records[id-1][key] = values
    
    with open("data.json", "w", encoding="UTF-8") as file_out:
        json.dump(records, file_out, ensure_ascii=False, indent=2)

