import yaml

yaml_path = "../data/data.yaml"
with open(yaml_path, "r", encoding="utf-8") as f:
    info = yaml.load(f, Loader=yaml.FullLoader)
    for i in info:
        print(info[i])