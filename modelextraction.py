import os
from unstructured.partition.pdf import partition_pdf
from unstructured.staging.base import elements_to_json

filename = "./Cable Data/LV Cable1.pdf" # For this notebook I uploaded Nvidia's earnings into the Files directory called "/content/"
output_dir = "./"

# Define parameters for Unstructured's library
strategy = "hi_res" # Strategy for analyzing PDFs and extracting table structure
model_name = "yolox" # Best model for table extraction. Other options are detectron2_onnx and chipper depending on file layout

# Extracts the elements from the PDF
elements = partition_pdf(
filename=filename, 
strategy=strategy, 
infer_table_structure=True, 
model_name=model_name
)

# Store results in json
elements_to_json(elements, filename=f"{filename}.json") # Takes a while for file to show up on the Google Colab
import os
from unstructured.partition.pdf import partition_pdf
from unstructured.staging.base import elements_to_json

filename = "/Path/To/Your/File" # For this notebook I uploaded Nvidia's earnings into the Files directory called "/content/"
output_dir = "/Path/To/Your/Desired/Output"

# Define parameters for Unstructured's library
strategy = "hi_res" # Strategy for analyzing PDFs and extracting table structure
model_name = "yolox" # Best model for table extraction. Other options are detectron2_onnx and chipper depending on file layout

# Extracts the elements from the PDF
elements = partition_pdf(
filename=filename, 
strategy=strategy, 
infer_table_structure=True, 
model_name=model_name
)

# Store results in json
elements_to_json(elements, filename=f"{filename}.json") # Takes a while for file to show up on the Google Colab
