def main():
    time = input("What time is it? ")
    day = convert(time)

    if 6.0 <= day <= 7.0 and time.endswith("p.m.") or 18.0 <= day <= 19.0:
        print("dinner time")
    elif 7.0 <= day <= 8.0 and not time.endswith("p.m."):
        print("breakfast time")
    elif 12.0 <= day <= 13.0 and not time.endswith("a.m."):
        print("lunch time")
    
 
def convert(time):
    if time.endswith("a.m."):
        ntime = time.rstrip("a.m.")
        x, y = ntime.split(":")
    elif time.endswith("p.m."):
        rtime = time.rstrip("p.m.")
        x, y = rtime.split(":")
    else:
        x, y = time.split(":")
    
    h = float(x)
    m = float(y)
    total = h + (m / 60)
    return(float(f"{total:.1f}"))
    

if __name__ == "__main__":
    main()