import yaml


def analyze(data_name, keyword):
    with open("./data/" + data_name + ".yml", "r", encoding='utf-8') as f:
        all_data = yaml.load(f)
        script_data = all_data[keyword]
        # print(script_data)
        # print("----------------")
        data_list = list()
        for i in script_data.values():
            data_list.append(i)
            # return阻断代码
        return data_list
# print(analyze("contact_data","test_add_contact"))