from csv import *
file = open('IRIDIUM.xml',"r" )
csvfile = open('IRIDIUM.xml',"w")
sat_writer = writer(csvfile, delimiter = ",", quotechar = '"' )
record=['']
"""
record=[]
for row in file:
    if "" in row:
        new= row.strip("")
        new1= new[0:new.index("")]
        record.append(new1)
"""
record=[]
for row in file:
    if 'OBJECT_NAME' in row:
        new= row.strip("<OBJECT_NAME>")
        new1= new[0:new.index("</OBJECT_NAME>")]
        record.append(new1)

record=[]
for row in file:
    if "OBJECT_ID" in row:
        new= row.strip("<OBJECT_ID>")
        new1= new[0:new.index("</OBJECT_ID>")]
        record.append(new2)

record=[]
for row in file:
    if "CENTER_NAME" in row:
        new= row.strip("<CENTER_NAME>")
        new1= new[0:new.index("</CENTER_NAME>")]
        record.append(new3)
        print(record)

record=[]
for row in file:
    if "REF_FRAME" in row:
        new= row.strip("<REF_FRAME>")
        new1= new[0:new.index("</REF_FRAME>")]
        record.append(new4)

record=[]
for row in file:
    if "TIME_SYSTEM" in row:
        new= row.strip("<TIME_SYSTEM>")
        new1= new[0:new.index("</TIME_SYSTEM>")]
        record.append(new5)

record=[]
for row in file:
    if "MEAN_ELEMENT_THEORY" in row:
        new= row.strip("<MEAN_ELEMENT_THEORY>")
        new1= new[0:new.index("</MEAN_ELEMENT_THEORY>")]
        record.append(new6)

record=[]
for row in file:
    if "EPOCH" in row:
        new= row.strip("<EPOCH>")
        new1= new[0:new.index("</EPOCH>")]
        record.append(new7)

record=[]
for row in file:
    if "MEAN_MOTION" in row:
        new= row.strip("<MEAN_MOTION>")
        new1= new[0:new.index("</MEAN_MOTION>")]
        record.append(new8)

record=[]
for row in file:
    if "ECCENTRICITY" in row:
        new= row.strip("<ECCENTRICITY>")
        new1= new[0:new.index("</ECCENTRICITY>")]
        record.append(new9)

record=[]
for row in file:
    if "INCLINATION" in row:
        new= row.strip("<INCLINATION>")
        new1= new[0:new.index("</INCLINATION>")]
        record.append(new10)

record=[]
for row in file:
    if "RA_OF_ASC_NODE" in row:
        new= row.strip("<RA_OF_ASC_NODE>")
        new1= new[0:new.index("</RA_OF_ASC_NODE>")]
        record.append(new11)

record=[]
for row in file:
    if "ARG_OF_PERICENTER" in row:
        new= row.strip("<ARG_OF_PERICENTER>")
        new1= new[0:new.index("</ARG_OF_PERICENTER>")]
        record.append(new12)

record=[]
for row in file:
    if "MEAN_ANOMALY" in row:
        new= row.strip("<MEAN_ANOMALY>")
        new1= new[0:new.index("</MEAN_ANOMALY>")]
        record.append(new13)        

record=[]
for row in file:
    if "EPHEMERIS_TYPE" in row:
        new= row.strip("<EPHEMERIS_TYPE>")
        new1= new[0:new.index("</EPHEMERIS_TYPE>")]
        record.append(new14)

record=[]
for row in file:
    if "CLASSIFICATION_TYPE" in row:
        new= row.strip("<CLASSIFICATION_TYPE>")
        new1= new[0:new.index("</CLASSIFICATION_TYPE>")]
        record.append(new15)

record=[]
for row in file:
    if "NORAD_CAT_ID" in row:
        new= row.strip("<NORAD_CAT_ID>")
        new1= new[0:new.index("</NORAD_CAT_ID>")]
        record.append(new16)

record=[]
for row in file:
    if "ELEMENT_SET_NO" in row:
        new= row.strip("<ELEMENT_SET_NO>")
        new1= new[0:new.index("</ELEMENT_SET_NO>")]
        record.append(new17)

record=[]
for row in file:
    if "REV_AT_EPOCH" in row:
        new= row.strip("<REV_AT_EPOCH>")
        new1= new[0:new.index("</REV_AT_EPOCH>")]
        record.append(new18)

record=[]
for row in file:
    if "BSTAR" in row:
        new= row.strip("<BSTAR>")
        new1= new[0:new.index("</BSTAR>")]
        record.append(new19)


record=[]
for row in file:
    if "MEAN_MOTION_DOT" in row:
        new= row.strip("<MEAN_MOTION_DOT>")
        new1= new[0:new.index("</MEAN_MOTION_DOT>")]
        record.append(new20)


record=[]
for row in file:
    if "MEAN_MOTION_DDOT" in row:
        new= row.strip("<MEAN_MOTION_DDOT>")
        new1= new[0:new.index("</MEAN_MOTION_DDOT>")]
        record.append(new21)
        
        if len(record) == 21 :
            sat_writer.writerow(record)
            record = [""]
            
print(record)
      
csvfile.close()
