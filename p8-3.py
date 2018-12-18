#! python3
__author__ = 'rls'
__version__ = 0.1
''' Program written by Robin Sharpton
    rest of DocString goes here 
'''

def print_models(unprinted_designs, completed_models):
    '''
    simulate printing each design, until none are left.
    move each design to completed_models after printing.
    :param unprinted_designs:
    :param completed_models:
    :return:
    '''

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # simulate creating a 3D print from the
        print('now printing : {}'.format(current_design))
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """ Show all the models that were printed. """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)