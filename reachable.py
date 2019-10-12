# Submitter: cslam2(Lam, Christopher)
# Partner  : ayresm(Ayres, Matthew)
# We certify that we worked cooperatively on this programming
#    assignment, according to the rules for pair programming

import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    gdict = {}
    for line in file:
        key, value = line.rstrip().split(';')
        if key not in gdict: gdict[key] = set()
        gdict[key].add(value)
    return gdict 


def graph_as_str(graph : {str:{str}}) -> str:
    strresult = ''
    for node in sorted(graph):
        strresult = strresult + '  ' + node + " -> " + str(sorted(list(graph[node]))) + '\n'
    return strresult

def reachable(graph : {str:{str}}, start : str, trace : bool = False) -> {str}:
    if graph.get(start) == None:
        return
    reachedset = set()
    exploringlist = [start]
    while len(exploringlist) != 0:
        if trace:
            print()
            print('reached set    =',reachedset)
            print('exploring list =',exploringlist)
            print('removing node', exploringlist[0], 'from the exploring list; adding it to reached list')
        if graph.get(exploringlist[0]) != None:
            exploringlist.extend([n for n in graph[exploringlist[0]] if exploringlist[0] not in reachedset])
        reachedset.add(exploringlist[0])
        if trace:
            print('after adding all nodes reachable directly from', exploringlist[0], 'but not already in reached,exploring =', exploringlist[1:], '\n')
        exploringlist.pop(0)
    return reachedset


if __name__ == '__main__':
    # Write script here
    def script():
        try:
            go = input('Enter the file name describing this graph: ')
            if go == "quit":
                return
            grph = read_graph(open(go))
            print()
            print('Graph: a node -> [showing all its destination nodes]')
            print(graph_as_str(grph))
            while 1 == 1: 
                go = input('Enter the starting node (or enter quit): ')
                if go.lower() == 'quit':
                    return
                elif go not in grph: 
                    print("  Entry Error: '" + str(go) + "'; Illegal: not a source node\n  Please enter a legal String\n")
                else:
                    tracer = input("Enter whether to trace this algorithm[True]: ")
                    if tracer.lower() == 'true':
                        tracer = True
                    elif tracer.lower() == 'false':
                        tracer = False 
                    reached = reachable(grph, go, tracer)
                    print('From node', go, "its reachable nodes:", reached, '\n')    
        except:
            print('File not found try again')
        return 
    script()
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
