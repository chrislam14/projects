#Christopher Lam 29545944 and Jane Hagen 91122491. Lab Sec 1. Lab assignment 9.

infile = open('INNcommands.txt', 'r')
outfile = open('INNresults.txt', 'w')

from collections import namedtuple

import datetime

Room = namedtuple('Room', 'num arrival depart guest ticket')

def AnnInn()->None:
    '''base of the Anteater Program'''
    infile = open("INNcommands.txt", 'r')
    outfile = open('INNresults.txt', 'w')
    commands = infile.readlines()
    room_num_list = []
    reservation_list = []
    ticket_count = [""]
    for line in commands:
        lower_line = our_lower(line)
        lower_line = lower_line.split()
        if "anbr" == lower_line[0]:
            num_line = int(return_num(line))
            room_num_list = ANBR(room_num_list,num_line,outfile)
        elif "labr" == lower_line[0]:
            LABR(room_num_list, outfile)
        elif "pntl" == lower_line[0]:
            printline = line[5:]
            PNTL(printline, outfile)
        elif "debr" == lower_line[0]:
            num_line = int(return_num(line))
            room_num_list = DeBR(room_num_list,num_line,outfile)
            reservation_list = del_by_num(num_line, reservation_list, outfile)
        elif "rear" == lower_line[0]:
            line = line.split()
            name = ' '.join(line[4:])
            arrive_date = datetime.datetime.strptime(line[2],"%m/%d/%Y").strftime("%m/%d/%Y")
            depart_date = datetime.datetime.strptime(line[3],"%m/%d/%Y").strftime("%m/%d/%Y")
            reservation = Room(int(line[1]),arrive_date,depart_date,name,len(ticket_count))
            reservation_list = REaR(reservation,outfile,reservation_list,room_num_list,ticket_count) 
        elif "laer" == lower_line[0]:
            LaER(reservation_list, outfile)
        elif "dear" == lower_line[0]:
            num_line = int(return_num(line))
            reservation_list = DEaR(num_line,reservation_list,outfile)
        elif "rbyb" == lower_line[0]:
            num_line = int(return_num(line))
            RBYB(reservation_list,num_line,room_num_list,outfile)
        elif "rbyg" == lower_line[0]:
            line = line.split()
            name = " ".join(line[1:])
            RBYG(reservation_list,name,outfile)
        elif "laar" == lower_line[0]:
            line = line.split()
            date = line[1]
            LAAR(reservation_list,date,outfile)
        elif "lade" == lower_line[0]:
            line = line.split()
            date = line[1]
            LADE(reservation_list,date,outfile)
        elif "lfbr" == lower_line[0]:
            line = line.split()
            date1 = line[1]
            date2 = line[2]
            LFBR(reservation_list,room_num_list,date1,date2,outfile)
        elif "lobr" == lower_line[0]:
            line = line.split()
            date1 = line[1]
            date2 = line[2]
            LOBR(reservation_list,room_num_list,date1,date2,outfile)
    infile.close()
    outfile.close()

#FUNCTIONS

def return_num (string: str) -> str:
    '''removes anything that isnt a number'''
    new_string = ""
    for c in string:
        if c.isdigit():
            new_string += c
        else:
            new_string += ""
    return new_string

assert return_num("1301313131adna1a") == "13013131311"

def our_lower (s:str) -> str:
    '''return the lower case version of string s'''
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    table = str.maketrans (ALPHABET.upper(), ALPHABET)
    return s.translate(table)

assert our_lower("LOUD") == "loud"

#TEXT COMMANDS FUNCTIONS

room103 = Room('103',"10/27/2013","10/29/2013","Paul Stokes", 1)
room102 = Room('102',"03/02/2016","04/04/2017","Stephanie Richardson", 2)
room101 = Room('101',"02/01/2017","02/05/2017","Susan Olson", 3)
test_reservations = [room103, room102]

test_rooms = [101,102,103]

test_outfile = open("testfile.txt", "w")

def ANBR (rooms: "List of num",room_num:int,outfile:"file") -> "List of Room":
    '''adds a room to the list'''
    if room_num in rooms:
        outfile.write(f"Sorry, can't add room {room_num} again; it's already on the list.\n")
    else:
        rooms.append(room_num)
    return rooms

assert ANBR([101,102,103],104,test_outfile) == [101,102,103,104]

