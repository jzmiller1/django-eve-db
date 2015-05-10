import sqlite3
con = sqlite3.connect('sqlite-latest.sqlite')
con.text_factory = str
cursor = con.cursor()

# SOMETIMES THERE ARE WEIRD -1 VALUES IN CCP'S DUMP
# I DON'T HAVE TIME TO TRY TO UNDERSTAND WHY
# BUT THIS MAKES THE LOADER RUN
cursor.execute("""INSERT INTO invTypes (typeID, groupID, typeName, description)
                  VALUES (?, ?, ?, ?);""",
               (-1, -1, 'DUMMY', 'DUMMY TYPE'))
cursor.execute("""INSERT INTO invCategories (categoryID, categoryName, description, published)
                  VALUES (?, ?, ?, ?);""",
               (-1, 'DUMMY', 'DUMMY CATEGORY', False,))
cursor.execute("""INSERT INTO invGroups (groupID, groupName, categoryID, description, published)
                  VALUES (?, ?, ?, ?, ?);""",
               (-1, 'DUMMY', -1, 'DUMMY GROUP', False,))

# # Missing Factions?
cursor.execute("""INSERT INTO chrFactions (factionID, factionName, description, stationCount, stationSystemCount, raceIDs)
                  VALUES (?, ?, ?, ?, ?, ?);""",
               (500021, "DUMMY", "DUMMY FACTION", 0, 0, 0))
cursor.execute("""INSERT INTO chrFactions (factionID, factionName, description, stationCount, stationSystemCount, raceIDs)
                  VALUES (?, ?, ?, ?, ?, ?);""",
               (500024, "DUMMY", "DUMMY FACTION", 0, 0, 0))

# Missing Types in industryMaterials?
cursor.execute("""INSERT INTO invTypes (typeID, typeName, description)
                  VALUES (?, ?, ?);""",
               (34189, 'DUMMY', 'DUMMY TYPE'))
cursor.execute("""INSERT INTO invTypes (typeID, typeName, description)
                  VALUES (?, ?, ?);""",
               (3924, 'DUMMY', 'DUMMY TYPE'))
cursor.execute("""INSERT INTO invTypes (typeID, typeName, description)
                  VALUES (?, ?, ?);""",
               (34188, 'DUMMY', 'DUMMY TYPE'))
con.commit()
