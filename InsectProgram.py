import InsectClass as i

def main():

    mosquito = i.Insect(2,4,'mosquito')
    housefly = i.Insect(2,4,'housefly')

    mosquito.flight_length()
    housefly.flight_length()

    print('The', mosquito.get_name(), 'traveled:', mosquito.get_distance(), 'miles')
    print('The', housefly.get_name(),'traveled:', housefly.get_distance(), 'miles')

main()