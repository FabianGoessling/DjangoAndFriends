import numpy as np
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure


def app(doc):
    bk_plot = figure(
        toolbar_location=None, width=200, height=200,
        x_range=(-1, 5), y_range=(-1, 1),
        x_axis_location=None, y_axis_location=None,
    )
    source = ColumnDataSource(data=dict(
        x=[0, 2, 4],
        angles=[0, 0, 0],
        colors=["red", "green", "blue"],
    ))
    bk_plot.annular_wedge("x", 0, 0, 0.9, 0, dict(field="angles", units="deg"), fill_color="colors", line_color=None,
                          source=source)

    x, y, z = np.random.random((3, 1000))

    bk_x = Slider(start=0, end=360, value=0, step=1, title="x")
    bk_y = Slider(start=0, end=360, value=0, step=1, title="y")
    bk_z = Slider(start=0, end=360, value=0, step=1, title="z", name='test')
    bk_vbox = column([bk_x, bk_y, bk_z])

    def change_bk_x(_attr, _old, new):
        source.patch(dict(angles=[(0, new)]))

    def change_bk_y(_attr, _old, new):
        source.patch(dict(angles=[(1, new)]))

    def change_bk_z(_attr, _old, new):
        source.patch(dict(angles=[(2, new)]))

    bk_x.on_change("value", change_bk_x)
    bk_y.on_change("value", change_bk_y)
    bk_z.on_change("value", change_bk_z)

    bk_hbox = row([bk_vbox, bk_plot], sizing_mode="stretch_both")

    # doc = curdoc()
    doc.add_root(bk_hbox)
