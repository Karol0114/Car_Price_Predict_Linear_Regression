import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Dataset z którego korzystam w projekcie pochodzi ze strony kaggle.com
### link: https://www.kaggle.com/datasets/hellbuoy/car-price-prediction



# Wczytuję dataset
df = pd.read_csv('cena_samochodow_regresja\CarPrice_Assignment.csv')


### Podstawowa analiza, wszystkich kolumn w dataset: 

##Jak typ paliwa ma wpływ na średnią cenę samochodu?
print(df['fueltype'].value_counts())

gas_price_mean = df[df['fueltype'] == 'gas']['price'].mean()
diesel_price_mean = df[df['fueltype'] == 'diesel']['price'].mean()

#Wizualizacja na wykresie:
fuel_types = ['Gas', 'Diesel']
mean_prices_fuel = [gas_price_mean, diesel_price_mean]

plt.bar(fuel_types, mean_prices_fuel)
plt.xlabel('Typ paliwa')
plt.ylabel('Średnia cena')
plt.title('Średnia cena dla różnych typów paliwa')
plt.show()
#Średnio cena samochodu z diselem jest większa niż z gazem


## Jak liczba drzwi wpływa średnio na cene samochodu?

print(df['doornumber'].value_counts())

four_doors_mean_price = df[df['doornumber'] == 'four']['price'].mean()
two_doors_mean_price = df[df['doornumber'] == 'two']['price'].mean()

#Wizualizacja na wykresie:
doors_types = ['Czterodrzwiowe', 'Dwudrzwiowe']
mean_prices_doors = [four_doors_mean_price, two_doors_mean_price]

plt.bar(doors_types, mean_prices_doors)
plt.xlabel('Ilość drzwi')
plt.ylabel('Średnia cena')
plt.title('Średnia cena dla różnych ilości drzwi w samochodzie:')
plt.show()
#Średnio droższe są samochody z 4 drzwiami


## Jak rodzaj nadwozia wpływa średnio na cenę samochodu?

print(df['carbody'].value_counts())

sedan_mean_price = df[df['carbody'] == 'sedan']['price'].mean()
hatchback_mean_price = df[df['carbody'] == 'hatchback']['price'].mean()
wagon_mean_price = df[df['carbody'] == 'wagon']['price'].mean()
hardtop_mean_price = df[df['carbody'] == 'hardtop']['price'].mean()
convertible_mean_price = df[df['carbody'] == 'convertible']['price'].mean()

#Wizualizacja na wykresie:
carbody_types = ['Sedan', 'Hatchback', 'Wagon', 'Hardtop', 'Convertible']
mean_prices_carbody = [sedan_mean_price, hatchback_mean_price, wagon_mean_price 
                       , hardtop_mean_price, convertible_mean_price ]

plt.bar(carbody_types, mean_prices_carbody)
plt.xlabel('Typ nadwodzia')
plt.ylabel('Średnia cena')
plt.title('Średnia cena dla poszczególnych rodzaji nadwozia')
plt.show()
#Średnie ceny od najdroższych do najtańszych: hardtop -> convertible -> sedan -> wagon -> hatchback


## Jak napęd wpływa na cenę samochodu?

print(df['drivewheel'].value_counts())

drivewheel_fwd_mean_price = df[df['drivewheel'] == 'fwd']['price'].mean()
drivewheel_rwd_mean_price = df[df['drivewheel'] == 'rwd']['price'].mean()
drivewheel_4wd_mean_price = df[df['drivewheel'] == '4wd']['price'].mean()

#Wizualizacja na wykresie:
drivewheel_types = ['fwd', 'rwd', '4wd']
mean_prices_doors = [drivewheel_fwd_mean_price, drivewheel_rwd_mean_price, drivewheel_4wd_mean_price]

