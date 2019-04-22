#Authors: Anthony Introne
#         Michael Klein

# Combines all subtopic into one text file
def ManyToOne(data_source, subtop1, subtop2, subtop3, subtop4, subtop5):
    with open("../../part1/data/" + data_source + "/" + data_source + ".txt","w") as data_file:
        with open("../../part1/data/"  + data_source + "/" + subtop1 + "_data_clean.txt","r") as esports:
            esports_data = esports.readlines()
            for data in esports_data:
                data_file.write(data)
            esports.close()
        with open("../../part1/data/"  + data_source + "/"  + subtop2 + "_data_clean.txt","r") as nba:
            nba_data = nba.readlines()
            for data in nba_data:
                data_file.write(data)
            nba.close()
        with open("../../part1/data/" + data_source + "/"  + subtop3 + "_data_clean.txt","r") as ncaam:
            ncaam_data = ncaam.readlines()
            for data in ncaam_data:
                data_file.write(data)
            ncaam.close()
        with open("../../part1/data/" + data_source + "/"  + subtop4 + "_data_clean.txt","r") as nfl:
            nfl_data = nfl.readlines()
            for data in nfl_data:
                data_file.write(data)
            nfl.close()
        with open("../../part1/data/" + data_source + "/"  + subtop5 +  "_data_clean.txt","r") as nhl:
            nhl_data = nhl.readlines()
            for data in nhl_data:
                data_file.write(data)
            nhl.close()
    data_file.close()
    print("Many Files To One File For " + data_source + " Finished")

ManyToOne("NYT", "esports", "nba", "ncaam", "nfl", "nhl")
ManyToOne("Twitter", "esports", "nba", "ncaa", "nfl", "nhl")

def MTOCommonCrawl():
    with open("../../part1/data/CommonCrawl/cc.txt","w") as data_file:
        with open("../../part1/data/CommonCrawl/ccESPORTS_data_clean.txt","r") as esports:
            esports_data = esports.readlines()
            for data in esports_data:
                data_file.write(data)
            esports.close()
        with open("../../part1/data/CommonCrawl/ccNBA_data_clean.txt","r") as nba:
            nba_data = nba.readlines()
            for data in nba_data:
                data_file.write(data)
            nba.close()
        with open("../../part1/data/CommonCrawl/ccNCAA_data_clean.txt","r") as ncaam:
            ncaam_data = ncaam.readlines()
            for data in ncaam_data:
                data_file.write(data)
            ncaam.close()
        with open("../../part1/data/CommonCrawl/ccNFL_data_clean.txt","r") as nfl:
            nfl_data = nfl.readlines()
            for data in nfl_data:
                data_file.write(data)
            nfl.close()
        with open("../../part1/data/CommonCrawl/ccNHL_data_clean.txt","r") as nhl:
            nhl_data = nhl.readlines()
            for data in nhl_data:
                data_file.write(data)
            nhl.close()
    data_file.close()
    print("Many Files To One File CC Finished")

MTOCommonCrawl()