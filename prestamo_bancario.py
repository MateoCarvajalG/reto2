#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 10:06:27 2020

@author: mateo
"""

def prestamo(informacion: dict) -> dict:
    
    h_c=informacion['historia_credito']   
    i_c = informacion['ingreso_codeudor']
    i_d = informacion['ingreso_deudor']
    c_p =informacion ['cantidad_prestamo']
    independiente= informacion['independiente']
    dependientes = informacion['dependientes']
    casado=informacion['casado']
    propiedad=informacion['tipo_propiedad']
    graduado=informacion['educacion']
    if dependientes == '3+':
        dependientes=3
    
    
    if h_c == 1 :                                               # SI tiene historial crediticio
        if (i_c < 0) and ((i_d/9)>c_p):
            resultado= True 
        else:
            if dependientes > 2 and independiente == 'Si' : 
                if (i_c/12) > c_p:
                    resultado = True
                else:
                    resultado = False
            else:
                if c_p < 200:
                    resultado = True
                else:
                    resultado = False
 #-------------------------Acaba la rama de si tiene historial crediticio---------------------   
    else:                                                        # NO tiene historial crediticio
#----------------- INICIA la rama de No tiene historial crediticio---------------------------
        if independiente == 'Si':                                # Es independiente
#-----------------------------INICIA la rama de es independiente------------------------------------        
            if not(casado=='Si' and dependientes >1) :           # NO es casado o NO tienemas de 1 dependiente(ley de morgan)
                if ((i_d/10)>c_p) or ((i_c/10)>c_p):
                    if c_p < 180:
                        resultado=True
                    else:
                        resultado=False
                else:
                    resultado=False
            else :
                resultado=False                                                
            
#--------------------------- FINALIZA la rama de es independiente----------------------------            
        else:                                                    # NO es independiente
#--------------------------- INICIA  la rama de NO es independiente--------------------------
            if  (not propiedad =='Semiurbano') and (dependientes<2):
                if graduado == 'Graduado'  :                        # SI es Graduado
                    if ((i_d/11)>c_p) and ((i_c/11)>c_p) :
                        resultado=True
                    else:
                        resultado=False    
                else:                                               # NO es Graduado  
                    resultado=False
            else:
                resultado=False
    
    
    diccionario_respuesta = {
        'id_prestamo': informacion['id_prestamo'],
        'aprobado': resultado,
        }
    return diccionario_respuesta
    
#-----------------------------PRUEBA DE LA FUNCION---------------------------
informacion = {
    'id_prestamo': 'RETOS2_001' ,
    'casado':'No' ,
    'dependientes': 1,
    'educacion': 'Graduado',
    'independiente': 'Si',
    'ingreso_deudor': 4692,
    'ingreso_codeudor': 0 ,
    'cantidad_prestamo': 106,
    'plazo_prestamo': 360,
    'historia_credito': 1 ,
    'tipo_propiedad': 'Rural',    
    }
print(prestamo(informacion))