plt.bar(drivewheel_types, mean_prices_doors)
plt.xlabel('Rodzaj napedu')
plt.ylabel('Średnia cena')
plt.title('Średnia cena dla różnych napędów w samochodzie:')
plt.show()
#Średnie ceny napedu od najdroższego: rwd -> 4wd -> fwd


## Jak liczba koni mechanicznych wpływa na średnią cene samochodu?

#print(df['horsepower'].value_counts())

small_amount_of_horsepower_mean_price = df[df['horsepower'] < 100]['price'].mean()
medium_amount_of_horsepower_mean_price = df[(df['horsepower'] >= 100) & (df['horsepower'] < 120)]['price'].mean()
large_amount_of_horsepower_mean_price = df[df['horsepower'] >= 120]['price'].mean()

#Wizualizacja na wykresie:
horsepower_types = ['< 100', '>= 100 i < 120', '>= 120']
mean_prices_horseower = [small_amount_of_horsepower_mean_price, medium_amount_of_horsepower_mean_price
                         , large_amount_of_horsepower_mean_price]

plt.bar(horsepower_types, mean_prices_horseower)
plt.xlabel('Ilośc koni')
plt.ylabel('Średnia cena')
plt.title('Średnia cena dla różnych ilości koni mechanicznych:')
plt.show()
# ZDECYDOWANIE najdroższe są samochody z mocą 120+, następnie z drugiego przedziału a najtańsze 
#są z moca mniejszą niż 100.


##  Jak highwaympg wpływa na średnią cene samochodu 
##(im większe highwaympg to samochód jest bardziej paliwoszczędny po za miastem)

#print(df['highwaympg'].value_counts())

smaller_highwaympg_mean_price = df[(df['highwaympg'] >= 25) & (df['highwaympg'] < 35)]['price'].mean()
bigger_highwatmpg_mean_price = df[(df['highwaympg'] >= 35) & (df['highwaympg'] < 54)]['price'].mean()

#Wizualizacja na wykresie:
highwaympg_types = ['>= 25 i < 35', '>= 35 i < 54']
mean_prices_highwaympg = [smaller_highwaympg_mean_price, bigger_highwatmpg_mean_price]

plt.bar(highwaympg_types, mean_prices_highwaympg)
plt.xlabel('Ilość highwaympg')
plt.ylabel('Średnia cena')
plt.title('Średnia cena dla różnych ilości highwaympg:')
plt.show()
#Droższe są samochody z mniejszym hwmpg, natomiast jest ich zdecydowanie więcej


## Jak citympg wpływa na średnią cenę samochodu 
##(im wiekszy citympg to samochód jest bardziej paliwoszczędny w mieście)

#print(df['citympg'].value_counts())

print(df[(df['citympg'] >= 14) & (df['citympg'] <= 30)]['price'].mean()) 
print(df[(df['citympg'] > 30) & (df['citympg'] < 50)]['price'].mean()) 

#tak sama sytuacja jak w hwmpg 

## Skoro duży wpływ na cene ma ilosc koni mechanicznych to sprawdzmy dla obydwu przedziałów 
##średnią ilosc koni:

print('Średnia ilość koni:')

print(df[(df['citympg'] >= 14) & (df['citympg'] <= 30)]['horsepower'].mean())
print(df[(df['citympg'] > 30) & (df['citympg'] < 50)]['horsepower'].mean()) 

## Drugi przedział posiada średnio mniej koni mechanicznych o prawie 50, co wydaje mi się, 
## że może przyczyniać się do tego, dlaczego bardziej paliwoszczedne w miescie samochody są tańsze



## Jaki peakrpm ma wpływ na średnią cenę samochodu;
##(peakrpm - najwyższa liczba obrotow na minutę/ maksymalne obroty, przy ktorych silnik;
##osiaga swoja najwieksza moc);

#print(df['peakrpm'].value_counts())

print(df[(df['peakrpm'] >= 4150) & (df['peakrpm'] < 5500)]['price'].mean())
print(df[(df['peakrpm'] >= 5500) & (df['peakrpm'] < 6600)]['price'].mean()) 

