# Trial Processing of Sample Daily Rainfall Records

Various files relating to attempts to process sample images of daily rainfall records.

The images being processed are the samples in [this folder](../Images). Most of them are standard daily rainfall forms from 1870s Anglesey. Details of the standard form layout vary, but the high-level format is essentially:
* a header section providing overall metadata: location info, year, instrument info, observer name, ...
* a table of 12 columns, one per month, and 31 rows, one per month-day, containing the detailed rainfall readings for each day of a specific year
* a 'totals' row, showing total rainfall for each month
* possible a further summary row showing a days-of-rain count for each month

Slightly rotated versions of the images were processed with Amazon Web Service's [Amazon Textract](https://aws.amazon.com/textract/) machine-learning text extraction service.

|Folder|Contents|
|:---|:-------|
|../Images|The source images|
|RotatedImages|The source images with slight rotations applied to try to make the column alignment as vertical as possible.|
|AmazonTextract-DetectedText|What Amazon Textract found in the images, as<br/>i) a CSV file listing the 'word blocks' found <br/>ii) an image showing where word blocks come from.|

