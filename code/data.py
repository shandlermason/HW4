# class Data:
#     """Data is holder of rows and their summaries"""
#     def __init__(self, src):
#         self.cols = None
#         self.rows = {}
#         if type(src)==str:
#             csv(src, self.add(row))
#         else:
#             for _, row in (src or {}):
#                 self.add(row)

#     def add(self, xs, row):
#         if not self.cols:
#             self.cols = Cols(xs)
#         else:
#             row = push(self.rows, cs.cells and xs or Row(xs))
#             for _, col in todo:
#                 col.add(row.cells[col.at])

#     def stats(self, places, showCols, fun, t, v):
#         showCols, fun = showCols or self.cols.y, fun or "mid"
#         t = {}
#         for _, col in showCols:
#             v = fun(col)
#             v = type(v) == float and rnd(v, places) or v
#             t[col.name] = v
#         return t 
        