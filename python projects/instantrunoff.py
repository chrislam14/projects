# Submitter: cslam2(Lam, Christopher)
# Partner  : ayresm(Ayres, Matthew)
# We certify that we worked cooperatively on this programming
#    assignment, according to the rules for pair programming

import goody


def read_voter_preferences(file : open) -> {list}:
    vote_dict = {}
    for line in file:
        line = line.rstrip().split(';')
        vote_dict[line[0]] = line[1:]
    return vote_dict

def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    strresult = ''
    for v in sorted(d, key = key, reverse = reverse):
        strresult = strresult + '  ' + v + " -> " + (str(d[v]) + '\n')
    return strresult

def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    vcdict = {c: 0 for c in cie}
    if cie == {}:
        return
    for v in sorted(vp):
        for c in vp[v]:
            if c in cie:
                vcdict[c] += 1
                break
    return vcdict

def remaining_candidates(vd : {str:int}) -> {str}:
    vlist = list(sorted(vd.values()))
    return {c for c in vd if vd[c] != vlist[0]}


def run_election(vp_file : open) -> {str}:
    vpdict = read_voter_preferences(vp_file)
    cset = {c for clist in vpdict.values() for c in clist}
    ballot_count = 1
    while len(cset) > 1:
        vcdict = evaluate_ballot(vpdict, cset)
        print('Vote count on ballot #'+str(ballot_count)+': candidates (sorted alphabetically) using candidates in only set '+ str(cset))
        print(dict_as_str(vcdict))
        print('Vote count on ballot #'+str(ballot_count)+': candidates (sorted numerically) using candidates in only set '+ str(cset))   
        print(dict_as_str(vcdict, key = (lambda t: (-vcdict[t],t))))
        cset = remaining_candidates(vcdict)
        ballot_count += 1
    return (cset)

  
  
  
  
    
if __name__ == '__main__':
    # Write script here
    def script():
        try:
            go = input('Enter the file name describing all the voter preferences: ')
            if go == "quit":
                return
            print('\nPreferences: voter -> [candidates in order]')
            print(dict_as_str(read_voter_preferences(open(go))))
            winner = run_election(open(go))
            if len(winner) == 0:
                print("Tie among final candidates: cannot choose one unique winner.")
            else:
                print("Election winner is "+ str(winner))
        except:
            print('File not found try again')
        return 
    script()
     
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
