# interface.py
import gradio as gr  # Import the Gradio library
from ndvi_calculator import calculate_ndvi  # Import the calculate_ndvi function from the index_calculator module
import earthpy.plot as ep
import cv2

# Define the process_file function that takes two file objects as inputs
def process_file(red_band_file, nir_band_file, visualize_button): 
    red_band_path = red_band_file.name  # Get the file path from the first file object
    nir_band_path = nir_band_file.name  # Get the file path from the second file object
    
    # Calculate NDVI using the calculate_ndvi function
    avg_ndvi, min_ndvi, max_ndvi, ndvi_category = calculate_ndvi(red_band_path, nir_band_path)
    return avg_ndvi, min_ndvi, max_ndvi, ndvi_category # Return the calculated NDVI result

    

# Check if the module is run as the main program
if __name__ == "__main__":
    # Create a Gradio interface
    demo = gr.Interface(
        fn=process_file,  # Use the process_file function for processing inputs
        inputs=[
            gr.inputs.File(label="Red Band TIFF"),
            gr.inputs.File(label="NIR Band TIFF")
            ],  # Define two file input fields
        outputs=[
            gr.Textbox(label="Average NDVI"),  # Label for the Average NDVI output
            gr.Textbox(label="Minimum NDVI"),  # Label for the Minimum NDVI output
            gr.Textbox(label="Maximum NDVI"),  # Label for the Maximum NDVI output
            gr.Textbox(lines = 3, label="Category")   # Label for the NDVI Category output
        ],  # Define the output field type as text
        flagging_options=["Save"], # Change the text of the flag button
        title="Vegetation Mapping Using NDVI"
    )
    
    # Launch the Gradio interface
    demo.launch()