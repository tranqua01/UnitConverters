import tkinter as tk
from tkinter import ttk
import dpi
dpi.dpi()

root=tk.Tk()
root.title('TranConverter')
root.geometry('650x300')
root.resizable(False,False)




frame1=tk.Frame(root,padx=5,pady=5)
frame1.grid()
choicein=tk.StringVar(value='meter')
choiceout=tk.StringVar(value='feet')
distanceinput=tk.StringVar(value='0')
textvalue=tk.StringVar(value='0')
def calculatedistance(*args):
    try:
        invalue=float(distanceinput.get())
        #if choiceout.get()==choiceout.get():outvalue=invalue 
        if choicein.get()=='meter':
            if choiceout.get()=='feet': outvalue=invalue*3.2808399
            elif choiceout.get()=='mile': outvalue=invalue*0.000621371
            elif choiceout.get()=='yard': outvalue=invalue*1.09361
            elif choiceout.get()=='inch':outvalue=invalue*39.36996
            elif choiceout.get()=='meter':outvalue=invalue
        elif choicein.get()=='feet':
            if choiceout.get()=='meter': outvalue=invalue*0.3047999
            elif choiceout.get()=='mile':outvalue=invalue*0.00018939336818182
            elif choiceout.get()=='yard':outvalue=invalue*0.33333232800000323071
            elif choiceout.get()=='feet':outvalue=invalue
            elif choiceout.get()=='inch':outvalue=invalue*11.999963808000115861
        elif choicein.get()=='mile':
            if choiceout.get()=='meter': outvalue=invalue*1609.34
            elif choiceout.get()=='mile':outvalue=invalue*1
            elif choiceout.get()=='yard':outvalue=invalue*1760
            elif choiceout.get()=='feet':outvalue=invalue*5280
            elif choiceout.get()=='inch':outvalue=invalue*63360
        elif choicein.get()=='yard':
            if choiceout.get()=='meter': outvalue=invalue*0.9144
            elif choiceout.get()=='mile':outvalue=invalue*0.000568182
            elif choiceout.get()=='yard':outvalue=invalue*1
            elif choiceout.get()=='feet':outvalue=invalue*3
            elif choiceout.get()=='inch':outvalue=invalue*36
        elif choicein.get()=='inch':
            if choiceout.get()=='meter': outvalue=invalue*0.0254
            elif choiceout.get()=='mile':outvalue=invalue*1.5783e-5
            elif choiceout.get()=='yard':outvalue=invalue*0.0277778
            elif choiceout.get()=='feet':outvalue=invalue*0.0833333
            elif choiceout.get()=='inch':outvalue=invalue*1      
        textvalue.set(f'{outvalue}')        
    except ValueError:
        pass

distance_entry=ttk.Entry(frame1, width=15,textvariable=distanceinput)
label1=ttk.Label(frame1,text='Length',font=('bold',11))
distance_input=ttk.Combobox(frame1,width=10,textvariable=choicein)
distance_input['values']=('meter','mile','yard','feet','inch')

distance_result=ttk.Label(frame1,textvariable=textvalue,width=20,font=('normal',12),borderwidth=1,relief="groove")
distance_output=ttk.Combobox(frame1,width=10,textvariable=choiceout)

distance_output['values']=('meter','mile','yard','feet','inch')
#but1=ttk.Button(frame1,text='calculate',command=calculatedistance)

label1.grid(sticky='EW')
distance_entry.grid(row=1,column=0,padx=5,sticky='W')
distance_input.grid(row=1,column=1)
distance_result.grid(row=1,column=2,padx=15)
distance_output.grid(row=1,column=3)
#but1.grid(row=1,column=4,padx=5,pady=5,sticky='EW')
ttk.Separator(root,orient='horizontal').grid(row=1,column=0,sticky='EW')

distanceinput.trace("w",calculatedistance)
#distance_entry.bind("<Key>", calculatedistance)

#-----------------------------------------------------------------------------------------------------
frame2=tk.Frame(root,padx=5,pady=5)
frame2.grid(row=2,column=0)
label2=ttk.Label(frame2,text='Temperature',font=('bold',11))
label2.grid(sticky='EW')

