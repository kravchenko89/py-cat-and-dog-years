def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    def convert(age: int,
                first_thresh: int,
                second_thresh: int,
                step: int) -> int:
        if age < first_thresh:
            return 0
        human = 1
        remaining = age - first_thresh
        if remaining > second_thresh:
            human += 1
            remaining -= second_thresh
            human += remaining // step
        elif remaining > 0:
            human += 0
        return human

    cat_human = convert(cat_age, 15, 9, 4)
    dog_human = convert(dog_age, 15, 9, 5)
    return [cat_human, dog_human]
