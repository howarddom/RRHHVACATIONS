import os
import shutil

# Ruta del acceso directo que quieres copiar
origen = r'\\192.168.0.15\PUB\AccesoDirectoMapas\15073IT14000776R.xlsx'

# Ruta base donde deseas copiar el acceso directo en cada perfil de usuario
destino_base = r'C:\Users'

# Obtener la lista de perfiles de usuario
perfiles = [perfil for perfil in os.listdir(destino_base) if os.path.isdir(os.path.join(destino_base, perfil))]

# Copiar el acceso directo a cada perfil de usuario
for perfil in perfiles:
    destino = os.path.join(destino_base, perfil, 'Desktop', 'mi_acceso_directo.lnk')    
    try:
        
        shutil.copyfile(origen, destino)
        print(f"Se ha copiado el acceso directo a {destino}")
    except Exception as e:
        print(f"Error al copiar el acceso directo a {destino}: {e}")