#Ceny samochodów są porównywalne, średnia dla pierwzego przedzialu to 13.5 tyś.;
#natomiast dla drugiego 12.7 tyś.;

print('Średnia ilosc koni mechanicznych dla przedziałów peakrpm')
print(df[(df['peakrpm'] >= 4150) & (df['peakrpm'] < 5500)]['horsepower'].mean())
print(df[(df['peakrpm'] >= 5500) & (df['peakrpm'] < 6600)]['horsepower'].mean()) 

#porównywalna ilość koni, sprawdzmy dla 'enginesize', który ma wpływ na cene

print('Średnia pojemnosc silnika dla przedziałów peakrpm')
print(df[(df['peakrpm'] >= 4150) & (df['peakrpm'] < 5500)]['enginesize'].mean())
print(df[(df['peakrpm'] >= 5500) & (df['peakrpm'] < 6600)]['enginesize'].mean()) 

## pierwszy przedział ma wiekszą pojemność silnika, a jego cena jest również wyższa, 
#więc prawdopodobnie na cene wpływa wlasnie pojemnosc silnika.


## Jaki wpływ ma compressionratio na średnią cenę samochodu? (współczynnik kompresji)

#print(df['compressionratio'].value_counts())

print(df[(df['compressionratio'] >= 7) & (df['compressionratio'] <= 9)]['price'].mean())
print(df[(df['compressionratio'] > 9) & (df['compressionratio'] < 23)]['price'].mean())

# Ceny są porównywalne, droższe są samochody z pierwszego przedziału o 1 tyś.


## Jaki stroke(skok tłoka) ma wpływ na średnią cenę samochodu?

#print(df['stroke'].value_counts())

print(df[(df['stroke'] >= 2.07) & (df['stroke'] < 3.400)]['price'].mean())
print(df[(df['stroke'] >= 3.400) & (df['stroke'] < 4.170)]['price'].mean())

# Cena samochodów z niższym stroke jest wyższa o 800.


## Czy boreratio ma wpływ na średnią cenę samochodu?

#print(df['boreratio'].value_counts())

smaller_boreratio_mean_price = df[(df['boreratio'] >= 2.54) & (df['boreratio'] <= 3.15)]['price'].mean()
bigger_boreratio_mean_price = df[(df['boreratio'] > 3.15) & (df['boreratio'] <= 3.94)]['price'].mean()

#Wizualizacja na wykresie:
boreratio_types = ['>= 2.54 i <= 3.15', '> 3.15 i <= 3.94']
mean_prices_boreratio = [smaller_boreratio_mean_price, bigger_boreratio_mean_price]

plt.bar(boreratio_types, mean_prices_boreratio)
plt.xlabel('Ilość boreratio')
plt.ylabel('Średnia cena')
plt.title('Średnia cena dla różnych ilości boreratio:')
plt.show()
# ZDECYDOWANIE droższe są samochody z większym boreratio


## Jaki wpływ ma  fuelsystem na średnią cenę samochodu?
#print(df['fuelsystem'].value_counts())

fuelsystem_mpfi_mean_price = df[df['fuelsystem'] == 'mpfi']['price'].mean()
fuelsystem_2bbl_mean_price = df[df['fuelsystem'] == '2bbl']['price'].mean()
fuelsystem_idi_mean_price = df[df['fuelsystem'] == 'idi']['price'].mean()
fuelsystem_1bbl_mean_price = df[df['fuelsystem'] == '1bbl']['price'].mean()
fuelsystem_spdi_mean_price = df[df['fuelsystem'] == 'spdi']['price'].mean()
fuelsystem_4bbl_mean_price = df[df['fuelsystem'] == '4bbl']['price'].mean()
fuelsystem_mfi_mean_price = df[df['fuelsystem'] == 'mfi']['price'].mean()
fuelsystem_spfi_mean_price = df[df['fuelsystem'] == 'spfi']['price'].mean()

