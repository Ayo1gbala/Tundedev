name = input("what's his name? ")


match name:
    case "Alade":
        print("Babalawo")
    case "Bayo":
        print("Christian")
    case "Baba_Ada":
        print("ise'se")
    case "Kay":
        print("ifa olokun")
    case "Mobimpe":
        print("Zion")
    case "Demilade" | "IBK" | "Shodex":
        print("Woli_Dare")
    case _:
        print("kini oruko e? ")



