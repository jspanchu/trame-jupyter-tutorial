# Utility function to save simulation input/output datasets to filesystem
from vtkmodules.vtkIOXML import vtkXMLImageDataWriter, vtkXMLPolyDataWriter
from vtkmodules.vtkIOParallelXML import vtkXMLPartitionedDataSetCollectionWriter

def save_dataset(dataset, file_name):
    if file_name.endswith(".vti"):
        writer = vtkXMLImageDataWriter()
    elif file_name.endswith(".vtp"):
        writer = vtkXMLPolyDataWriter()
    elif file_name.endswith(".vtpc"):
        writer = vtkXMLPartitionedDataSetCollectionWriter()
    writer.input_data_object = dataset
    writer.file_name = file_name
    writer.Write()