#Wizualizacja na wykresie:
fuelsystem_types = ['mpfi', '2bbl', 'idi', '1bbl', 'spdi', '4bbl', 'mfi', 'spfi']
mean_prices_fuelsystem = [fuelsystem_mpfi_mean_price, fuelsystem_2bbl_mean_price, fuelsystem_idi_mean_price
                          ,fuelsystem_1bbl_mean_price, fuelsystem_spdi_mean_price,  fuelsystem_4bbl_mean_price
                          ,fuelsystem_mfi_mean_price, fuelsystem_spfi_mean_price]

plt.bar(fuelsystem_types, mean_prices_fuelsystem)
plt.xlabel('Rodzaje paliwa')
plt.ylabel('Średnia cena')
plt.title('Średnia cena dla różnych rodzaji paliw:')
plt.show()


## Jak rozmair silnika wpływa na cenę samochodu?

#print(df['enginesize'].value_counts())

least_enginesize_mean_price = df[df['enginesize'] <= 114]['price'].mean()

medium_enginesize_mean_price = df[(df['enginesize'] > 114) & (df['enginesize'] <= 167)]['price'].mean()

largest_enginesize_mean_price = df[df['enginesize'] > 167]['price'].mean()

#Wizualizacja na wykresie:
enginesize_types = ['najmniejsze rozmiary', 'średnie rozmiary', 'największe rozmiary']
mean_prices_enginesize = [least_enginesize_mean_price, medium_enginesize_mean_price
                          , largest_enginesize_mean_price]

plt.bar(enginesize_types, mean_prices_enginesize)
plt.xlabel('Rozmiary silnika')
plt.ylabel('Średnia cena')
plt.title('Średnia cena dla różnych rozmiarów silnika w samochodzie:')
plt.show()
#Rozmiar silnika ma ZDECYDOWANIE wpływ na cene samochodu, 
#im wieksza pjemnosć tym zdecydowanie większa cena


## Jak liczba cylindrów (cilindernumber) wpływa na średnią cenę samochodu?

#print(df['cylindernumber'].value_counts())
cylindernumber_two_mean_price = df[df['cylindernumber'] == 'two']['price'].mean()
cylindernumber_three_mean_price = df[df['cylindernumber'] == 'three']['price'].mean()
cylindernumber_four_mean_price = df[df['cylindernumber'] == 'four']['price'].mean()
cylindernumber_five_mean_price = df[df['cylindernumber'] == 'five']['price'].mean()
cylindernumber_six_mean_price = df[df['cylindernumber'] == 'six']['price'].mean()
cylindernumber_eight_mean_price = df[df['cylindernumber'] == 'eight']['price'].mean()
cylindernumber_twelve_mean_price = df[df['cylindernumber'] == 'twelve']['price'].mean()

# Wizualizacja na wykresie:
cylindernumber_types = ['two', 'three', 'four', 'five', 'six', 'eight', 'twelve']
mean_price_cylindernumbers = [cylindernumber_two_mean_price, cylindernumber_three_mean_price
                              , cylindernumber_four_mean_price, cylindernumber_five_mean_price
                             , cylindernumber_six_mean_price, cylindernumber_eight_mean_price
                              , cylindernumber_twelve_mean_price]

plt.bar(cylindernumber_types, mean_price_cylindernumbers)
plt.xlabel('Liczba cylindrów')
plt.ylabel('Średnia cena')
plt.title('Średnia cena dla danej ilości cylindrów: ')
plt.show()


## Jaki wpływ na średnią cenę samochodu ma typ silnika?

print(df['enginetype'].value_counts())

