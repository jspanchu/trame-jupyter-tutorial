import magpylib as magpy
import numpy as np

from vtkmodules.vtkCommonCore import vtkIdList
from vtkmodules.vtkCommonDataModel import vtkDataObjectTreeIterator
from vtkmodules.vtkFiltersExtraction import vtkExtractBlockUsingDataAssembly
from vtkmodules.util.numpy_support import numpy_to_vtk, vtk_to_numpy
from vtkmodules.util.data_model import *


def build_magnetic_coils(mesh, current=1000):

    magpy_coils = magpy.Collection()

    # Extract blocks under the "coils" node.
    coil_extractor = vtkExtractBlockUsingDataAssembly(assembly_name="Assembly", selector="//coils", input_data=mesh)
    coil_extractor.Update()

    # Build a magpy current source for every coil.
    coil_iter = vtkDataObjectTreeIterator(data_set=coil_extractor.output)
    coil_iter.visit_only_leaves = True
    coil_iter.InitTraversal()
    while not coil_iter.IsDoneWithTraversal():
        line = vtkIdList()
        coil = coil_iter.current_data_object
        coil.lines.InitTraversal()
        while (coil.lines.GetNextCell(line)):
            vertices = [coil.points[line.GetId(i)] for i in range(line.GetNumberOfIds())]
            magpy_coils.add(magpy.current.Polyline(vertices=vertices, current=current))
        coil_iter.GoToNextItem()

    return magpy_coils

if __name__ == "__main__":
    from build_reactor import Builder
    builder = Builder()
    builder.build()
    coils = build_magnetic_coils(builder.mesh)
    print(len(coils))