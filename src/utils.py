import re

def remove_placeholders(text, value):
    placeholders = re.findall(r'\{([^}]+)\}', text)
    
    hasil = text  
    for p in placeholders:
        hasil = hasil.replace(f"{{{p}}}", value)
    
    return hasil

print(remove_placeholders("mewing {target}", "local"))
