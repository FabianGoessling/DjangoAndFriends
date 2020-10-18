from bokeh.layouts import row

from ipyaggrid import Grid
from ipywidgets_bokeh import IPyWidget


def app(doc):
    cars = [
        {'carName': 'Chevelle', 'origin': 'US', 'make': 'Chevrolet', 'price': 30415},
        {'carName': 'Skylark 320', 'origin': 'US', 'make': 'Buick', 'price': 21042},
        {'carName': 'PL411', 'origin': 'Asia', 'make': 'Datsun', 'price': 27676}
    ]

    column_defs = [{'headerName': 'carName', 'field': 'carName', 'rowGroup': True, 'hide': True},
                   {'headerName': 'origin', 'field': 'origin', 'rowGroup': True, 'hide': True},
                   {'headerName': 'make', 'field': 'make'},
                   {'headerName': 'price', 'field': 'price', 'aggFunc': 'avg'},
                   ]

    grid_options = {
        'columnDefs': column_defs,
        'enableSorting': True,
        'enableFilter': True,
        'enableColResize': True,
        'enableRangeSelection': True,
    }

    g = Grid(grid_data=cars,
             grid_options=grid_options,
             quick_filter=True,
             show_toggle_edit=True,
             export_mode="buttons",
             export_csv=True,
             export_excel=True,
             theme='ag-theme-balham',
             show_toggle_delete=True,
             columns_fit='auto',
             index=False,
             keep_multiindex=False)

    # doc = curdoc()
    doc.add_root(row(IPyWidget(widget=g, height=200, width=800)))

# if __name__ == "__main__":
# doc = curdoc()
# app(doc)
