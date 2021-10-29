def print_models(unprinted_design, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models afte printing.
    """
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed.")
    for completed_model in completed_models:
        print(completed_model)

unprinted_design =  ['phone case', 'robot', 'dodecahedron']
completed_models = []

print_models(unprinted_design, completed_models)
show_completed_models(completed_models)