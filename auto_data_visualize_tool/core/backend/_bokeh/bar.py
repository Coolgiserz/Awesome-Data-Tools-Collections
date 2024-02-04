# @Author: weirdgiser
# @Time: 2024/2/1
# @Function:
from bokeh.plotting import figure, show
from bokeh.io import export_png

class BaseBarProxy:
    def __init__(self, x_labels, y_data, x_data=None, save_file=True):
        self.x_data = x_data
        self.y_data = y_data
        self.x_labels = x_labels
        self.save_file = save_file

    def vbar(self, height=400, title=None, x_axis_label="x", y_axis_label="y", output_filename=None):
        p = figure(x_range=self.x_labels,
                   height=height,
                   title=title,
                   toolbar_location=None, tools="")

        p.vbar(x=self.x_labels, top=self.y_data, width=0.9)
        p.xaxis.axis_label = x_axis_label
        p.yaxis.axis_label = y_axis_label

        p.xgrid.grid_line_color = None
        p.y_range.start = 0

        # show(p)
        if self.save_file:
            if output_filename is None:
                pass
            else:
                export_png(p, filename=output_filename)
                print(f"Saving {output_filename}")
