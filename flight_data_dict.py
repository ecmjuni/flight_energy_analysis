import pandas as pd

ENERGY_LABEL = {"LOW ENERGY" : "yellow",
                "ON PATH" : "blue",
                "HIGH ENERGY" : "red"}

flight_data_columns = {
                        "DATE" : "object",
                        "TIME" : "object",
                        "LDGL": "object",
                        "LDGR": "object",
                        "FPHASE" : "object",
                        "HEIGHT" : "float64",
                        "ALTSTDC": "float64",
                        "ALTQNH" : "float64",
                        "TAT" : "float64",
                        "CAS" : "float64",
                        "GS" : "float64",
                        "VLS" : "float64",
                        "MACH" : "float64",
                        "HEAD" : "float64",
                        "WINDIR" : "float64",
                        "WINSPD" : "float64",
                        "LATP" : "float64",
                        "LONP" : "float64"
                        }

flight_data_columns_final = {
                        "DATE" : "object",
                        "TIME" : "object",
                        "LDGL": "object",
                        "LDGR": "object",
                        "FPHASE" : "object",
                        "HEIGHT" : "float64",
                        "ALTSTDC": "float64",
                        "ALTQNH" : "float64",
                        "TAT" : "float64",
                        "CAS" : "float64",
                        "GS" : "float64",
                        "VLS" : "float64",
                        "MACH" : "float64",
                        "HEAD" : "float64",
                        "WINDIR" : "float64",
                        "WINSPD" : "float64",
                        "LATCORR" : "float64",
                        "LONCORR" : "float64",
                        "LATP" : "float64",
                        "LONP" : "float64",
                        "COLOR" : "object"
                        }