#install matplotlib in .venv --> python -m pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np

#plot
#plt.plot([1,2,3,4]) #indexes are the X-axe and values are the Y-axe
#plt.ylabel('values') #name on Y-axe
#plt.show() #shows plot

#to explicit plot y-axe too, we can pass 2 arguments (x,y)
plt.plot([1,2,3,4], [1,4,9,16]) #first parameter are the X-axe and second parameter are the Y-axe
plt.ylabel('Y values') #name on Y-axe
plt.xlabel('X values') #name on X-axe
#plt.show() #shows plot

#styling plot
plt.plot([1,2,3,4], [1,4,9,16], 'ro') #third argument is for styling, ro stays for red circles, 'r-' stands for red line. Default is 'b-', so blue line
plt.axis((0,6,0,20)) #to configure the plot area (xmin, xmax, ymin, ymax)
#plt.show()

#plotting numpy arrays
t = np.arange(0.,5.,0.2) #samples time every 0.2s from 0s to 5s (0, 0.2, 0.4 ecc)

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') #we show in the same figure a linear dependency between t and t with red dashes, quadratic with blue square and cubic with green triangles
#plt.axis((0,20,0,20))
#plt.show()

#plotting data (ex. from pandas)
#in plt.plot o plt.scatter possiamo mettere la parola chiave 'data' per accettare un oggetto contenente diverse variabili, accessibili come stringhe (tipo key in dict) e il value sara il plot da visualizzare

data = {
    'a': np.arange(50), #array da 0 a 49
    'c': np.random.randint(0, 50, 50), #50 numeri casuali da 0 a 50
    'd': np.random.randn(50), #array di 50 elementi casuali dalla distribuzione normale (mean 0 standard derivation 1)
}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data) #scatter prints dots in the specified axes (a and b), with colors (c) and size (d)
plt.xlabel('entry a')
plt.ylabel('entry b')
#plt.show()

#plotting with categorical variables (not only numbers)
names = ['group_a', 'grouip_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9,3)) #Nuova figura larga 9 inches e alta 3 inches

plt.subplot(131) #1=numero di righe in figure, 3=numero di colonne in figure, 1=numero di subplot da attivare (da sx a dx), #!DOVREMMO METTERE LE VIRGOLE se cols*rows >=10
plt.bar(names, values) #se un asse ha dei nomi (stringhe) essi vengono viosualizzati in modo equidistante sull'asse stesso
plt.subplot(132) #secondo plot
plt.scatter(names, values)
plt.subplot(133) #quindi abbiamo un plot per colonna e tutti in una sola riga, guardando figsize, notiamo che ogni subplot occupa 3 inches di larghezza (3*3=9) e 3 inches di altezza (unica riga)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()

#controlling line properties
#attributes: there are many attributes,  linewidth, dash style, antialiased, eccc

x = np.arange(5) #passare sempre array numpy ai plot. Su di essi si possono fare anche operazioni come l'elevazione a differenza degli array normali
y = x ** 2

plt.plot(x, y, linewidth=2.0)
#plt.show()

first_line, *other_lines = plt.plot(x, y, '-') #plot returns a list of Line2D objects
first_line.set_antialiased(False) #turn off antialiasing

#setp to set properties to lines returned by plot function 

lines = plt.plot(x, y, [2,4,8,16], [3,9,27,81]) #return 2 lines
plt.setp(lines, color = 'r', linewidth=2.0)
plt.show()

#LINE2D PROPERTIES
#see file line2d_properties

#working with multiple figures and axes

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t) #function of the time

t1 = np.arange(0., 5., 0.1)
t2 = np.arange(0., 5, 0.02)
plt.figure() #create figure
plt.subplot(211) #2 righe, 1 colonna, primo plot (massimo col*row plots)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k') #bo = cerchi blu, k = linea nera --> due linee nella stessa figura sovrapposte

plt.subplot(212) #2 righe, 1 colonna, secondo plot (sotto a quella di prima)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--') #tratteggi rossi
plt.show()

plt.clf() #clear current figures
plt.cla() #clear current axes


#different figures
plt.figure(3)
plt.subplot(211)
plt.plot([1, 2, 3])
plt.subplot(212)
plt.plot([4, 5, 6])

plt.figure(4) #second figure, all the subplots below attend to this second figure
plt.plot([4, 5, 6]) #automatic subplot created

plt.figure(3)
plt.subplot(211)
plt.title('Easy as 1, 2, 3') #title to first subplot of first figure

plt.show()

#working with text

plt.text(60, 0.025, r'$\mu=100, \ \sigma=15$') #!sintassi per scrivere espressioni matematiche
plt.grid(True) #disegna griglia nella figure
t = plt.xlabel('my data', fontsize=14, color='red') #possiamo avere delle configurazioni salvate in variabili e applicabili a linee tramite setp (passando alla funzione questa variabile) o text

#Annotating text
ax = plt.subplot()

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)
plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.005),) #crea la scritta localmax posizionata in (3, 1.5) con una freccia nera che punta al massimo in xy=(2,1)
plt.ylim(-2, 2) #y da -2 a 2
plt.show()

#NON-LINEAR AXIS

np.random.seed(19680801) #seed fisso per poter replicare il codice

#data in the interval (0, 1)
y = np.random.normal(loc=0.5, scale=0.4, size=1000) #centro della distribuzione, dev standard e numero di valori
y = y[(y > 0) & (y < 1)] #filtro quelli compresi tra 0 e 1
y.sort() #li ordino
x = np.arange(len(y)) #un numero casuale da 0 a  len(y)

#plot figure
plt.figure()

# linear
plt.subplot(221) #2 righe, 2 colonne, primo plot
plt.plot(x, y)
plt.yscale('linear') #scala lineare
plt.title('linear')
plt.grid(True)

# log
plt.subplot(222) #secondo plot
plt.plot(x, y)
plt.yscale('log') #logaritmico
plt.title('log')
plt.grid(True)

# symmetric log
plt.subplot(223) #terzo plot
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.01)
plt.title('symlog') #symmetric log
plt.grid(True)

# logit
plt.subplot(224) #quarto plot
plt.plot(x, y)
plt.yscale('logit') #logit
plt.title('logit')
plt.grid(True)
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35) #margini (top, bottom, left, right) come percentuale della dimensione totale e spazio (hspace verticale tra righe e wspavce orizzontale tra colonne) tra subplot

plt.show()