print(df.groupby("enginetype")['price'].mean())
enginetype_dohc_mean_price = df[df['enginetype'] == 'dohc']['price'].mean()
enginetype_dohcv_mean_price = df[df['enginetype'] == 'dohcv']['price'].mean()
enginetype_l_mean_price = df[df['enginetype'] == 'l']['price'].mean()
enginetype_ohc_mean_price = df[df['enginetype'] == 'ohc']['price'].mean()
enginetype_ohcf_mean_price = df[df['enginetype'] == 'ohcf']['price'].mean()
enginetype_ohcv_mean_price = df[df['enginetype'] == 'ohcv']['price'].mean()
enginetype_rotor_mean_price = df[df['enginetype'] == 'rotor']['price'].mean()

#Wizualizacja na wykresie:
enginetype_types = ['dohc', 'dohcv', 'l', 'ohc', 'ohcf', 'ohcv', 'rotor']
mean_prices_enginetype = [enginetype_dohc_mean_price, enginetype_dohcv_mean_price
                          , enginetype_l_mean_price, enginetype_ohc_mean_price
                          , enginetype_ohcf_mean_price, enginetype_ohcv_mean_price
                          , enginetype_rotor_mean_price]

plt.bar(enginetype_types, mean_prices_enginetype)
plt.xlabel('Rodzaje silnika')
plt.ylabel('Średnia cena')
plt.title('Średnia cena dla różnych rodzaji silnika w samochodzie:')
plt.show()


## Jak wielkość samochodu wpływa średnio na cenę?

#print(df['carheight'].value_counts())

#print(df.groupby('carheight')['price'].mean())

print(df[df['carheight'] < 52]['price'].mean())

print(df[(df['carheight'] >= 52) & (df['carheight'] < 56)]['price'].mean())

print(df[df['carheight'] >= 56]['price'].mean())

#Największe samochody z ostatniego przedziału są droższe od poprzedników, 
#natomiast pierwszy przedział jest droższy od drugiego, do przeanalizowania!.

## Sprawdzę co wpływa na to, że cena drugiego przedziału jest mniejsza od pierwszego
print('średnia ilość koni mechanicznych dla wysokości samochodów:')

print(df[df['carheight'] < 52]['horsepower'].mean()) # --> 117 koni

print(df[(df['carheight'] >= 52) & (df['carheight'] < 56)]['horsepower'].mean()) # --> 96 koni

print(df[df['carheight'] >= 56]['horsepower'].mean()) # --> 114 koni

print('średnia pojemnosc silnika dla wysokosci samochodów: ')
print(df[df['carheight'] < 52]['enginesize'].mean()) # --> 126 koni

print(df[(df['carheight'] >= 52) & (df['carheight'] < 56)]['enginesize'].mean()) # --> 122

print(df[df['carheight'] >= 56]['enginesize'].mean()) # --> 142 

# Samochody z drugiego przedziału mają średnio mniejszą liczbę koni mechanicznych oraz 
#mniejszą pojemność silnika
# Dlatego ich cena jest mniejsza od samochodów z pierwszego przedziału


## Jak waga samochodu wpływa na jego średnią cenę?

#print(df['curbweight'].value_counts())

print(df[df['curbweight'] < 2261.40]['price'].mean())

print(df[(df['curbweight'] >= 2261.40) & (df['curbweight'] < 3034.80)]['price'].mean())

print(df[df['curbweight'] >= 3034.80]['price'].mean())

# Z analizy tej wynika, że waga pojazdu ma zdecydowanie wpływ na jego średnią cene.


## Jak szerokość ma wpływ na średnią cenę samochodu?

#print(df['carwidth'].value_counts())

print(df[df['carwidth'] < 64]['price'].mean())

print(df[(df['carwidth'] >= 64) & (df['carwidth'] <= 67)]['price'].mean())

print(df[df['carwidth'] > 67]['price'].mean())

# Szerokość samochodu ma wpływ na jego średnią cenę 


## Jak długość wpływa na średnią cenę samochodu?

print(df[df['carlength'] < 167]['price'].mean())

print(df[(df['carlength'] >= 167) & (df['carlength'] < 181)]['price'].mean())

