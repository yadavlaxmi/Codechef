def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    string="".join(l)
    return(string)
print(mutate_string("abracadabra",5,"k"))
# join