module Ejercicio_6 where


type Texto = [Char]

type Nombre = Texto

type Telefono = Texto

type Contacto = (Nombre, Telefono)

type ContactosTel = [Contacto]

enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos nombreQ [] = False
enLosContactos nombreQ ((nombre,_):xs) = nombre == nombreQ ||enLosContactos nombreQ xs

actualizarContacto :: Contacto -> ContactosTel -> ContactosTel
actualizarContacto (nombre,telefono) [] = []
actualizarContacto (nombre, telefono) (x:xs) 
    | nombre == fst x = (nombre,telefono):xs
    | otherwise = x : actualizarContacto (nombre, telefono) xs

agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto contacto lista 
    | not (enLosContactos (fst contacto) lista) = contacto : lista
    | otherwise = actualizarContacto contacto lista

eliminarContacto :: Nombre -> ContactosTel -> ContactosTel
eliminarContacto nombreQ [] = []
eliminarContacto nombreQ (x:xs) 
    | nombreQ == (fst x) = xs
    | otherwise = x : (eliminarContacto nombreQ xs)
