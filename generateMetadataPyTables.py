import numpy
import tables
from tables import *

def OBIEEData():
    class Particle(IsDescription):
        objName = StringCol(100)
        objType = StringCol(20)
        objPath = StringCol(500)
        objOwner= StringCol(100)
        objCreated=time64Col()

        
    #print OBIEEMetadata
    h5file = open_file("tutorial1.h5", mode = "w", title = "Test file")
    group = h5file.create_group("/", 'detector', 'Detector information')
    table = h5file.create_table(group, 'readout', Particle, "Readout example")

    print h5file

OBIEEData();
