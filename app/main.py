def get_human_age(cat_age: int, dog_age: int) -> list[int]:
    cat_human = 0
    if cat_age > 15:
        cat_human += 1
        remaining = cat_age - 15
        if remaining > 9:
            cat_human += 1
            remaining -= 9
            cat_human += remaining // 4
        else:
            cat_human += 0
    elif cat_age == 15:
        cat_human = 1
    else:
        cat_human = 0

    # Dog conversion
    dog_human = 0
    if dog_age > 15:
        dog_human += 1
        remaining = dog_age - 15
        if remaining > 9:
            dog_human += 1
            remaining -= 9
            dog_human += remaining // 5
        else:
            dog_human += 0
    elif dog_age == 15:
        dog_human = 1
    else:
        dog_human = 0

    return [cat_human, dog_human]