tempinvar=tk.StringVar(value='Celsius')
tempoutvar=tk.StringVar(value='Kelvin')
tempresult=tk.StringVar(value='0')
tempinput=tk.StringVar(value='0')
def tempcalculate(*args):
    try:
        tempinvalue=float(tempinput.get())
        if tempinvar.get()=='Celsius':
            if tempoutvar.get()=='Celsius':tempout=tempinvalue
            elif tempoutvar.get()=='Fahrenheit':tempout=(9/5)*tempinvalue+32
            elif tempoutvar.get()=='Kelvin':tempout=tempinvalue+273.15
        elif tempinvar.get()=='Fahrenheit':
            if tempoutvar.get()=='Fahrenheit':tempout=tempinvalue
            elif tempoutvar.get()=='Celsius': tempout=(tempinvalue-32)*(5/9)
            elif tempoutvar.get()=='Kelvin': tempout=(tempinvalue-32)*(5/9)+273.15
        elif tempinvar.get()=='Kelvin':
            if tempoutvar.get()=='Celsius': tempout=tempinvalue-273.15
            elif tempoutvar.get()=='Kelvin': tempout=tempinvalue
            elif tempoutvar.get()=='Fahrenheit': tempout=(tempinvalue-273.15)*(9/5)+32
        tempresult.set(f'{tempout}')

    except ValueError:
        pass

temp_entry=ttk.Entry(frame2, width=15,textvariable=tempinput)
temp_input=ttk.Combobox(frame2,width=10,textvariable=tempinvar)
temp_input['values']=('Celsius','Fahrenheit','Kelvin')
temp_display=ttk.Label(frame2,textvariable=tempresult,width=20,font=('normal',12),borderwidth=1,relief="groove")
temp_output=ttk.Combobox(frame2,width=10,textvariable=tempoutvar)
temp_output['values']=('Celsius','Fahrenheit','Kelvin')

temp_entry.grid(row=1,column=0,padx=5,sticky='W')
temp_input.grid(row=1,column=1)
temp_display.grid(row=1,column=2,padx=15)
temp_output.grid(row=1,column=3)
#but1.grid(row=1,column=4,padx=5,pady=5,sticky='EW')
ttk.Separator(root,orient='horizontal').grid(row=3,column=0,sticky='EW')
tempinput.trace("w",tempcalculate)
#-------------------------------------------------------------------------
frame3=tk.Frame(root,padx=5,pady=5)
frame3.grid(row=4,column=0)
label3=ttk.Label(frame3,text='Volume',font=('bold',11))
label3.grid(sticky='EW')


entry_input=tk.StringVar(value='0')
label_output=tk.StringVar(value='0')
combo_input=tk.StringVar(value='Liters')
combo_output=tk.StringVar(value='US Gallons')

def vol_convert(*args):
    try:
        vol_in=float(entry_input.get())
        if combo_input.get()=='Liters':
            if combo_output.get()=='Liters': vol_out=vol_in
            elif combo_output.get()=='US Gallons': vol_out=vol_in*0.264172
            elif combo_output.get()=='UK Gallons': vol_out=vol_in*0.219969
            elif combo_output.get()=='UK Pints':vol_out=vol_in*1.75975
            elif combo_output.get()=='UK Ounces':vol_out=vol_in*35.19512617902417
        elif combo_input.get()=='US Gallons':
            if combo_output.get()=='Liters': vol_out=vol_in/(0.264172)
            elif combo_output.get()=='US Gallons':vol_out=vol_in
            elif combo_output.get()=='UK Gallons':vol_out=vol_in*0.832674
            elif combo_output.get()=='UK Pints':vol_out=vol_in*6.66139
            elif combo_output.get()=='UK Ounces':vol_out=vol_in*133.228
        elif combo_input.get()=='UK Gallons':
            if combo_output.get()=='Liters': vol_out=vol_in*13.6383
            elif combo_output.get()=='US Gallons':vol_out=vol_in/(0.832674)
            elif combo_output.get()=='UK Pints': vol_out=vol_in*8
            elif combo_output.get()=='UK Gallons':vol_out=vol_in
            elif combo_output.get()=='UK Ounces': vol_out=vol_in*160
        elif combo_input.get()=='UK Pints':
            if combo_output.get()=='Liters':vol_out=vol_in/(1.75975)
            elif combo_output.get()=='US Gallons': vol_out=vol_in/(6.66139)
            elif combo_output.get()=='UK Gallons': vol_out=vol_in/8
            elif combo_output.get()=='UK Pints': vol_out=vol_in
            elif combo_output.get()=='UK Ounces': vol_out=vol_in*20
        elif combo_input.get()=='UK Ounces':
            if combo_output.get()=='Liters': vol_out=vol_in*0.0284131
            elif combo_output.get()=='US Gallons': vol_out=vol_in/(133.228)
            elif combo_output.get()=='UK Gallons': vol_out=vol_in/(160)
            elif combo_output.get()=='UK Pints': vol_out=vol_in/20
            elif combo_output.get()=='UK Ounces': vol_out=vol_in
        label_output.set(f'{vol_out}')
    except ValueError:
        pass

