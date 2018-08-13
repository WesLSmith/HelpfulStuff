import pandas as pd
import numpy as np
import numexpr as ne
import timeit

setup = """import pandas as pd;import numpy as np;import numexpr as ne;import timeit;data = pd.DataFrame({"vals":["ABC","DEF","ZYX"]*10000}, index = range(30000))"""


###Specifying S3 etc. is faster than S32, specify min number of characters possible
timeit.Timer("""test = np.array(data["vals"].values, dtype = 'S3');ne.evaluate("where(test == b'ABC', True,False)")""", setup = setup).repeat(10,1000)

timeit.Timer("""data[data["vals"] == 'ABC']""",setup = setup).repeat(10,1000)
