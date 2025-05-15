
NUM_PAGES = 4
NUM_FRAMES = 4
PAGE_SIZE = 1024

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
    print(f"Proceso {process_id} cargado en memoria")

def print_state():
    print(f"Tabla de páginas: {page_table}")
    print(f"Memoria: {memory}")

# Ejecución principal
if __name__ == "__main__":
    load_process(1, 2)
    load_process(2, 1)
    load_process(3, 2)  # Este debería fallar porque no hay marcos suficientes
    print_state()