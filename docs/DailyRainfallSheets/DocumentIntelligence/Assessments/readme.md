## Assessment of readings extracted using Azure AI Document Intelligence

* [DR_Anglesey_1871-1880C_p008](DR_Anglesey_1871-1880C_p008.image_map.html)

Clickable images for a few sample daily rainfall sheets comparing manually transcribed daily readings with the readings text extracted by Azure AI Document Intelligence from the images. 

Where an exact comparison fails, a comparison using predefined adjustments to the extracted text was tried, including:
* adding/relocating the decimal point to a readings
* substituting letters for similar digits e.g. replacing letter 'b' with a digit '6'

Click on each daily reading cell in an image to see details of the extracted text, manual transcription and adjustments needed to make a match. Cell borders are coloured by status:

* green - the unmodified extracted text matches the manual transcription
* pale blue - the raw extracted text does not match the manual transcription, but an adjusted form does match
* yellow - where a 'long dash' appears on the sheet to indicate 'no rainfall' for a day, this is missed in the extracted text
* orange - a reading other than a long dash is missed in the extracted text
* red - the extracted text does not match the manual transcription, even after trying adjustments

Summary counts of each of the above classifications are shown at the top of each image.