# Text detected by Amazon Textract in daily rainfall records

These [images](../RotatedImages) of sample daily rainfall records were processed using Amazon Textract's 'Detect Document Text' API. 

The 'word blocks' detected by Textract in each image are recorded here, with two files for each image:

* a CSV file which lists some details of each detected word block, including: 
  * the unique block ID
  * whether Textract thinks the text is 'Printed' or 'Handwriting'
  * the confidence value (0-100) assigned to the detection by Textract
  * the coordinates on the source image of the top-left corner of the bounding rectangle which contains the detected text
    * coordinates go from (0,0) in the top-left corner of the image to (1,1) in the bottom-right corner
  * the detected text (enclosed in square brackets to prevent Excel doing any auto-formatting of the text when displaying the CSV file)
  
* an image file which draws on the bounding rectangles for all the word blocks:
  * blue rectangles for text detected as 'Handwriting', black for 'Printed'
  * with a thicker border used where the confidence value is 90 or more
	
