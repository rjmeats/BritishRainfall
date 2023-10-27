## Table Cells and Words identified by Amazon Textract within images of Rainfall Sheets

Using Textract in 'Analyze Document' mode to detect Table features as well as text.

* [DR_Anglesey_1871-1880C_p002](DR_Anglesey_1871-1880C_p002.rot.textract-analysis.image_map.html)
* [DR_Anglesey_1871-1880C_p005](DR_Anglesey_1871-1880C_p005.rot.textract-analysis.image_map.html)
* [DR_Anglesey_1871-1880C_p008](DR_Anglesey_1871-1880C_p008.rot.textract-analysis.image_map.html)
* [DR_Anglesey_1871-1880C_p017](DR_Anglesey_1871-1880C_p017.rot.textract-analysis.image_map.html)
* [DR_Anglesey_1871-1880C_p020](DR_Anglesey_1871-1880C_p020.rot.textract-analysis.image_map.html)


Blue and black rectangles on the images show the bounding boxes for each 'Word' identified by Amazon Textract. Click within a rectangle to see a pop-up showing the text which Amazon Textract detected. 

Yellow rectangles show the bounding boxes for table cells. Click within a rectangle to see a pop-up identifying the row/oolumn of the cell, and the text of the 'Words' associated with the cell. 

(You can close the pop-ups with the 'Esc' key as well as by pressing the OK button.)

A couple of cases where the Table detection hasn't worked properly for determining the rows in the table:

* [DR_Anglesey_1871-1880C_p004](DR_Anglesey_1871-1880C_p004.rot.textract-analysis.image_map.html) - the rows determined by Textract gradually get out of alignment with the actual rows of figures in the image
* [DR_Anglesey_1871-1880C_p011](DR_Anglesey_1871-1880C_p011.rot.textract-analysis.image_map.html) - the rows for Days 25, 26 and 27 are detected as just a single row by Textract, perhaps because quite a lot of the cells 
in these rows are blank ? However, for a very similar image of the same sheet, [DR_Anglesey_1871-1880C_p010](DR_Anglesey_1871-1880C_p010.rot.textract-analysis.image_map.html), Textract has found the rows correctly.