vol_entry=ttk.Entry(frame3, width=15,textvariable=entry_input)
vol_input=ttk.Combobox(frame3,width=10,textvariable=combo_input)
vol_input['values']=('Liters','US Gallons','UK Gallons','UK Pints','UK Ounces')
vol_display=ttk.Label(frame3,width=20,font=('normal',12),textvariable=label_output,borderwidth=1,relief="groove")
vol_output=ttk.Combobox(frame3,width=10,textvariable=combo_output)
vol_output['values']=('Liters','US Gallons','UK Gallons','UK Pints','UK Ounces')

vol_entry.grid(row=1,column=0,padx=5,sticky='W')
vol_input.grid(row=1,column=1)
vol_display.grid(row=1,column=2,padx=15)
vol_output.grid(row=1,column=3)
#but1.grid(row=1,column=4,padx=5,pady=5,sticky='EW')
ttk.Separator(root,orient='horizontal').grid(row=5,column=0,sticky='EW')

entry_input.trace('w',vol_convert)
#-------------------------------------------------------------------------------------
frame4=tk.Frame(root,padx=5,pady=5)
frame4.grid(row=6,column=0)
label4=ttk.Label(frame4,text='Weight',font=('bold',11))
label4.grid(sticky='EW')

entry4_input=tk.StringVar(value='0')
label4_output=tk.StringVar(value='0')
combo4_input=tk.StringVar(value='Kilograms')
combo4_output=tk.StringVar(value='Pounds')

def weicalculate(*args):
    try:
        wei_in=float(entry4_input.get())
        if combo4_input.get()=='Kilograms':
            if combo4_output.get()=='Pounds': wei_out=wei_in*2.20462
            elif combo4_output.get()=='Kilograms':wei_out=wei_in
            elif combo4_output.get()=='Ounces': wei_out=wei_in*35.274
        elif combo4_input.get()=='Pounds':
            if combo4_output.get()=='Kilograms': wei_out=wei_in/(2.20462)
            elif combo4_output.get()=='Pounds': wei_out=wei_in
            elif combo4_output.get()=='Ounces': wei_out=wei_in*16
        elif combo4_input.get()=='Ounces':
            if combo4_output.get()=='Kilograms': wei_out=wei_in/(35.274)
            elif combo4_output.get()=='Pounds': wei_out=wei_in/16
            elif combo4_output.get()=='Ounces': wei_out=wei_in
        label4_output.set(f'{wei_out}')
    except ValueError:
        pass



wei_entry=ttk.Entry(frame4, width=15,textvariable=entry4_input)
wei_input=ttk.Combobox(frame4,width=10,textvariable=combo4_input)
wei_input['values']=('Kilograms','Pounds','Ounces')
wei_display=ttk.Label(frame4,width=20,font=('normal',12),textvariable=label4_output,borderwidth=1,relief="groove")
wei_output=ttk.Combobox(frame4,width=10,textvariable=combo4_output)
wei_output['values']=('Kilograms','Pounds','Ounces')

wei_entry.grid(row=1,column=0,padx=5,sticky='W')
wei_input.grid(row=1,column=1)
wei_display.grid(row=1,column=2,padx=15)
wei_output.grid(row=1,column=3)
#but1.grid(row=1,column=4,padx=5,pady=5,sticky='EW')
ttk.Separator(root,orient='horizontal').grid(row=7,column=0,sticky='EW')

entry4_input.trace('w',weicalculate)



#-----------------------------------------------------------------------------------
def allfunction(*args):
    tempcalculate()
    calculatedistance()
    vol_convert()
    weicalculate()
root.bind('<Return>',allfunction)
root.bind_all('<KP_Enter>',allfunction)

root.mainloop()