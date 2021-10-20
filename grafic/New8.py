import matplotlib.pyplot as plt
import numpy as np
try:

    #with open('data.txt', 'r') as infile:
        #tmp = [float(i) in infile.read().split("\n")]
    data_array = np.loadtxt("data.txt", dtype=float)
    #with open ('settings.txt', 'r') as setting:
        #tmp1 =[float(i) in setting.read().split("\n")] 
    setting_array = np.loadtxt("settings.txt", dtype=float)
    timef= setting_array[0]
    napr= setting_array[1]
    time_list =[]
    voltage_array =data_array*3.3/256
    time_list = list(range(0, len(voltage_array)))
    time_list =[i/100 for i in time_list]
    fig_data = plt.figure()

    #time_array = np.arange(0, len(voltage_array)-1, timef)
    time_zaradka = 4.20
    time_razradka = 5.8 
    plot = fig_data.add_subplot(111)
    line_plot = plot.plot(time_list, voltage_array, marker = '.', color = 'green', linewidth =1, label = 'напряжение', markevery= 35)
    plot.set_title('RC')
    plot.set_xlabel('Time, s')
    plot.set_ylabel('Voltage, u')
    plot.legend()
    plot.grid(color='r', linestyle='-', linewidth=0.5)
    plot.text(5.5, 2.5, 'Время зарядки= 4.20' )
    plot.text(5.5, 2, 'Время разрядки = 5.8' )
    fig_data.savefig("test.png")
    plt.show()

finally:
    print('1')