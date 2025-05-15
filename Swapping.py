
# Configuración de parámetros
NUM_PAGES = 4
NUM_FRAMES = 2  
PAGE_SIZE = 1024

# Inicialización de la tabla de páginas y la memoria
page_table = [-1] * NUM_PAGES
memory = [None] * NUM_FRAMES
swap_space = {}  # simula el disco para swapping


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

def swap_out():
    for i, data in enumerate(memory):
        if data is not None:
            for page, frame in enumerate(page_table):
                if frame == i:
                    swap_space[page] = memory[i]
                    memory[i] = None
                    page_table[page] = -1
                    print(f"Swapped out página {page} al disco")
                    return i
    return None

def load_process_with_swapping(process_id, pages_needed):
    print(f"\nCargando proceso {process_id} con swapping, necesita {pages_needed} páginas")
    for page in range(pages_needed):
        frame = find_free_frame()
        if frame is None:
            frame = swap_out()
        if frame is None:
            print("No fue posible obtener un marco ni siquiera con swapping")
            return
        set_page_frame(page, frame)
        load_page(frame, f"Data página {page} del proceso {process_id}")
    print(f"Proceso {process_id} cargado")

def print_state():
    print(f"Tabla de páginas: {page_table}")
    print(f"Memoria: {memory}")
    print(f"Swap (disco): {swap_space}")

if __name__ == "__main__":
    load_process_with_swapping(1, 2)
    load_process_with_swapping(2, 2)
    print_state()