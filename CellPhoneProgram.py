import CellPhoneClass as p

def main():

    phone = p.CellPhone("Apple", "iPhone 15", 1099)

    print(phone.get_manufact() + "\n" + phone.get_model() + "\n" + "$" + format(phone.get_retail_price(),',.2f'))

    phone.set_retail_price(999)

    print(phone.get_manufact() + "\n" + phone.get_model() + "\n" + "$" + format(phone.get_retail_price(),',.2f'))

main()