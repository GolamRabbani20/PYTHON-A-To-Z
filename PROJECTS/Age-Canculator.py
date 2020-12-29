def AgeCalculator(day,month,year,day2,month2,year2):
    d3=0
    m3=0
    y3=0

    if day2<day and month2<month:
        d3=day2+30-day
        month2-=1
        m3=month2+12-month
        year2-=1
        if year2>year:
            y3=year2-year
        return y3,m3,d3

    elif day2 < day:
        d3 = day2+30 - day
        month2 -= 1
        if month2<month:
            m3=month2+12-month
            year2-=1
            if year2>year:
                y3=year2-year
        else:
            m3=month2-month
            y3=year2-year
        return y3,m3,d3

    elif month2 < month:
        d3=day2-day
        m3 = month2+12 - month
        year2 -= 1
        if year2>year:
            y3=year2-year
        else:
            y3=0
        return y3,m3,d3

    else:
        d3=day2-day
        m3=month2-month
        y3=year2-year
    return y3,m3,d3

day,month,year=input("Enter your date of birth:").strip().split()
day,month,year=[int(day),int(month),int(year)]

day2,month2,year2=input("Age at the Date of:").strip().split()
day2,month2,year2=[int(day2),int(month2),int(year2)]

print("%d Years %d Month %d days"%(AgeCalculator(day,month,year,day2,month2,year2)))