def LABR (rooms: "List of num", outfile: "file") -> None:
    '''writes the amount of rooms available and the room numbers
    to the outfile'''
    outfile.write(f"Number of bedrooms in service: {len(rooms)}")
    outfile.write('\n')
    outfile.write("-------------------------------------\n")
    for room in rooms:
        outfile.write(str(room))
        outfile.write('\n')

def PNTL (string: str, outfile: "file") -> None:
    '''writes the string inputed to the outfile'''
    outfile.write(string)

def DeBR (rooms:"List of num", room_num:int, outfile:"file") -> "List of Room":
    '''removes a room from the list'''
    new_list = []
    if room_num not in rooms:
        outfile.write(f"Sorry, can't delete room {room_num}; it is not in service now\n")
    for room in rooms:
        if room_num != room:
            new_list.append(room)
    return new_list

assert DeBR([101,102,103],101,test_outfile) == [102,103]

def del_by_num (room_num:int, res_list: "list of Room", outfile:"file") -> None:
    '''deletes a reservation based off room number'''
    new_list = []
    for res in res_list:
            if int(res.num) != room_num:
                new_list.append(res)
            else:
                outfile.write(f"Deleting room {res.num} forces cancellation of this reservation:\n")
                outfile.write(f"\t {res.guest} arriving {res.arrival} and departing {res.depart} (Conf. #{res.ticket})\n")
    return new_list

def possible_error(reservation:"Room", res_list:"list of Room")->str:
    ''' if there is in an error will return a string with that error'''
    arrival_date1 = datetime.datetime.strptime(reservation.arrival,"%m/%d/%Y")
    depart_date1 = datetime.datetime.strptime(reservation.depart,"%m/%d/%Y")
    for res in res_list:
        arrival_date2 = datetime.datetime.strptime(res.arrival,"%m/%d/%Y")
        depart_date2 = datetime.datetime.strptime(res.depart,"%m/%d/%Y")
        if res.num == reservation.num:
            if arrival_date1 < depart_date2 and depart_date1 > arrival_date2:
                return "booked"
    if arrival_date1 > depart_date1:
        return "leave before arrive"
    elif arrival_date1 == depart_date1:
        return "arrive equals leave"
    else:
        return "no error"

assert possible_error(room101, test_reservations) == "no error"

def REaR (reservation:"Room", outfile: "file", res_list:"list of Room", room_num_list:"list of Room", ticket_count:"list of str") ->  "list of Room":
    '''reserves a room if available'''
    error_message = f"Sorry, can't reserve room {reservation.num} ({reservation.arrival} to {reservation.depart});\n"
    if int(reservation.num) in room_num_list:
        error = possible_error(reservation, res_list)
        if error == "no error":
            res_list.append(reservation)
            outfile.write(f"Reserving room {reservation.num} for {reservation.guest} -- Confirmation #{reservation.ticket}")
            outfile.write("\n")
            outfile.write(f"\t(arriving {reservation.arrival} departing {reservation.depart})\n")
            ticket_count.append('')
        elif error == "booked":
            for res in res_list:
                if res.num == reservation.num:
                    booked_ticket = res.ticket
            outfile.write(error_message)
            outfile.write(f"\t it's already booked (Conf. #{booked_ticket})\n")
        elif error == "leave before arrive":
            outfile.write(error_message)
            outfile.write("\tcan't leave before you arrive.\n")
        elif error == "arrive equals leave":
            outfile.write(error_message)
            outfile.write("\tcan't arrive and leave on the same day.\n")
    else:
        outfile.write(f"Sorry, can't reserve room {reservation.num}; room not in service\n") 
    return res_list

assert REaR(room101,test_outfile,[room102,room103],test_rooms,['']) ==\
       [Room(num='102', arrival='03/02/2016', depart='04/04/2017', guest='Stephanie Richardson', ticket=2),
        Room(num='103', arrival='10/27/2013', depart='10/29/2013', guest='Paul Stokes', ticket=1),
        Room(num='101', arrival="02/01/2017", depart="02/05/2017", guest="Susan Olson", ticket=3)]