print(df[df['carlength'] >= 181]['price'].mean())

# Długość samochodu również ma wpływ na jego średnią cenę


##Czy rozstaw osi ma wpływ na cene samochodu?

print(df[df['wheelbase'] < 96]['price'].mean())

print(df[(df['wheelbase'] >= 96) & (df['wheelbase'] < 103)]['price'].mean())

print(df[df['wheelbase'] <= 103]['price'].mean())

# najtańsze są samochody z pierwszego przedziału, natomiast najdroższe są samochody z drugiego
# przedziału


## Jak położenie silnika w samochodzie ma wpływ na jego cene?

#print(df['enginelocation'].value_counts())

print(df.groupby('enginelocation')['price'].mean())

enginelocation_front_mean_price = df[df['enginelocation'] == 'front']['price'].mean()
enginelocation_rear_mean_price = df[df['enginelocation'] == 'rear']['price'].mean()

#Wizualizacja na wykresie:
enginelocation_types = ['przedni napęd', 'tylni napęd']
mean_prices_enginelocation = [enginelocation_front_mean_price, enginelocation_rear_mean_price]

plt.bar(enginelocation_types, mean_prices_enginelocation)
plt.xlabel('Rodzaje położenia silnika')
plt.ylabel('Średnia cena')
plt.title('Średnia cena dla poszczególnego rozmieszczenia silnika: ')
plt.show()
# Samochody z tylnim napędem są ZDECYDOWANIE droższe od tych z przednim, natomiast są ich 
#3 sztuki, należy przenalizować jakie samochody są w tylnim napędzie.

print('sprawdzamy srednią pojemnosc silnika oraz srednie konie mechaniczne dla sanmochodów z tylnim napędem')
print(df[df['enginelocation'] == 'rear']['enginesize'].mean())
print(df[df['enginelocation'] == 'rear']['horsepower'].mean())
# zdecydowanie, obydwie cechy należą do najwyższych prezedziałów, 
#dlatego tylni napęd jest ZDECYDOWANIE droższy


## Jak aspiration ma wpływ na średnią cenę samochodu?

print(df.groupby('aspiration')['price'].mean())

aspiration_std_mean_price = df[df['aspiration'] == 'std']['price'].mean()
aspiration_turbo_mean_price = df[df['aspiration'] == 'turbo']['price'].mean()

#Wizualizacja na wykresie:
aspiration_types = ['std', 'turbo']
mean_prices_aspirations = [aspiration_std_mean_price, aspiration_turbo_mean_price]

plt.bar(aspiration_types, mean_prices_aspirations)
plt.xlabel('Rodzaje aspiration')
plt.ylabel('Średnia cena')
plt.title('Średnia cena dla poszczególnego rodzaju aspiration: ')
plt.show()
# Samochodów z turbo jest mniej ale średnia cena jest wieksza od std.

##Analiza dlaczego turbo jest droższe od std
print('porównujemy średnią ilość koni mechanicznych w autach std vs turbo')

print(df[df['aspiration'] == 'std']['horsepower'].mean())
print(df[df['aspiration'] == 'turbo']['horsepower'].mean())

print('porównujemy średnią pojemność silnika w autach std vs turbo')

print(df[df['aspiration'] == 'std']['enginesize'].mean())
print(df[df['aspiration'] == 'turbo']['enginesize'].mean())
# Obydwie kluczowe cechy są większe dla turbo, stąd ich wyższa cena.


## Jak symboling ma wpływ na cene samochodu? --> Symboling to ocena ryzyka 
#ubepieczeniowego samochodu. Jest to wartośc przypisana przez agencje ubezpieczeniową, która
#określa względne ryzyko ubepieczeniowe związane z danym modelem samochodu 
#skala w naszym przypadku jest od -2 do 3, gdzie -2 to wysoki stan ryzyka a 3 to niski stan ryzyka


print(df['symboling'].value_counts())

