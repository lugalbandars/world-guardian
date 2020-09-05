def worlds_to_json(worlds):
    worlds_json = sorted([world.to_dict() for world in worlds], key=lambda world: world['number'])
    return worlds_json
