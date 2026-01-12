def get_human_age(cat_age: int, dog_age: int) -> list[int]:

    def convert_cat(age: int) -> int:
        if age == 0:
            return 0
        elif age <= 15:
            return 1
        elif age <= 24:  # 15+9
            return 2
        else:
            return 2 + (age - 24) // 4 + (1 if (age - 24) % 4 else 0)

    def convert_dog(age: int) -> int:
        if age == 0:
            return 0
        elif age <= 15:
            return 1
        elif age <= 24:
            return 2
        else:
            return 2 + (age - 24) // 5 + (1 if (age - 24) % 5 else 0)

    return [convert_cat(cat_age), convert_dog(dog_age)]
