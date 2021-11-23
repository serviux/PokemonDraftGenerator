class Config: 
        # the following filter which classes of pokemon to use
        # available values:
        #       "legendary", 
        #       "mythical",
        #       "sub_legendary",
        #       "ultra_beast"
        DONT_USE = ["legendary", "mythical","sub_legendary","ultra_beast"]

        # how big the ending pool will be 
        SAMPLE_SIZE = 50


        # file data gets saved too
        OUT_FILE = "Draft.csv"

        # email file will get sent to afterwards
        EMAIL = "example@email.com"

