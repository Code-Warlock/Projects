"""Working with dates and time """
from datetime import date,time,datetime,timedelta
status = input("Sign Up or Login : ").lower()
if "login" in status or "logged" in status:
    dob = input("Enter your date of birth : (dd/mm/yyyy) : ")
    dob = dob.split("/")
    dob = list(map(int,dob))
    real = datetime.today()
    day,month,year = dob
    ref_date = datetime(year,month,day)
    date_joined = input("Enter your date of recruitment : (dd/mm/yyyy) : ")
    date_joined = date_joined.split("/")
    date_joined = list(map(int,date_joined))
    j_day,j_month,j_year = date_joined
    date_joined = datetime(j_year,j_month,j_day)
    days_between = date_joined - ref_date
    age = (days_between.days) // 365
    today_age = (real - ref_date).days // 365
    global age_as_at_joined
    age_as_at_joined = (date_joined - ref_date).days // 365
else:
    dob = input("Enter your date of birth : (dd/mm/yyyy) : ")
    dob = dob.split("/")
    dob = list(map(int,dob))
    real = datetime.today()
    day,month,year = dob
    ref_date = datetime(year,month,day)
    date_joined = datetime.today()
    days_between = date_joined - ref_date
    age = (days_between.days) // 365
    age_as_at_joined = age
    today_age = (real - ref_date).days // 365
if age > 25:
    _years = 60-age
    _days = _years * 365
    retire = date_joined + timedelta(days=_days)
elif age <= 25:
    _years = 35
    _days = _years * 365
    retire = date_joined + timedelta(days=_days)
print(f"""================================User Profile=================================
Date Joined       ===> {date_joined:%A,%B,%Y}
Date of Birth    ===>  {ref_date:%d,%A ,%B,%Y}
Age              ===>  {today_age}years
Age Joined => {age_as_at_joined}years
Date due to Retire ==> {retire:%A,%B,%Y}
""")
# present = time(12,34,45)
# print(present)