def LaER (res_list: "List of Room", outfile: "file")-> None:
    '''prints the reservations'''
    outfile.write(f"Number of reservations: {len(res_list)}\n")
    outfile.write("No. Rm. Arrive      Depart     Guest\n")
    outfile.write("--------------------------------------------\n")
    for res in res_list:
        outfile.write(f'{res.ticket:3d} {res.num} {res.arrival} {res.depart} {res.guest}\n')

def DEaR (confirm_ticket:int, res_list:"list of Room", outfile:"file")->"List of Room":
    ''' deletes a reservation from the list'''
    new_list = []
    count = 0
    for res in res_list:
        if res.ticket != confirm_ticket:
            new_list.append(res)
        count += 1
    #checks if the reservation was removed
    if len(new_list) == count:
        outfile.write(f"Sorry, can't cancel reservation; no confirmation number {confirm_ticket}\n")
    return new_list

assert DEaR(2,[room102,room103],test_outfile) == [Room(num='103', arrival='10/27/2013', depart='10/29/2013', guest='Paul Stokes', ticket=1)]

def RBYB(res_list:"list of Room",room_num:int,room_list:"list of int",outfile:'file')->None:
    '''lists all the reservations for a given bedroom'''
    if room_num in room_list:
        outfile.write(f'Reservations for room {room_num}:\n')
        for res in res_list:
            if int(res.num) == room_num:
                outfile.write(f"\t{res.arrival} to {res.depart}: {res.guest}\n")
    else:
        outfile.write(f'Sorry, {room_num} is not in service\n')

def RBYG(res_list:"list of Room",guest:str,outfile:'file')->None:
    '''lists all the reservations for a given guest'''
    outfile.write(f'Reservations for {guest}:\n')
    for res in res_list:
         if res.guest == guest:
                outfile.write(f"\t{res.arrival} to {res.depart}: room {res.num}\n")

def LAAR(res_list:"list of Room",date:str,outfile:'file')->None:
    '''lists of all reservations for a given arrival date'''
    outfile.write(f'Guests arriving on {date}:\n')
    for res in res_list:
        if res.arrival == date:
            outfile.write(f"\t{res.guest} (room {res.num})\n")

def LADE(res_list:"list of Room",date:str,outfile:'file')->None:
    '''lists of all reservations for a given departure date'''
    outfile.write(f'Guests departing on {date}:\n')
    for res in res_list:
        if res.depart == date:
            outfile.write(f"\t{res.guest} (room {res.num})\n")
            
def LFBR(res_list:"list of Room",room_list:"list of int",date1:str,date2:str,outfile:'file')->None:
    '''lists of all free rooms between two dates'''
    f_rooms = []
    r_rooms = []
    outfile.write(f'Bedrooms free between {date1} to {date2}:\n')
    date1 = datetime.datetime.strptime(date1,"%m/%d/%Y")
    date2 = datetime.datetime.strptime(date2,"%m/%d/%Y")
    for res in res_list:
        date3 = datetime.datetime.strptime(res.arrival,"%m/%d/%Y")
        date4 = datetime.datetime.strptime(res.depart,"%m/%d/%Y")
        if  date3 > date2 or date4 <= date1:
            f_rooms.append(res.num)
        else: 
            r_rooms.append(res.num)
    for room in room_list:
        if room not in r_rooms and room not in f_rooms:
            f_rooms.append(room)
    f_rooms = set(f_rooms)
    r_rooms = set(r_rooms)
    f_rooms = f_rooms - r_rooms
    for room in f_rooms:
        outfile.write(f'\t{room}\n')

def LOBR(res_list:"list of Room",room_list:"list of int",date1:str,date2:str,outfile:'file')->None:
    '''lists of all occupied rooms between two dates'''
    r_rooms = []
    f_rooms = []
    outfile.write(f'Bedrooms occupied between {date1} to {date2}:\n')
    date1 = datetime.datetime.strptime(date1,"%m/%d/%Y")
    date2 = datetime.datetime.strptime(date2,"%m/%d/%Y")
    for res in res_list:                
        date3 = datetime.datetime.strptime(res.arrival,"%m/%d/%Y")
        date4 = datetime.datetime.strptime(res.depart,"%m/%d/%Y")
        if  date3 > date2 or date4 <= date1:
            f_rooms = []
        else: 
            r_rooms.append(res.num)
    r_rooms = set(r_rooms)
    for room in r_rooms:
        outfile.write(f'\t{room}\n')
AnnInn()

