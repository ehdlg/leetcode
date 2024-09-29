def two_sum(numbers: list[int], target: int):
    hashmap = dict()

    for i, number in enumerate(len(numbers)):
        diff = target - number
        map_value = hashmap.get(diff, None)

        if map_value is not None:
            return [i, map_value]

        hashmap.update({diff: i})

    return []
