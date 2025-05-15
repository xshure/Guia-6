
# Configuración de parámetros
NUM_PAGES = 4
NUM_FRAMES = 4
PAGE_SIZE = 1024

# Inicialización de la tabla de páginas y la memoria
page_table = [-1] * NUM_PAGES
memory = [None] * NUM_FRAMES

def set_page_frame(page_number, frame_number):
    page_table[page_number] = frame_number

def get_frame(page_number):
    return page_table[page_number]

def load_page(frame_number, page_data):
    memory[frame_number] = page_data

def find_free_frame():
    for i in range(len(memory)):
        if memory[i] is None:
            return i
    return None

def load_process(process_id, pages_needed):
    print(f"\nCargando proceso {process_id} que necesita {pages_needed} páginas")
    for page in range(pages_needed):
        frame = find_free_frame()
        if frame is None:
            print("Memoria llena, no se puede cargar el proceso")
            return
        set_page_frame(page, frame)
        load_page(frame, f"Data de la página {page} del proceso {process_id}")
    print(f"Proceso {process_id} cargado")

def translate_address(logical_address):
    page_number = logical_address // PAGE_SIZE
    offset = logical_address % PAGE_SIZE
    frame_number = get_frame(page_number)
    if frame_number == -1:
        return None
    return frame_number * PAGE_SIZE + offset

def translate_addresses(logical_addresses):
    physical_addresses = []
    for la in logical_addresses:
        pa = translate_address(la)
        physical_addresses.append(pa)
    return physical_addresses

def print_state():
    print(f"Tabla de páginas: {page_table}")
    print(f"Memoria: {memory}")

if __name__ == "__main__":
    load_process(1, 3)
    print_state()

    logical_list = [0, 1024, 2048, 3072]
    print("\nTraducción de direcciones:")
    results = translate_addresses(logical_list)
    for l, p in zip(logical_list, results):
        if p is not None:
            print(f"Lógica: {l} -> Física: {p}")
        else:
            print(f"Lógica: {l} -> Página no cargada")