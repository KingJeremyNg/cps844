import pandas
from csv import reader

# csvData = pandas.read_csv("LeagueofLegends.csv")
# print(csvData.describe())

file = open("LeagueofLegends.arff", "w")
file.write("@RELATION LeagueofLegends\n\n")
file.write("@ATTRIBUTE gamelength numeric\n")
file.write("@ATTRIBUTE gold numeric\n")
file.write("@ATTRIBUTE kills numeric\n")
file.write("@ATTRIBUTE inhibitors numeric\n")
file.write("@ATTRIBUTE towers numeric\n")
file.write("@ATTRIBUTE dragons numeric\n")
file.write("@ATTRIBUTE barons numeric\n")
file.write("@ATTRIBUTE heralds numeric\n")
file.write("@ATTRIBUTE class {'yes','no'}\n")
file.write("@data\n")

# open file in read mode
with open('LeagueofLegends.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    next(csv_reader)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        b_result = "yes" if row[5] == "1" else "no"
        r_result = "yes" if row[6] == "1" else "no"
        gamelength = row[8]

        b_gold = row[10].strip("][").split(", ")[-1]
        b_kills = row[11].count("]") // 2
        b_towers = row[12].count("]") - 1
        b_inhibs = row[13].count("]") - 1
        b_dragons = row[14].count("]") - 1
        b_barons = row[15].count("]") - 1
        b_heralds = row[16].count("]") - 1
        file.write("{},{},{},{},{},{},{},{},{}\n"
                   .format(
                       gamelength, b_gold, b_kills, b_inhibs, b_towers,
                       b_dragons, b_barons, b_heralds, b_result
                   ))

        r_gold = row[17].strip("][").split(", ")[-1]
        r_kills = row[18].count("]") // 2
        r_towers = row[19].count("]") - 1
        r_inhibs = row[20].count("]") - 1
        r_dragons = row[21].count("]") - 1
        r_barons = row[22].count("]") - 1
        r_heralds = row[23].count("]") - 1
        file.write("{},{},{},{},{},{},{},{},{}\n"
                   .format(
                       gamelength, r_gold, r_kills, r_inhibs, r_towers,
                       r_dragons, r_barons, r_heralds, r_result
                   ))

file.close()
