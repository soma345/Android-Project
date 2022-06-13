def expQuery (vectorMod,query):
    term1, term2, val1, val2 = '', '', 0, 0
    for term in vectorMod:
        if term not in query and vectorMod[term] > 0:
            weight = vectorMod[term]
            if weight > val1:
                term1, val1, term2, val2 = term, weight, term1, val1
            elif weight > val2:
                term2, val2 = term, weight
            else:
                pass
    if term1:query =  query+" "+(term1)
    if term2: query = query+" "+(term2)   
    return query