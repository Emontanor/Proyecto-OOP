# !/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mssg
import sqlite3

class Inventario:
    def __init__(self, master=None):
        # self.path = r'X:/Users/ferna/Documents/UNal/Alumnos/2023_S2/ProyInventario'
        # self.db_name = self.path + r'/Inventario.db'
        self.db_name = "Inventario.db" # esto se debe quitar
        # Dimensiones de la pantalla
        ancho=800
        alto=700
        self.actualiza = None

        # Crea ventana principal
        self.win = tk.Tk()
        self.win.minsize(int(ancho/1.25), alto//2)
        self.win.geometry(f"{ancho}x{alto}")
        icon_name = "f2.ico"
        self.win.iconbitmap(icon_name)
        self.win.title("Manejo de Proveedores")

        #Centra la pantalla
        self.centra(self.win,ancho,alto)

        # Contenedor de widgets
        self.label_frame = tk.LabelFrame(master)
        self.label_frame.configure(background="#e0e0e0",font="{Arial} 12 {bold}",labelanchor="n")
        self.tabs = ttk.Notebook(self.label_frame)
        self.tabs.configure(height=800, width=800)

        #Main frame
        self.main_frame = ttk.Frame(self.tabs)

        #Frame de datos
        self.frm1 = ttk.Frame(self.main_frame)
        self.frm1.configure(height=200, width=200)
        self.frm1.columnconfigure((0,3,4,6,7,8,9,10,11,13,14,15), weight=1)
        # self.frm1.columnconfigure((3,4,7,9,10,14), minsize=30)
        self.frm1.rowconfigure((1,2,5,11), weight=1)
        self.frm1.rowconfigure((0,4,7), weight=1, minsize=70)
        self.frm1.rowconfigure((11,), weight=1, minsize=300)

        #Etiqueta IdNit del Proveedor
        self.lblIdNit = ttk.Label(self.frm1)
        self.lblIdNit.configure(text='Id/Nit', anchor="center")
        self.lblIdNit.grid(row=0, column=1, sticky="we", pady=25, padx=5)

        #Captura IdNit del Proveedor
        self.idNit_sv = tk.StringVar()
        self.idNit = ttk.Entry(self.frm1, textvariable=self.idNit_sv)
        self.idNit.configure(takefocus=True, width=17)
        self.idNit.grid(row=0, column=2, columnspan=2, sticky="w", pady=25)
        self.idNit_sv.trace("w",self.validaIdNit)
        self.idNit.focus()

        #Etiqueta razón social del Proveedor
        self.lblRazonSocial = ttk.Label(self.frm1)
        self.lblRazonSocial.configure(text='Razon social', anchor="center")
        self.lblRazonSocial.grid(row=0, column=5, sticky="we", pady=25, padx=5)

        #Captura razón social del Proveedor
        self.razonSocial = ttk.Entry(self.frm1, width=25)
        self.razonSocial.grid(row=0, column=6, columnspan=5, sticky="w", pady=25)

        #Etiqueta ciudad del Proveedor
        self.lblCiudad = ttk.Label(self.frm1)
        self.lblCiudad.configure(text='Ciudad', anchor="center")
        self.lblCiudad.grid(row=0, column=12, sticky="we", pady=25, padx=5)

        #Captura ciudad del Proveedor
        self.ciudad = ttk.Entry(self.frm1, width=20)
        self.ciudad.grid(row=0, column=13, columnspan=3, sticky="w", pady=25)

        #Separador
        self.separador1 = ttk.Separator(self.frm1)
        self.separador1.configure(orient="horizontal")
        self.separador1.grid(row=3, column=0, columnspan=17, sticky="we", pady=5)

        #Etiqueta Código del Producto
        self.lblCodigo = ttk.Label(self.frm1)
        self.lblCodigo.configure(text='Código', anchor="center")
        self.lblCodigo.grid(row=4, column=1, sticky="we", pady=25, padx=5)

        #Captura el código del Producto
        self.codigo = ttk.Entry(self.frm1, width=10)
        self.codigo.grid(row=4, column=2, sticky="w", columnspan=2, pady=25)

        #Etiqueta descripción del Producto
        self.lblDescripcion = ttk.Label(self.frm1)
        self.lblDescripcion.configure(text='Descripción', anchor="center")
        self.lblDescripcion.grid(row=4, column=5, sticky="we", pady=25, padx=5)

        #Captura la descripción del Producto
        self.descripcion = ttk.Entry(self.frm1, width=25)
        self.descripcion.grid(row=4, column=6, columnspan=5, sticky="w", pady=25)

        #Etiqueta unidad o medida del Producto
        self.lblUnd = ttk.Label(self.frm1)
        self.lblUnd.configure(text='Unidad', anchor="center")
        self.lblUnd.grid(row=4, column=12, sticky="we", pady=25, padx=5)

        #Captura la unidad o medida del Producto
        self.unidad = ttk.Entry(self.frm1, width=12)
        self.unidad.grid(row=4, column=13, sticky="w", pady=25)

        #Etiqueta cantidad del Producto
        self.lblCantidad = ttk.Label(self.frm1)
        self.lblCantidad.configure(text='Cantidad', anchor="center")
        self.lblCantidad.grid(row=7, column=1, sticky="we", pady=25, padx=5)

        #Captura la cantidad del Producto
        self.cantidad = ttk.Entry(self.frm1, width=10)
        self.cantidad.grid(row=7, column=2, sticky="w", pady=25)

        #Etiqueta precio del Producto
        self.lblPrecio = ttk.Label(self.frm1)
        self.lblPrecio.configure(text='Precio $', anchor="center")
        self.lblPrecio.grid(row=7, column=5, sticky="we", pady=25, padx=5)

        #Captura el precio del Producto
        self.precio = ttk.Entry(self.frm1, width=10)
        self.precio.grid(row=7, column=6, sticky="w", pady=25)

        #Etiqueta fecha de compra del Producto
        self.lblFecha = ttk.Label(self.frm1)
        self.lblFecha.configure(text='Fecha', anchor="center")
        self.lblFecha.grid(row=7, column=12, sticky="we", pady=25, padx=5)

        #Captura la fecha de compra del Producto
        self.fecha_sv = tk.StringVar(value="dd/mm/aaaa")
        self.fecha = ttk.Entry(self.frm1, width=12, textvariable=self.fecha_sv, )
        self.fecha.grid(row=7, column=13, sticky="w", pady=25)
        for i in ("Button-1", "Left", "Right", "Key","BackSpace", "space"):
            self.fecha.bind(f"<{i}>", self.validaFecha)
        self.fecha.bind("<FocusOut>", self.fechaFocusOut)
        self.fecha.bind("<FocusIn>", self.fechaFocusIn)
        self.fecha_mal = False
        
        #Separador
        self.separador2 = ttk.Separator(self.frm1)
        self.separador2.configure(orient="horizontal")
        self.separador2.grid(row=10, column=0, columnspan=17, sticky="we", pady=5)

        #tablaTreeView
        self.style=ttk.Style()
        self.style.configure("estilo.Treeview", highlightthickness=0, bd=0, background="#e0e0e0", font=('Calibri Light',10))
        self.style.configure("estilo.Treeview.Heading", background='Azure', font=('Calibri Light', 10,'bold')) 
        self.style.layout("estilo.Treeview", [('estilo.Treeview.treearea', {'sticky': 'nswe'})])
        
        #Árbol para mosrtar los datos de la B.D.
        self.treeProductos = ttk.Treeview(self.frm1, style="estilo.Treeview")
        
        self.treeProductos.configure(selectmode="extended")

        # Etiquetas de las columnas para el TreeView
        self.treeProductos["columns"]=("Codigo","Descripcion","Und","Cantidad","Precio","Fecha")
        # Características de las columnas del árbol
        self.treeProductos.column ("#0",          anchor="w",stretch=True,width=3)
        self.treeProductos.column ("Codigo",      anchor="w",stretch=True,width=3)
        self.treeProductos.column ("Descripcion", anchor="w",stretch=True,width=150)
        self.treeProductos.column ("Und",         anchor="w",stretch=True,width=3)
        self.treeProductos.column ("Cantidad",    anchor="w",stretch=True,width=3)
        self.treeProductos.column ("Precio",      anchor="w",stretch=True,width=8)
        self.treeProductos.column ("Fecha",       anchor="w",stretch=True,width=3)

        # Etiquetas de columnas con los nombres que se mostrarán por cada columna
        self.treeProductos.heading("#0",          anchor="center", text='ID / Nit')
        self.treeProductos.heading("Codigo",      anchor="center", text='Código')
        self.treeProductos.heading("Descripcion", anchor="center", text='Descripción')
        self.treeProductos.heading("Und",         anchor="center", text='Unidad')
        self.treeProductos.heading("Cantidad",    anchor="center", text='Cantidad')
        self.treeProductos.heading("Precio",      anchor="center", text='Precio')
        self.treeProductos.heading("Fecha",       anchor="center", text='Fecha')

        # self.treeProductos.bind("<<TreeviewSelect>>", self.habilitarEdicion)
        self.treeProductos.grid(row=11, column=0, columnspan=16, sticky="news")

        #Scrollbar en el eje Y de treeProductos
        self.scrollbary=ttk.Scrollbar(self.frm1, orient='vertical', command=self.treeProductos.yview)
        self.treeProductos.configure(yscroll=self.scrollbary.set)
        self.scrollbary.grid(row=11, column=16, sticky="ns")

        #Frame 2 para contener los botones
        self.frm2 = ttk.Frame(self.main_frame)
        self.frm2.configure()
        trailingCols = 10
        self.frm2.columnconfigure(
            (
                *range(trailingCols),
                trailingCols+1,
                trailingCols+3,
                trailingCols+5,
                trailingCols+7,
                *range(trailingCols+9,2*trailingCols+8)
            ),
            weight=1
            )
        self.frm2.columnconfigure(
            (
                trailingCols,
                trailingCols+2,
                trailingCols+4,
                trailingCols+6,
                trailingCols+8,
            ),
            minsize=70,
            weight=0
            )
        self.frm2.rowconfigure((0,2), weight=1)

        #Botón para Buscar un Proveedor
        self.btnBuscar = ttk.Button(self.frm2)
        self.btnBuscar.configure(text='Buscar', command=self.buscar)
        self.btnBuscar.grid(row=1, column=trailingCols)

        #Botón para Guardar los datos
        self.btnGrabar = ttk.Button(self.frm2)
        self.btnGrabar.configure(text='Grabar', command=self.grabar)
        self.btnGrabar.grid(row=1, column=trailingCols+2)

        #Botón para Editar los datos
        self.btnEditar = ttk.Button(self.frm2)
        self.btnEditar.configure(text='Editar', command=self.editar)
        self.btnEditar.grid(row=1, column=trailingCols+4)

        #Botón para Elimnar datos
        self.btnEliminar = ttk.Button(self.frm2)
        self.btnEliminar.configure(text='Eliminar', command = self.selecEliminar)
        self.btnEliminar.grid(row=1, column=trailingCols+6)
        self.ventana = None

        #Botón para cancelar una operación
        self.btnCancelar = ttk.Button(self.frm2)
        self.btnCancelar.configure(text='Cancelar',command = self.cancelar)
        self.btnCancelar.grid(row=1, column=trailingCols+8)

        #Ubicación del Frame 2
        self.frm2.pack(side="bottom", anchor="s", expand=True, fill="both")
        self.label_frame.pack(anchor="center", side="top", expand=True, fill="both")
        
        # Título de la pestaña Ingreso de Datos
        self.frm1.pack(side="top", expand=True, fill="both")
        self.tabs.add(self.main_frame, compound="center", text='Ingreso de datos')
        self.tabs.pack(side="top", expand=True, fill="both")


        # widget Principal del sistema
        self.mainwindow = self.label_frame

    def run(self):
        """Fución de manejo de eventos del sistema"""
        self.mainwindow.mainloop()

    # Métodos utilitarios del sistema-----------------------------------------
    
    # def habilitarEdicion(self, event):
    #     seleccion=self.treeProductos.selection()
    #     if seleccion:
    #         self.btnEditar["state"] = "normal"
    #     else :
    #         self.btnEditar["state"] = "disabled"
    
    #Rutina de centrado de pantalla
    def centra(self,win: tk.Tk,ancho,alto):
        """ centra las ventanas en la pantalla """ 
        x = win.winfo_screenwidth() // 2 - ancho // 2
        y = win.winfo_screenheight() // 2 - alto // 2
        win.geometry(f'{ancho}x{alto}+{x}+{y}')
        # win.deiconify() # Se usa para restaurar la ventana

    def idExiste(self, id: str) -> bool:
        """Retorna si existe el idNit en Proveedor"""
        return bool(self.run_Query('SELECT count(*) FROM Proveedor WHERE IdNitProv = ?;',(id,)).fetchone()[0])
    
    # Validaciones del sistema
    def validaIdNit(self, _,__,___):
        ''' Valida que la longitud no sea mayor a 15 caracteres'''
        if len(self.idNit.get()) > 15:
            mssg.showerror('Atención!!','.. ¡Máximo 15 caracteres! ..')
            self.idNit.delete(15,"end")

    def isFechaValida(self, fecha:str) -> tuple[bool,str]:
        """ Revisa si la fecha es valida\n
            retorna: 
                -una tupla con el bool como resultado de la validación\n
                -un str como la razon de porque es invalido ("" si es valido)"""
        try:
            dia, mes, año = (int(i) for i in fecha.split("/"))
        except ValueError:
            return False, "Las fechas deben estar compuestas solo por números enteros positivos"
        if año < 1000:
            return False,"El año debe ser de cuatro digitos (minimo 1000)"
        es_biciesto = (año%4 == 0) and ((año%100 != 0) or (año%400 == 0))
        max_dia = 31
        if mes > 12 or mes < 0:
            return False, "El mes debe ser un número entero entre 12 y 0"
        elif mes == 2: max_dia =28 + (1 if es_biciesto else 0) #si es biciesto y el mes es febrero 
        #Enero, Marzo, Mayo, Julio,
        elif mes in (1,3,5,7,9,10,12): max_dia = 30
        if dia < 0:
            return False, "El día debe ser un número entero positivo"
        if dia > max_dia or dia < 0:
            mes_str = ( "Enero", "Febrero", "Marzo", "Abril", "Mayo",
                        "Junio", "Julio", "Agosto", "Septiembre",
                        "Octubre", "Noviembre", "Diciembre"
                      )[mes]
            return False, f"Día invalido para {mes_str}, el maximo es {max_dia}"
        return True, ""
    
    def fechaFocusIn(self, _):
        """Se ejecuta cuando se entra al Entry fecha"""
        self.fecha.after_idle(self.fecha.icursor,0) #pone el cusor al inicio del entry
    
    def fechaFocusOut(self, event):
        """Se ejecuta cuando se sale del Entry fecha"""
        valida = self.isFechaValida(self.fecha.get())
        if (not valida[0]) and self.fecha.get().replace("/","").isnumeric():
            self.validaFecha(event)
            mssg.showerror("Atención!!", "¡Fecha invalida!!!\n"+valida[1])
    
    def validaFecha(self, event: tk.Event):
        """ Mantiene correctamente escrita a la variable fecha"""
        #nota: esta funcion ocurre antes de que se le aplicen cambios al entry por el usuario
        
        brk = False #si es True interrumpe la entrada de valores a self.fecha
        if event.type == 1: position = self.fecha.index("insert")
        else: position = self.fecha.index("insert") #El indice donde se encuentra el cusor
        
        seleccionado = False
        #si esta selecionada parte del texto
        if self.fecha.select_present():
            seleccionado = True
            position = self.fecha.index("sel.first")
            self.fecha.after_idle(self.fecha.select_clear)
            brk = True
            self.fecha.after_idle(self.fecha.icursor, position+1)
        #modificacion del texto dentro del entry -----------------------------------
        #si esta entrando un numero
        if event.keysym.isnumeric():
            #quitar el caracter que estaba en ese espacio
            if position < 10 and not position in (2,5):
                self.fecha.delete(position, position+1)
                #si se seleccionó texto añadir manualmente el caracter
                if seleccionado: self.fecha.insert(position, event.char)
                position += 1
            #pero si esta al final del entry no permitir la entrada del caracter
            else:
                brk = True
        #si esta borrando
        elif event.keysym == "BackSpace" and position > 0:
            #si se seleccionó texto moverlo hacia adelante (se maneja mejor)
            if seleccionado: position += 1
            #reemplazar caracter a borrar con el correspondiente ('d', 'm', o 'a')
            char = "a"
            if position <= 3: char = "d"
            elif position <= 6: char = "m" 
            #si esta despues de un '/' mover el cursor hacia atras para no borrarlo
            if position in (3, 6):
                position -= 1 
            position -= 1
            self.fecha.delete(position,position+1)
            self.fecha.insert(position, char)
            #reposicionar el cursor despues de modificar el entry
            self.fecha.after_idle(self.fecha.icursor, position)
            brk = True
        elif len(event.char) >= 1 and int(event.type) != 4:
            #borra el ultimo caracter digitado
            brk = True
        #movimiento por flechas ----------------------------------------------------
        if event.keysym == "Left": position -= 1
        elif event.keysym == "Right": position += 1
        #cuando el cursor llega detras de un '/' lo mueve adelante de el
        #a no ser de que halla texto seleccionado
        if position in (2, 5) and not seleccionado:
            mover = position+(-1 if event.keysym == "Left" else 1)
            self.fecha.after_idle(self.fecha.icursor,mover)
            position = mover
        
        #mostrar validez de fecha --------------------------------------------------
        #si todos los valores de fecha son numeros (exepto los '/')
        #osea ya es una fecha
        if (self.fecha.get().replace("/","")).isnumeric():
            if self.isFechaValida(self.fecha.get()+event.char)[0]:
                self.fecha.configure(foreground="black")
            else:self.fecha.configure(foreground="red")
        
        #en caso de que el largo de fecha sea mayor a 10 repararlo
        if len(self.fecha_sv.get())>10: self.fecha_sv.set(self.fecha_sv.get()[:10])
        
        #cuando un metodo que se ejecuto por bind y retorna "break" no se
        #ejecuta el resto de binds (no puede añadir caracteres al Entry)
        if brk: return "break"
    
    #Rutina de limpieza de datos
    def limpiaCampos(self):
        ''' Limpia todos los campos de captura'''
        self.actualiza = None
        self.idNit.config(state = 'normal')
        self.codigo.config(state = 'normal')
        self.razonSocial.config(state = 'normal')
        self.ciudad.config(state = 'normal')
        self.idNit.delete(0,'end')
        self.razonSocial.delete(0,'end')
        self.ciudad.delete(0,'end')
        self.idNit.delete(0,'end')
        self.codigo.delete(0,'end')
        self.descripcion.delete(0,'end')
        self.unidad.delete(0,'end')
        self.cantidad.delete(0,'end')
        self.precio.delete(0,'end')
        self.fecha.delete(0,'end')
        self.fecha.insert(0,'dd/mm/aaaa')
    
    def carga_Datos(self, seleccion: str):
        """Rutina para cargar los datos del árbol a los entry correspondientes"""
        self.limpiaCampos()
        #insertando valores del tree a los Entry
        #valores de Productos
        tree_items = self.treeProductos.item(seleccion)
        items_Productos = tree_items["values"]
        self.idNit.insert(0, tree_items["text"]) #"text" porque es el primer campo
        self.codigo.insert(0,items_Productos[0])
        self.descripcion.insert(0,items_Productos[1])
        self.unidad.insert(0,items_Productos[2])
        self.cantidad.insert(0,items_Productos[3])
        self.precio.insert(0, items_Productos[4])
        self.fecha.delete(0,"end")
        self.fecha.insert(0, items_Productos[5])
    
    # Operaciones con la base de datos
    def run_Query(self, query, parametros = ()) -> sqlite3.Cursor:
        ''' Función para ejecutar los Querys a la base de datos '''
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parametros)
            conn.commit()
        return result

    def lee_treeProductos(self, id:str):
        ''' Limpia la Tabla tablaTreeView y Carga los datos de nuevo
        Si se provee un id solo carga las filas con ese id/Nit'''
        tabla_TreeView = self.treeProductos.get_children()
        for linea in tabla_TreeView:
            self.treeProductos.delete(linea) # Límpia la filas del TreeView
        
        if id == "":
            return
        # Seleccionando los datos de la BD
        # query = '''SELECT * from Proveedor INNER JOIN Productos WHERE idNitProv = idNit ORDER BY idNitProv'''
        query = f"SELECT * FROM Productos WHERE IdNit = ? ORDER BY IdNit;" # hace lo mismo con menos
        db_rows = self.run_Query(query,() if id == "" else (id,)) # db_rows contine la vista del query
        
        # Insertando los datos de la BD en treeProductos de la pantalla
        for row in db_rows:
            self.treeProductos.insert('',0, text = row[0], values = row[1:])
    
    def editarProductos(
        self,
        id: str,
        codigo: str,
        desc: str,
        unidad: str,
        cantidad: float,
        precio: float,
        fecha: str) -> None:
        """Edita los datos de la tabla Productos en un idNit y codigo con los datos.
        
        Los datos deben ser validados antes de ser llamada
        
        Retorna true si se aplico el cambio correctamente"""
        completado = False
        WHERE = f'WHERE IdNit = ? AND Codigo = ?'
        datos = (
            (0, "Descripcion", desc),
            (1, "Und", unidad),
            (2, "Cantidad", cantidad),
            (3, "Precio", precio),
            (4, "Fecha", fecha)
        )
        registroActual = self.run_Query(
            f'SELECT Descripcion, Und, Cantidad, Precio, Fecha FROM Productos {WHERE};',
            (id, codigo)
            ).fetchone()
        if not registroActual:
            mssg.showerror("Id/Codigo invalido", "No existe un producto con ese IdNit y Codigo")
            return False
        
        #para cambiar los datos del registro al mismo formato que el resto de datos
        registroActual = tuple(
            map(
                lambda x: 
                    (lambda x: x if type(x) != str else x.replace('"','""'))(x)
                    if x!=None else "NULL"
                ,registroActual
                )
            )
        cambiar = []
        parametros = []
        for i,k,v in datos:
            if v != registroActual[i]:
                cambiar.append(f'{k} = ?')
                parametros.append(v)
                
        if cambiar and mssg.askokcancel("Confirmación","¿Desea editar la tabla Productos?"):
            cambiar = ", ".join(cambiar)
            try:
                self.run_Query(f'UPDATE Productos SET {cambiar} {WHERE};',(*parametros,id,codigo))
                completado = True
            except:
                mssg.showerror("Edicion fallida", "Fallo el cambio de datos en la tabla Productos")
                return
            else:
                mssg.showinfo("Edicion completada", "Se completo cambio de datos en la tabla Productos")
        return completado
    
    def editarProveedor(self, id: str, razon: str, ciudad: str) -> None:
        """Edita los datos de la tabla Proveedor en un idNit con los datos.
        
        Los datos deben ser validados antes de ser llamada
        
        Retorna true si se aplico el cambio correctamente"""
        completado = False
        WHERE = f'WHERE IdNitProv = ?'
        registroActual = self.run_Query(
            f'SELECT Ciudad,RazonSocial FROM Proveedor {WHERE};',
            (id,)
            ).fetchone()
        if not registroActual:
            mssg.showerror("Id invalido","No existe el idNit en la tabla Proveedor")
            return False
        registroActual = tuple(map(lambda x: x if x!=None else "NULL",registroActual))
        #valores a cambiar
        cambiar = []
        parametros = []
        if razon != registroActual[0]:
            cambiar.append(f'RazonSocial = ?')
            parametros.append(razon)
        if ciudad != registroActual[1]:
            cambiar.append(f'Ciudad = ?')
            parametros.append(ciudad)
        #Aplica los cambios
        
        if cambiar and mssg.askokcancel("Confirmación","¿Desea editar la tabla Proveedor?"):
            cambiar = ", ".join(cambiar)
            try:
                self.run_Query(
                    f'UPDATE Proveedor SET {cambiar} {WHERE};',
                    (*parametros, id)
                   )
                completado = True
            except:
                mssg.showerror("Edicion fallida", "Fallo el cambio de datos en la tabla Proveedor")
            else:
                mssg.showinfo("Edicion completada", "Se completo cambio de datos en la tabla Proveedor")
        return completado
    
    def validacionCampos(self) -> bool:
        """Valida los datos en los entry, avisa al usuario de datos invalidos
        y retorna false si hay datos invalidos; True si todos son validos"""
        #validaciones de descripcion, unidad, razon social, y ciudad son innecesarias
        
        invalido = "" #para guardar las razones por las que un dato es invalido
        #validacion idNit
        id = self.idNit.get()
        if len(id) > 15:
            invalido += "El ID debe ser menor a 15\n"
        elif id == "":
            invalido += "El campo ID no puede estar vacio\n"
        id = id.replace('"','""')
        
        codigo = self.codigo.get().replace('"','""')
        if codigo != "":
            if (
                self.actualiza == None and
                self.run_Query(
                    'SELECT count(*) FROM Productos WHERE Codigo = ? AND IdNit = ?',
                    (codigo, id)
                    ).fetchone()[0] != 0
                ):
                invalido += f"El codigo {codigo} para el proveedor {id} ya existe, los codigos deben ser unicos\n"
            #validadcion cantidad
            cantidad = self.cantidad.get()
            if cantidad != "":
                if (not cantidad.replace(".","").isnumeric()) or float(cantidad) < 0:
                    invalido += "Las cantidades deben ser números positivos\n"
            #validadcion precio
            precio = self.precio.get()
            if precio != "":
                if (not precio.replace(".","").isnumeric()) or float(precio) < 0:
                    invalido += "Los precios deben ser números positivos\n"
            #validadcion fecha
            fechaValida, porque = self.isFechaValida(self.fecha.get())
            if not fechaValida:
                invalido += porque
        
        if invalido:
            mssg.showerror("¡Datos Incorrectos!!!", str(invalido.removesuffix("\n")))
            return False
        return True
    
    def adiciona_Registro(
        self,
        id: str,
        codigo: str,
        desc: str,
        unidad: str,
        razon: str,
        ciudad: str,
        cantidad: float,
        precio: float,
        fecha: str) -> bool:
        '''Adiciona un producto a la BD. La validación debe ser True'''
        
        existe = False
        if self.idExiste(id):
            if codigo == "":
                mssg.showerror("Error","Este proveedor ya existe, si desea editarlo presione editar")
                return
            elif bool(self.run_Query(
                'SELECT COUNT(*) FROM Productos WHERE idNit = ? AND Codigo = ?',
                (id, codigo)
                ).fetchone()[0]):
                mssg.showerror("Error","Ya existe un producto con misma idNit y Codigo")
                return
        else:
            if mssg.askokcancel("Confirmación","Desea añadir los datos a la tabla Proveedor?"):
                try:
                    self.run_Query(
                        'INSERT INTO Proveedor VALUES(?, ?, ?);',
                        (id, razon, ciudad)
                        )
                except Exception as e:
                    mssg.showerror("Resultado de la acción", "Ocurrio un error al intentar añadir datos a Proveedor")
                    return
                else:
                    mssg.showinfo("Resultado de la acción", "Se añadieron los items a la base de datos correctamente")
            else:
                mssg.showinfo("Cancelando", "Cancelando guardado de registro")
                return
        if codigo != "" and mssg.askokcancel("Confirmacion", "Desea añadir los datos a Productos?"):
            rowProductos = (id,codigo, desc, unidad, cantidad, precio,fecha)
            try:
                self.run_Query(
                    'INSERT INTO Productos VALUES(?,?,?,?,?,?,?);',
                    rowProductos
                    )
            except:
                mssg.showerror("Resultado de la acción", "Ocurrio un error al intentar añadir datos a Productos")
                return
            else:
                mssg.showinfo("Resultado de la acción", "Se añadieron los items a Productos correctamente")
        self.lee_treeProductos(id)
        self.limpiaCampos()

    def buscar(self):
        """Busca un idNit en la base de datos y la muestra en el treeview.
        
        Tambien se colocan los valores de ciudad y razon social de ese id en sus entry"""
        id = self.idNit.get()
        if id == "":
            mssg.showerror("Error Id", "El campo Id/Nit esta vacio")
        else:
            idValues = self.run_Query(
                'SELECT Ciudad,RazonSocial FROM Proveedor WHERE idNitProv = ?',
                (id,)
                ).fetchone()
            if idValues:
                self.lee_treeProductos(id)
                self.ciudad.delete(0,'end')
                self.razonSocial.delete(0,'end')
                self.ciudad.insert(0, "" if idValues[0]==None else idValues[0])
                self.razonSocial.insert(0, "" if idValues[1]==None else idValues[1])
                self.ciudad["state"] = "readonly"
                self.razonSocial["state"] = "readonly"
            else: mssg.showerror("Error Id", f"No existe el id: {id}")
    
    def editar(self, event: tk.Event=None) -> None:
        """Rutina para cuando se presiona editar"""
        seleccion = self.treeProductos.selection()
        if len(seleccion) == 0:
            id = self.idNit.get()
            if id == "":
                mssg.showerror("Error editar", "Debe haber un IdNit para editar un Proveedor o seleccionar un registro a editar")
            else:
                idValues = self.run_Query(
                    'SELECT Ciudad,RazonSocial FROM Proveedor WHERE idNitProv = ?',
                    (id,)
                    ).fetchone()
                if idValues:
                    self.ciudad["state"] = "normal"
                    self.razonSocial["state"] = "normal"
                    self.ciudad.delete(0,'end')
                    self.razonSocial.delete(0,'end')
                    self.ciudad.insert(0, "" if idValues[0]==None else idValues[0])
                    self.razonSocial.insert(0, "" if idValues[1]==None else idValues[1])
                    self.actualiza = True
                else:
                    mssg.showerror("Error Id", f"No existe el id: {id}")
        elif len(seleccion) == 1:
            self.carga_Datos(seleccion[0])
            self.deseleccionarTree()
            self.idNit["state"] = "readonly"
            self.codigo["state"] = "readonly"
            self.razonSocial["state"] = "normal"
            self.ciudad["state"] = "normal"
            self.actualiza = seleccion[0]
        else: mssg.showerror("Error seleccion","Se debe seleccionar una sola fila para poder editar")
        
    
    def grabar(self):
        """Rutina para cuando se presiona grabar"""
        if self.validacionCampos():
            #obtencion de datos dentro de los entrys
            id = self.idNit.get()
            codigo = self.codigo.get()
            desc = self.descripcion.get()
            unidad = self.unidad.get()
            razon = self.razonSocial.get()
            ciudad = self.ciudad.get()
            cantidad = self.cantidad.get()
            precio = self.precio.get()
            fecha = self.fecha.get()
            
            datos = (codigo,desc,unidad,cantidad,precio,fecha)
            if codigo != "":
                if cantidad != "": cantidad = float(cantidad)
                if precio != "": precio = float(precio)
            
            #si se esta adicionando un nuevo registro
            if self.actualiza == None:
                self.adiciona_Registro(id,codigo,desc,unidad,razon,ciudad,cantidad,precio,fecha)
            else: #si se esta editando un registro
                self.editarProveedor(id,razon,ciudad)
                if codigo != "":
                    if self.editarProductos(id,codigo,desc,unidad,cantidad,precio,fecha):
                        self.idNit["state"] = "normal"
                        self.codigo["state"] = "normal"
                        self.treeProductos.item(self.actualiza,values=datos)
                    else:
                        return
                self.actualiza = None
                self.limpiaCampos()
                
            
    
    def cancelar(self):
        self.limpiaCampos()
        self.lee_treeProductos("")
        self.deseleccionarTree()
        self.cancelar_ventana()
        
        self.actualiza = None
        self.idNit["state"] = "normal"
        self.codigo["state"] = "normal"
        self.btnGrabar["state"]="normal"
        self.btnBuscar["state"]="normal"
    
    def deseleccionarTree(self):
        seleccion=self.treeProductos.selection()
        if seleccion:
            self.treeProductos.selection_remove(*seleccion)
    
    def cancelar_ventana(self):
        if self.ventana != None:
            self.ventana.destroy()
            self.ventana = None
    #declara variable ventana
    
    def selecEliminar(self):
        self.cancelar_ventana()
        self.ventana = tk.Toplevel()
        self.ventana.title("Confirmacion")
        self.ventana.geometry("300x300")
        self.ventana.minsize(200,150)
        self.ventana.maxsize(300,300)

        self.ventana.rowconfigure((0,2,4,6),weight=2)
        self.ventana.rowconfigure((8,), weight=1)
        self.ventana.columnconfigure((0,2,4),weight=1)
        #advertencia
        #ruta='C:\\Users\\Cardenas Reyes\\Downloads\\Proyecto-OOP-main\\tren-128x64.png'
        #tren = PhotoImage(file=ruta)
        #self.imagen1 = ttk.Label(ventana, image=tren,anchor="center")
        #self.imagen1.pack()   
        boton_confirmar = tk.Button(self.ventana, text="Confirmar", command=self.eliminaRegistro)
        boton_confirmar.grid(row=7, column=1, sticky="news")

        boton_cancelar = tk.Button(self.ventana, text="Cancelar", command= self.cancelar_ventana)
        boton_cancelar.grid(row=7, column=3, sticky="news")
        self.opcion_var = tk.IntVar()  # Variable de control para almacenar el valor seleccionado

        radio_opcion1 = tk.Radiobutton(self.ventana, text="Eliminar proveedor", variable=self.opcion_var, value=1)
        radio_opcion1.grid(row=1, column=1, columnspan=3, sticky="news")

        radio_opcion2 = tk.Radiobutton(self.ventana, text="Eliminar productos seleccionados", variable=self.opcion_var, value=2)
        radio_opcion2.grid(row=3, column=1, columnspan=3, sticky="news")

        radio_opcion3 = tk.Radiobutton(self.ventana, text="Eliminar todos los productos", variable=self.opcion_var, value=3)
        radio_opcion3.grid(row=5, column=1, columnspan=3, sticky="news")

        self.clase = tk.IntVar()

    
    def eliminaRegistro(self):
        '''Elimina un Registro en la BD'''
        idNit = self.idNit.get()

        if self.opcion_var.get() == 1:
            #validaciones----------------------------------------------------------------
            if idNit == "": #Valida que el Entry de IdNit no este vacio 
                mssg.showerror("Eliminacion fallida", "No ha sido proporcionado un IdNit existente")
                self.cancelar_ventana()
                return
            
            consulta = self.run_Query("SELECT * FROM Proveedor WHERE IdNitProv = ?",(idNit,)).fetchall()
            if not consulta: #Valida que exista un proveedor con el IdNit proporcionado
                mssg.showerror("Eliminacion fallida", "No ha sido proporcionado un IdNit valido para eliminar")
                self.cancelar_ventana()
                return

            #Se hace el proceso de eliminacion con sus puntos de confirmacion------------
            valida_Consulta = mssg.askokcancel("Confirmacion",f"Se eliminara el proveedor con el id {idNit} y todos sus productos asociados")
            if valida_Consulta:
                try:
                    self.run_Query("DELETE FROM Productos WHERE IdNit = ? ",(idNit,))
                except:
                    mssg.showerror("Eliminacion Fallida","Ha habido un error al eliminar los productos asociados al Proveedor")
                else:
                    try:
                        self.run_Query("DELETE FROM Proveedor WHERE IdNitProv = ?",(idNit,))
                    except:
                        mssg.showerror("Eliminacion Fallida","Ha habido un error al eliminar el Proveedor")
                    else:
                        mssg.showinfo("Eliminacion Completada",f"Se ha eliminado el Proveedor de IdNit = {idNit} y todos sus productos asociados")
                        self.lee_treeProductos(idNit)
            self.cancelar_ventana()
            
        elif self.opcion_var.get() == 2:
            #validacion------------------------------------------------------------------
            if self.treeProductos.selection() == ():
                mssg.showinfo("Advertencia","Debe seleccionar los elementos que desea eliminar")
                self.cancelar_ventana()
                return
            
            #eliminacion-----------------------------------------------------------------
            query = f"DELETE from Productos WHERE IdNit = ? and (" #inicio del query que se actulizara con cada elemento seleccionado
            mensaje_validacion = f"¿Esta seguro de eliminar los siguientes registros de la base de datos?\n" #mensaje de la ventana emergente que se actulizara con cada elemento seleccionado
            busqueda = self.treeProductos.item(self.treeProductos.selection()[0])['text'] #idNit de los elemento a eliminar, para buscar al final del proceso
            
            #agrega los datos de cada seleccion a las variables que se van a ejecutar
            parametros = []
            for elemento in self.treeProductos.selection():
                codigo = self.treeProductos.item(elemento)['values'][0]
                parametros.append(codigo)
                query += "Codigo = ? or "
                mensaje_validacion += f"IdNit = {busqueda}, Codigo = {codigo}\n"

            query = query[:-4] #limpia el texto del query que se va a ejecutar
            query += ")" #cierra el parentesis donde estan todos los codigos
            valida_Consulta = mssg.askokcancel("Confirmacion",mensaje_validacion) #crea la ventana emergente de validacion

            if valida_Consulta:
                try:
                    self.run_Query(query, (busqueda,*parametros))
                except:
                    mssg.showerror("Eliminacion fallida", "No se pudo eliminar los datos seleccionados de la base de datos")
                else:
                    mssg.showinfo("Eliminacion Terminada","Se han eliminado los productos seleccionados de la base de datos")
                self.lee_treeProductos(busqueda) #Busca y muestra los elementos del idNit restantes despues de la eliminacion
            self.cancelar_ventana()

        elif self.opcion_var.get() == 3:
            #validacion------------------------------------------------------------------
            if idNit == "": #Valida que el Entry de IdNit no este vacio 
                mssg.showerror("Eliminacion fallida", "No ha sido proporcionado un IdNit valido para eliminar")
                self.cancelar_ventana()
                return
            
            consulta = self.run_Query("SELECT * FROM Proveedor WHERE IdNitProv = ?",(idNit,)).fetchall()
            if not consulta: #Valida que exista un proveedor con el IdNit proporcionado
                mssg.showerror("Eliminacion fallida", "No ha sido proporcionado un IdNit existente")
                self.cancelar_ventana()
                return
            #Valida que existan Productos asociados al IdNit proporcionado 
            consulta_Proveedor = self.run_Query("SELECT * FROM Productos WHERE IdNit = ?",(idNit,)).fetchall()
            if not consulta_Proveedor:
                mssg.showerror("Eliminacion Fallida","No existen Productos asociados al Proveedor proporcionado")
                self.cancelar_ventana()
                return
            
            #eliminacion-----------------------------------------------------------------
            #Ejecuta la eliminacion de todos los productos asociados al Proveedor proporcionado, con su respectiva confirmacion
            valida_Consulta = mssg.askokcancel("Confirmacion",f"Se eliminaran {len(consulta_Proveedor)} Productos asociados al Proveedor {idNit}")

            if valida_Consulta:
                try:
                    self.run_Query("DELETE FROM Productos WHERE IdNit = ?",(idNit,))
                except:
                    mssg.showerror("Eliminacion Fallida","No fue posible eliminar los productos")
                else:
                    mssg.showinfo("Eliminacion Terminada",f"Se han eliminado {len(consulta_Proveedor)} Productos de la tabla Productos")
                    self.lee_treeProductos(idNit)
            #sin importar lo que pase cerrar la ventana
            self.cancelar_ventana()

if __name__ == "__main__":
    app = Inventario()
    app.run()