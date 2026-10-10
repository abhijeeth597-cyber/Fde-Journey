import json
def Load_json(path):
    with open(path) as f:
        data = json.load(f)
    return data
def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
if __name__ == "__main__":
    people = [{"name": "Asha", "score": 88}]
    save_json("out.json", people)
    print(Load_json("out.json"))