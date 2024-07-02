import rivalry as rv
import thunderpick as tp
import team
import fuzzy as fuzz
import numpy as np
import sqlite3


def update_html():
    """
    simply update html of both rv and tp

    input : none
    output: none
    """
    # check if html exists delete elsewise
    import os

    if os.path.exists("rivalry.html"):
        os.remove("rivalry.html")
        print("successfully removed rv")

    if os.path.exists("thunderpick.html"):
        os.remove("thunderpick.html")
        print("successfully removed tp")

    rv.update_rivalry_html()
    print("successfully updated rv")
    tp.update_tp_html()
    print("successfully updated tp")


# parse html
def parse_html():
    """
    parse thru html of rv and tp

    input: none
    output: dict (rv), dict (tp)
    """
    import os

    if not os.path.exists("rivalry.html") or not os.path.exists("thunderpick.html"):
        print("html not available, exiting")
        exit()

    rv_dict = rv.parse_rivalry()
    tp_dict = tp.parse_thunderpick()

    return rv_dict, tp_dict


# update html
# update_html()


def flip_bits(binary_string):
    # Ensure the input is a valid binary string
    if not set(binary_string).issubset({"0", "1"}):
        raise ValueError("Input must be a binary string containing only '0' and '1'")

    # Flip the bits using a list comprehension
    flipped_string = "".join("1" if bit == "0" else "0" for bit in binary_string)
    return flipped_string


def store_into_class(rv_dict, tp_dict):
    """
    store dictionary into classes by matching with fuzzy matching

    input : dict , dict
    output: list of TEAM.py class

    """
    rv_dict, tp_dict = parse_html()

    # get list of dates, get smallest key list
    len_rv = len(rv_dict.keys())
    len_tp = len(tp_dict.keys())

    # use the smallest key list
    if len_rv < len_tp:
        small_dict_key = rv_dict.keys()
    else:
        small_dict_key = tp_dict.keys()

    # what the fuck ???
    viable_matches = []
    # get list of dates
    for i in small_dict_key:
        # get list of rv matches on date
        for j in rv_dict[i]:
            rv_teams = list(j.keys())
            if i in tp_dict:
                tp_teams = tp_dict[i]
                # get list of tp matches on date
                for l in tp_teams:
                    l_key = list(l.keys())

                    # calculate fuzzy match ratios and match teams from rv and tp at the same time
                    ratio1 = fuzz.avg_ratio(rv_teams[0], l_key[0])
                    ratio2 = fuzz.avg_ratio(rv_teams[0], l_key[1])
                    ratio3 = fuzz.avg_ratio(rv_teams[1], l_key[0])
                    ratio4 = fuzz.avg_ratio(rv_teams[1], l_key[1])

                    # get avg ratios and test if they are similar enough
                    ratio_list = [ratio1, ratio2, ratio3, ratio4]
                    index_max = np.argmax(ratio_list)
                    ratio_list.sort()

                    # if match is good pair up tp and rv and store into match
                    if ratio_list[-1] > 70 and ratio_list[-2] > 70:
                        bits = format(index_max, "b").zfill(2)
                        bits_flipped = flip_bits(bits)

                        team_a = team.Team(
                            name=rv_teams[int(bits[0])],
                            odd_rv=j[rv_teams[int(bits[0])]],
                            odd_tp=l[l_key[int(bits[1])]],
                        )
                        team_b = team.Team(
                            name=rv_teams[int(bits_flipped[0])],
                            odd_rv=j[rv_teams[int(bits_flipped[0])]],
                            odd_tp=l[l_key[int(bits_flipped[1])]],
                        )
                        match = team.Match(date=i, team_a=team_a, team_b=team_b)
                        viable_matches.append(match)

    return viable_matches


def setup():
    '''
    setup function
        - update html
        - parse html
        - store into classes
        - store class into sqlite3
    '''
    # update_html()
    rv_dict, tp_dict = parse_html()
    print(store_into_class(rv_dict, tp_dict))
    
setup()

# some TODO maybes : front facing website, operte via docker in aws
