from EngineParameters import *
from Optimization.ContourCode import runContourCode

def main():
    #run contour optimization
    runContourCode()

    #save to design folder
    from Geometry.Contour import uploadToDesigns
    uploadToDesigns()


if __name__ == "__main__":
    main()