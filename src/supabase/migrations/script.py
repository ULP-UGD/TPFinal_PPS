import re

# Configuración de archivos
input_file = 'C:/Programacion/UGD/PPS/PPS/TPFinal_PPS/supabase/migrations/Localidades_argentinas_Mysql.sql'
output_file = 'C:/Programacion/UGD/PPS/PPS/TPFinal_PPS/supabase/migrations/insert_localidades.sql'

# Leer el archivo completo
with open(input_file, 'r', encoding='utf-8') as file:
    data = file.read()

# Patrón mejorado para encontrar todas las sentencias INSERT
pattern = r'INSERT INTO\s+(?:`)?localidad(?:`)?\s*\(([^)]+)\)\s*VALUES\s*((?:\([^)]+\)(?:,\s*)?)+);'
matches = re.findall(pattern, data, re.IGNORECASE | re.MULTILINE)

if not matches:
    print("No se encontraron sentencias INSERT INTO localidad.")
    exit()

all_records = []

for columns_part, values_part in matches:
    # Obtener nombres de columnas
    columns = [col.strip().strip('`') for col in columns_part.split(',')]
    
    # Procesar todos los valores
    raw_values = values_part.strip()
    records = []
    
    # Dividir registros manteniendo la integridad
    current_record = []
    in_quotes = False
    buffer = ""
    
    for char in raw_values:
        if char == "'":
            in_quotes = not in_quotes
            buffer += char
        elif char == "(" and not in_quotes:
            if buffer.strip():
                current_record.append(buffer.strip())
            buffer = ""
        elif char == ")" and not in_quotes:
            if buffer.strip():
                current_record.append(buffer.strip())
            if current_record:
                records.append(current_record)
            current_record = []
            buffer = ""
        elif char == "," and not in_quotes:
            if buffer.strip():
                current_record.append(buffer.strip())
            buffer = ""
        else:
            buffer += char
    
    # Procesar cada registro
    for record in records:
        if len(record) != len(columns):
            continue
            
        field_map = dict(zip(columns, record))
        
        provincia_id = field_map.get('provincia_id', '').strip("'")
        nombre = field_map.get('nombre', '').strip("'")
        codigopostal = field_map.get('codigopostal', '').strip("'")
        
        if provincia_id and nombre and codigopostal:
            all_records.append(f"({provincia_id},'{nombre}','{codigopostal}')")

# Generar el archivo de salida
with open(output_file, 'w', encoding='utf-8') as file:
    file.write("INSERT INTO localidad (provincia_id, nombre, codigopostal) VALUES\n")
    file.write(",\n".join(all_records) + ";")

print(f"Se procesaron {len(all_records)} localidades y se guardaron en {output_file}")