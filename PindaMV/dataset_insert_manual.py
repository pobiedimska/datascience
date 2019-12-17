from PindaMV.dataset_structure import dataset


def add_row(latin, year, wire, inf):
    dataset.update({latin: {'cen_year': year, 'wire_other': wire, 'inf_other': inf}})
    return dataset


new_ds = add_row('FRAXINUS PENNSYLVANICA', 2006, 'No', 'No')

print(new_ds)
