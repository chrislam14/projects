# Submitter: cslam2(Lam, Christopher)
# Partner  : ayresm(Ayres, Matthew)
# We certify that we worked cooperatively on this programming
#    assignment, according to the rules for pair programming

import goody


def read_fa(file : open) -> {str:{str:str}}:
    newdict = {}
    for line in file:
        key = line[:line.find(';')]
        line = line.rstrip()[line.find(';')+1:].split(';')
        newdict[key] = {line[n]: line[n+1] for n in [n for n in range(0,len(line)-1,2)]}
    return newdict


def fa_as_str(fa : {str:{str:str}}) -> str:
    return ''.join(sorted(['  ' + (str(s) + ' transitions: ' +  str(sorted(list(fa[s].items())))+ '\n') for s in fa]))
    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    resultlist = [state]
    s = state
    for i in inputs:
        if i not in fa[s]:
            resultlist.append((i, None))
        else:
            s = fa[s][i]
            resultlist.append((i,s))
    return resultlist

def interpret(fa_result : [None]) -> str:
    resultstr = 'Start state = ' + fa_result[0]+'\n'
    for f in fa_result[1:]:
        newstate = f[1]
        if newstate == None:
            newstate = 'illegal input: simulation terminated'
        else:
            newstate = 'new state = ' + f[1]
        resultstr = resultstr + '  Input = ' + f[0] + '; ' + newstate + '\n'
    return resultstr + "Stop state = " + str(f[1]) + '\n'



if __name__ == '__main__':
    # Write script here
    filename = input('Enter the file name describing this Finite Automaton: ')
    fa = read_fa(open(filename))
    print("\nThe Description of the file entered for this Finite Automaton")
    print(fa_as_str(fa))
    filename = input('Enter the file name describing the sequence of start-states and all their inputs: ')
    print()
    for line in open(filename):
        starts = line [:line.find(';')]
        inputlist = line[line.find(';')+1:].split(';')
        print('Start tracing this FA in its start-state\n'+ interpret(process(fa, line [:line.find(';')], line[line.find(';')+1:].rstrip().split(';'))))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
