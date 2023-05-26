import soundex


def main():

    """
    Demonstration of the Soundex module, creating lists of name pairs
    and running them through the soundex method before printing results.
    """

    print("-----------------")
    print("| codedrome.com |")
    print("| Soundex       |")
    print("-----------------\n")

    names1 = ["Johnson", "Adams", "Davis", "Simons", "Richards", "Taylor", "Carter", "Stevenson", "Taylor", "Smith", "McDonald", "Harris", "Sim", "Williams", "Baker", "Wells", "Fraser", "Jones", "Wilks", "Hunt", "Sanders", "Parsons", "Robson", "Harker"]

    names2 = ["Jonson", "Addams", "Davies", "Simmons", "Richardson", "Tailor", "Chater", "Stephenson", "Naylor", "Smythe", "MacDonald", "Harrys", "Sym", "Wilson", "Barker", "Wills", "Frazer", "Johns", "Wilkinson", "Hunter", "Saunders", "Pearson", "Robertson", "Parker"]

    namecount = len(names1)
    

    for i in range(0, len(names1)):

        s1 = soundex.Soundex(names1[i])
        s2 = soundex.Soundex(names2[i])

        print("{:20s}{:4s}  {:20s}{:4s}".format(names1[i], s1, names2[i], s2))


main() 