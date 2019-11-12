HAWAIIANALPHA = ['a','e','i','o','u','p','k','h','l','m','n','w',' ','\'']
HAWAIIANCONSTS = ['p','k','l','m','n','w']
VOWELS = ['a','e','i','o','u',]
VALIDVOWELCOMBOS = ['ai','ae','ao','au','ei','eu','iu','oi','ou','ui']
    
def validWord(word:str)->bool:
    ''' returns true if word only uses Hawaiian characters
    and white spaces and apostrophes
    '''
    word = word.lower()
    for c in word:
        if c not in HAWAIIANALPHA:
            return False
    return True

assert (validWord('aloha') == True)
assert (validWord('guava') == False)
assert (validWord('Hawai\'ian Pineapple') == True)

def Wpronunciate(word:str)->str:
    '''returns the Hawaiian pronunciation of w'''
    if word == 'i' or word == 'e':
        return 'v'
    else:
        return 'w'

def VCpronunciate(combo:str)->str:
    '''returns the Hawaiian pronunciation of vowel and w combos'''
    svpron = ['ah','eh','ee','oh','oo']
    Vdict = {'ai':'eye','ae':'eye','ao':'ow',
             'au':'ow','ei':'ay','eu':'eh-oo',
             'iu':'ew','oi':'oy','ou':'ow','ui':'ooey'}
    result = ''
    if combo not in VALIDVOWELCOMBOS:
            for l in combo:
                for v in range(len(VOWELS)):
                    if VOWELS[v] == l:
                        result += svpron[v]+'-' 
    else:
        result = Vdict[combo]+'-'
    return result

def formatstr(word:str)->str:
    '''formats a string by capitalizing each word 
        and removing unnecessary dashes'''
    word = word.replace('- ', ' ')
    word = word.replace('-\'','\'')
    word = word.strip('-')
    word = word.split()
    for w in range(len(word)):
        word[w] = word[w].capitalize()
    word = ' '.join(word)
    return word
def pronunciate(phrase:str)->str:
    '''returns the Hawaiian pronunciation of words'''
    c = 0
    result = ''
    phrase = phrase.lower()
    if phrase[0] == 'w':
            result += 'w'
            c += 1
    while c < len(phrase):
        if phrase[c] in HAWAIIANCONSTS:
            if phrase[c] == "w":
                p1 = Wpronunciate(phrase[c-1])
            else:
                p1 = phrase[c]
            result+= p1
            c += 1
        elif phrase[c] in VOWELS:
            if c == len(phrase)-1:
                vc = phrase[c]
            else:
                vc = phrase[c]+phrase[c+1]
            p2 = VCpronunciate(vc)
            result += p2
            for v in vc:
                if v in VOWELS:
                    c += 1
        else:
            result += phrase[c]
            c += 1

    result = formatstr(result)
    return result

assert(pronunciate('E komo mai') == 'Eh Koh-moh Meye')
assert(pronunciate('humuhumunukunukuapua\'a') == 'Hoo-moo-hoo-moo-noo-koo-noo-koo-ah-poo-ah\'ah')
assert(pronunciate('hoaloha') == 'Hoh-ah-loh-hah')
assert(pronunciate('Mahalo wahine') == 'Mah-hah-loh Wah-hee-neh')
assert(pronunciate('maika\'i mahalo') == 'Meye-kah\'ee Mah-hah-loh')
assert(pronunciate('iwa') == 'Ee-vah')

def createGuide(inputfile:str,outputfile:str)->None:
    '''reads a file and writes the Haiwaiian
    translations to another file'''
    linelist = []
    try:
        infile = open(inputfile, 'r')
        outfile = open(outputfile, 'w')
        for line in infile:
            line = line.strip('\n')
            linelist.append(line)
        for line in linelist:
            p = pronunciate(line)
            outfile.write(p+'\n')
        infile.close()
        outfile.close()
        return
    except:
        print("The file cannot be found or does not exist")     