# logical operators
"""
and -> both conditions must be true 
or -> at leats onecondition must be true
not -> reverses the truth value
"""

has_gatepass = True
has_scholl_id = False
has_national_id = True

# if has_gatepass or has_scholl_id:
#     print('Access school services')

if not has_scholl_id:
    print('Welcome to school')
# elif has_gatepass and has_national_id:
#     print('Permitted to enter school gates')