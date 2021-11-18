calisma_saati = int(input('Haftalik Calisma saatini giriniz'))
saatlik_ucret = int(input('Haftalik  saat ucreti giriniz'))

if calisma_saati <= 40:
 print('haftalik kazanciniz ', (calisma_saati * saatlik_ucret))
else:
  print('haftalik kazanciniz ', (40* saatlik_ucret)+((calisma_saati-40)*saatlik_ucret*1.5))


print('BYE')
 
