student = 'Mateusz'
stypendium = 950
assert type(stypendium) in (int,float) and stypendium>0, "Stypendium musi być dodatnią liczbą"
wydatki = 920
assert type(wydatki) in (int,float) and wydatki>=0, "Wydatki muszą być liczbą dodatnią"
print('Student: {}'.format(student.upper()))
print('stypendium: {} zł'.format(stypendium))
print('Wydatki: {} zł'.format(wydatki))
print('Oszczędności: {} zł'.format(stypendium-wydatki))