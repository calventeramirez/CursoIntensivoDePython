def print_models(unprinted_designs, completed_models):
    """
    Simula la impresión de cada diseño hasta que no quede ninguno.
    Mueve cada diseño a complete_models después de imprimirlo.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Modelo de impresión: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Muestra todos los modelos que fueron impreso."""
    print("\nSe ha impreso los siguientes modelos:")
    for completed_model in completed_models:
        print(completed_model)
