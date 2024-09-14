import aspose.pdf as ap

# Load PDF file
compressPdfDocument = ap.Document("KNYMergedSection1-2.pdf")

# Create an object of OptimizationOptions class
pdfOptimizeOptions = ap.optimization.OptimizationOptions()

# Enable image compression
pdfOptimizeOptions.image_compression_options.compress_images = True

# Set the image quality
pdfOptimizeOptions.image_compression_options.image_quality = 50

# Compress PDF
compressPdfDocument.optimize_resources(pdfOptimizeOptions)

# Save the compressed PDF
compressPdfDocument.save("KNY1-2compressed.pdf")