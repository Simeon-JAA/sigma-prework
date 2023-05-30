from datetime import date

def get_today_date():
  today_date = date.today()
  return today_date
def get_user_dob():
  user_dob = input('Please enter your date of birth (year-month-day): ')
  return user_dob

#--top function
def calculate_age():
  today_date = get_today_date()
  today_date_list = str(today_date).split('-')
  user_dob = get_user_dob()
  user_dob_list = user_dob.split('-')

  year = int(today_date_list[0]) - int(user_dob_list[0])
  month = int(today_date_list[1]) - int(user_dob_list[1])
  day = int(today_date_list[2]) - int(user_dob_list[2])

  if year > 0 and month > 0:
    return year
  elif year > 0 and month == 0 and day > 0:
    return year
  elif year > 0 and month ==  0 and day == 0:
    return (f'You turn {year} today')
  elif year > 0 and month == 0 and day < 0:
    return year - 1
  elif year > 0 and month < 0:
    return year - 1
  else:
    return 0
  

print(calculate_age())