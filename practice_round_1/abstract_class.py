from abc import ABC, abstractmethod


class PizzaDelivery(ABC):

    def __init__(self, total_pizza_available, pizza_dict):
        self._total_pizza_available = int(total_pizza_available)
        self._pizza_delivery: int = 0
        self._pizza_dict = pizza_dict
        self._result_dict = dict()

    @abstractmethod
    def return_pizza(self, total_n):
        raise NotImplementedError

    @property
    def total_pizza_available(self):
        return self._total_pizza_available

    @total_pizza_available.setter
    def total_pizza_available(self, value):
        self._total_pizza_available = value

    @property
    def pizza_delivery(self):
        return self._pizza_delivery

    @pizza_delivery.setter
    def pizza_delivery(self, value):
        self._pizza_delivery = value

    @property
    def pizza_dict(self):
        return self._pizza_dict


def file_parser2(file_name):
    with open(file_name, 'r') as f:
        all_file_lines = f.readlines()

    total_pizza = 0
    two_member_teams = 0
    three_member_teams = 0
    four_member_teams = 0

    pizza_dict = dict()
    count = 1
    for line in all_file_lines:
        if count == 1:
            (
                total_pizza, 
                two_member_teams, 
                three_member_teams, 
                four_member_teams
            ) = line.split()

        else:
            pizza_dict[f"{count - 1}"] = set(line.split()[1:])
        count += 1

    return pizza_dict, two_member_teams, three_member_teams, four_member_teams, total_pizza


def file_parser(file_name):
    with open(file_name, 'r') as f:
        all_file_lines = f.readlines()

    total_pizza = 0
    two_member_teams = 0
    three_member_teams = 0
    four_member_teams = 0

    pizza_dict = dict()
    count = 1

    for line in all_file_lines:
        if count == 1:
            total_pizza, two_member_teams, three_member_teams, four_member_teams = line.split()
            pizza_dict = {key: set() for key in range(int(total_pizza)) if key != 0}

        else:
            num_ingredients = int(line.split()[0].strip())
            pizza_dict[count - 1] = [num_ingredients, set(line.split()[1:]), 1]
        count += 1

    return pizza_dict, two_member_teams, three_member_teams, four_member_teams, total_pizza


def get_score(data):
    score = sum([values[0] ** 2 for dicky in data for key, values in dicky.items()])
    return score



def get_pizza_delivery_data(obj, people):
    data = []
    for number in people:
        if obj.total_pizza_available >= number:
            obj.pizza_delivery += 1
            obj.total_pizza_available -= number
            dict_pizza_list = obj.return_pizza(number)
            data.append(dict_pizza_list)
        else:
            print(f"{obj.total_pizza_available} and {number}")
    return data


def write_output(obj, data, output_file):
    with open(output_file, 'w') as f:
        f.write(f"{obj.pizza_delivery} \n")
        for i in range(obj.pizza_delivery):
            dictty = data[i]
            key = list(dictty.keys())[0]
            output_idx = ' '.join(str(i) for i in dictty[key][1])
            f.write(f"{key} {output_idx} \n")
