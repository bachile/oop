import InsectClass as i

def main():

    mosquito = i.Insect()
    housefly = i.Insect()

    mosquito.flight_length()
    housefly.flight_length()

    print('The mosquito traveled:', mosquito.get_distance(), 'miles')
    print('The housefly traveled:', housefly.get_distance(), 'miles')

main()