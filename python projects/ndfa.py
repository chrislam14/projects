# Submitter: cslam2(Lam, Christopher)
# Partner  : ayresm(Ayres, Matthew)
# We certify that we worked cooperatively on this programming
#    assignment, according to the rules for pair programming

import goody

awsr = {'end': {}, 'start': {'1': {'start'}, '0': {'start', 'near'}}, 'near': {'1': {'end'}}}

def read_ndfa(file : open) -> {str:{str:{str}}}:
    newdict = {}
    for line in file:
        newdict2 = {}
        if ';' in line:
            key = line[:line.find(';')]
            line = line.rstrip()[line.find(';')+1:].split(';')
            for n in range(0,len(line)-1,2):
                newdict2.setdefault(line[n],set()).add(line[n+1])
                newdict[key] = newdict2
        else:
            newdict[line.rstrip()] = {}
    return newdict

def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    return ''.join(sorted(['  ' + (str(s) + ' transitions: ' +  str(sorted([(n,sorted(m)) for n,m in ndfa[s].items()]))+ '\n') for s in ndfa]))

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    resultlist = [state]
    ss = [state]
    for i in inputs:
        res = set()
        for s in ss:
            if len(ndfa[s]) != 0 and i in ndfa[s]:
                for x in ndfa[s][i]:
                    res.add(x)
        result = (i,res)
        resultlist.append(result)
        if len(res) == 0:
            break
        ss = res
    return resultlist


def interpret(result : [None]) -> str:
    resultstr = 'Start state = ' + result[0]+'\n'
    for f in result[1:]:
        resultstr = resultstr + '  Input = ' + f[0] + '; new possible states = ' + str(sorted(list(f[1]))) + '\n'
    return resultstr + 'Stop state(s) = ' + str(sorted(list(f[1]))) + '\n'




if __name__ == '__main__':
    # Write script here
    filename = input('Enter the file name describing this Non-Deterministic Finite Automaton: ')
    fa = read_ndfa(open(filename))
    print("\nThe Description of the file entered for this Non-Deterministic Finite Automaton")
    print(ndfa_as_str(fa))
    filename = input('Enter the file name describing the sequence of start-states and all their inputs: ')
    print()
    for line in open(filename):
        starts = line [:line.find(';')]
        inputlist = line[line.find(';')+1:].split(';')
        print('Start tracing this NDFA in its start-state\n'+ interpret(process(fa, line [:line.find(';')], line[line.find(';')+1:].rstrip().split(';'))))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
