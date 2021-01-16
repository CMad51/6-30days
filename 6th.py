tpl=()

my_siss=('hannan','annan')
my_bros=('abud','mamud')

my_siblings=my_siss+my_bros

print('I have',str(len(my_siblings)),'siblings')

my_parents=['Rez','Sha']

lst_my_siblings=list(my_siblings)

lst_my_family=my_parents+lst_my_siblings

my_family_members=tuple(lst_my_family)

print("These are my family's members:",my_family_members)

mom_and_siss=my_family_members[1:4]
print(mom_and_siss)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if "Estonia" in nordic_countries:
 print('Estonia is a nordic country!')
else:
 print("Estonia isn't a nordic country!!")

if 'Iceland' in  nordic_countries :
 print('Iceland is a nordic country!')

