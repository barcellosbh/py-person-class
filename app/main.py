class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_dicts: list) -> list:
    Person.people = {}

    instances = []
    for p_dict in people_dicts:
        new_person = Person(p_dict["name"], p_dict["age"])
        instances.append(new_person)

    for p_dict in people_dicts:
        current_person = Person.people[p_dict["name"]]

        for key in ["wife", "husband"]:
            if key in p_dict and p_dict[key] is not None:
                spouse_name = p_dict[key]
                spouse_instance = Person.people[spouse_name]
                setattr(current_person, key, spouse_instance)

    return instances
