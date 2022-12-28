import fitz, os, io
from PIL import Image

def extract_images(input_file:str
                   ,output_path:str
                   ,pages:list=None):
    """
    Extract the images from a PDF file and save them to the output folder
    """
    # Open the PDF
    pdfDoc = fitz.open(input_file)

    # Iterate through the PDF pages
    for pg in range(pdfDoc.pageCount):
        pageID = pg+1
        #If required for specific pages
        if pages:
            if pageID not in pages:
                continue

        #Select a page
        page = pdfDoc[pg]

        #Extract images in the page
        page_images = page.getImageList()

        images_count = 0
        if page_images:
           images_count = len(page_images)
        print(f"Processing page {pageID} -- {images_count} image(s) exist.")

        #Loop throughout the page images
        for img_idx , img in enumerate(page_images,start=1):
            #access the image xref
            img_xref = img[0]
            #extract the image
            img_content = pdfDoc.extractImage(img_xref)
            #Extract the image content
            img_binary = img_content["image"]
            #Extract the image extension
            img_ext = img_content["ext"]
            #Create the output image
            img_out = Image.open(io.BytesIO(img_binary))
            # Output Base File Name
            output_fileName = os.path.join(output_path, os.path.splitext(os.path.basename(input_file))[0])
            # Save the output image
            img_out.save(open(f"{output_fileName}_Page{pageID}_Image{img_idx}.{img_ext}", "wb"))
            img_out.close()
            
    pdfDoc.close()
