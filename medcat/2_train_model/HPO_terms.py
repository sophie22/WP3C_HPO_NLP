import os

with open("HCM_DCM_HPO_terms.txt", "r") as f:
    unprocessed_terms = f.readline()
    unprocessed_term_list = unprocessed_terms.split("), ")
    term_list = [
        {"term": term.split(" (")[0].strip(), "code": term.split(" (")[1]}
        for term in unprocessed_term_list
    ]
    print(term_list)


with open("HPO_terms_Ronny.txt") as f:
    unprocessed_terms = f.readline()

    print(unprocessed_terms)
    