print(df.groupby('symboling')['price'].mean())

# z analizy wychodzi na to, że najdroższe są te z niskim stanem ryzyka i 
#jest to logiczne, natomiast reszta już tego nie prezentuje, do przeanalizowania.

print('zobaczmy średnią ilosc koni dla poszczególnych symboli')

print(df.groupby('symboling')['horsepower'].mean())

# patrząc na średnią ilość koni dla poszególnych 'grup', można powiedzieć, że to one miały wpływ 
#na ich średnią cenę


### Zmiana danych typu 'object' na dane numeryczne, aby móc utworzyć model uczenia maszynowego

df.info()

#Zmiana fueltype z object na: gas -> 1, diesel -> 0
def fueltype_swap(sample):
    if sample == 'gas':
        return 1
    else:
        return 0
df['fueltype'] = df['fueltype'].apply(fueltype_swap)

#zmiana aspiration z object na: std -> 1, turbo -> 0
def aspiration_swap(sample):
    if sample == 'std':
        return 1
    else:
        return 0
df['aspiration'] = df['aspiration'].apply(aspiration_swap)

#zmiana doornumber z object na: four -> 1, two -> 0
def doornumber_swap(sample):
    if sample == 'four':
        return 1
    else:
        return 0
df['doornumber'] = df['doornumber'].apply(doornumber_swap)  

#zmiana enginelocation z object na: front -> 1, rear -> 0
def enginelocation_swap(sample):
    if sample == 'front':
        return 1
    else:
        return 0
df['enginelocation'] = df['enginelocation'].apply(enginelocation_swap)

## Dla cech, które posiadają więcej zmiennych niż jeden zastosuję metodę One Hot Encoding

# One Hot Encoding dla kolumny carbody (5 zmiennych jest w kolumnie)
df = pd.get_dummies(df, columns=['carbody'])

# One hot Encoding dla kolumny drivewheel (3 zmienne w kolumnie)
df = pd.get_dummies(df, columns=['drivewheel'])

# One Hot Encoding dla kolumny enginetype (7 zmiennych w kolumnie)
df= pd.get_dummies(df, columns=['enginetype'])

# One hot Encoding dla kolumny fuelsystem (8 zmiennych w kolumnie)
df = pd.get_dummies(df, columns = ['fuelsystem'])

#One Hot Encoding dla kolumny cylindernumber (7 zmiennych w kolumnie)
df = pd.get_dummies(df, columns= ['cylindernumber'])

df.info()

## ostatni 'object', kóry pozostał w DataFrame jest CarName, ta cecha nie przyda się w modelu, więc ją
#usuwam

#Tworzę kopię df, na której będę teraz działać:
df_copy = df.copy()

#Usuwam CarName:
df_copy = df_copy.drop(columns =['CarName'])

# Sprawdzam czy wszystkie kolumny sa numeryczne i nie posiadają braków w danych:
df_copy.isna().sum()
df_copy.info()


# Tworze histogram, aby zobaczyć jak rozłozone są wartości kolumny 'price'

df_copy['price'].hist(bins = 20)
plt.title('Prices histogram')
plt.xlabel('price')
plt.ylabel('number of prices')

# Wyszedł rozkład prawoskośny, przywróce go do rozkładu normalnego aby pozbyć się wartości odstających


# Przywracam kolumne 'price' do postaci normalnej, za pomocą jej zlogarytmowania
df_copy['prices_log'] = np.log(df['price'])

# Zobaczmy rozkład po zlogarytmowaniu
df_copy['prices_log'].hist(bins = 20)
plt.title('prices_log histogram')
plt.xlabel('charges_log')
plt.ylabel('number of charges_log')


# Zapisuję sobie kolumne price, ale chce ją usunąć, ponieważ mam ją w wersji zlogarytmowanej, na której będę pracować. 

price_before_log = df_copy['price']

df_copy = df_copy.drop(columns = ['price'])

