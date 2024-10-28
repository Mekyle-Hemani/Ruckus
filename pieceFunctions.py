def inversenotation(notation):
    if len(notation) == 2:
        notationsplit = list(notation)
        if notationsplit[1] == "'":
            return notationsplit[0]
        elif notationsplit[1] == "2":
            return notation
    else:
        return notation+"'"