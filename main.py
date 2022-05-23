from junk_haul import JunkHauler

task_index = int(input('Enter the appropriate job index: '))

pu_mileage = float(input('How many miles to pickup?'))
rt_mileage = float(input('How far is the round trip?'))
dh_mileage = float(input('How far from the dump to home?'))

num_loads = int(input('How many loads?'))

miles_driven = (pu_mileage + (rt_mileage * (num_loads - 0.5)) + dh_mileage)

load_charge = int(input('How much would you like to charge per load?'))

labor_charge = input('Are you hiring labor?')
total_labor = 0

if labor_charge.lower() == 'yes':
    total_labor = 20
else:
    pass

junk = JunkHauler(job_index = task_index, mileage = miles_driven, loads = num_loads, load_fee = load_charge, labor_fee = total_labor )
junk.calculate()