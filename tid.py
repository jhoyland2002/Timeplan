import pathlib

def datoforskjell():
    import datetime
    import os
    old_date=None
    path= pathlib.Path(__file__).parent / 'tider.txt'
    try:
        with open(path, "r") as f:
                if os.stat(path).st_size != 0:
                    old_date = datetime.datetime.fromisoformat(f.read())
    except:
        pass

    x = datetime.datetime.now()
    if old_date==None or x-old_date>datetime.timedelta(days=1):
        with open(path, "w") as f:
            f.write(x.isoformat())
            return True
    return False
if __name__=="__main__":
    datoforskjell()
