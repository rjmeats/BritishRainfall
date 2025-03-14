# Quick JPEG compression Experiments

Experiments to assess JPEG file compression:
* using a Python program to invoke the Pillow image-processing library
* JPEG files for three example rainfall sheets (from the Isle of May location) were compressed
* using a range of compression quality values between 1 and 90
* the *jpg_output* folder holds the compressed jpg files produced, with the quality value used included in the file name
* the size reductions achieved (taken from *results.txt*) are listed below

```
Running jpg compression tests using source jpg file TYRain_1677-1886_B_pt2-page-147.jpg

TYRain_1677-1886_B_pt2-page-147.jpg : q =  1 :  719277 bytes =>   24600 bytes : 3 %
TYRain_1677-1886_B_pt2-page-147.jpg : q =  2 :  719277 bytes =>   24626 bytes : 3 %
TYRain_1677-1886_B_pt2-page-147.jpg : q =  5 :  719277 bytes =>   32322 bytes : 4 %
TYRain_1677-1886_B_pt2-page-147.jpg : q = 10 :  719277 bytes =>   45066 bytes : 6 %
TYRain_1677-1886_B_pt2-page-147.jpg : q = 20 :  719277 bytes =>   74045 bytes : 10 %
TYRain_1677-1886_B_pt2-page-147.jpg : q = 30 :  719277 bytes =>  109736 bytes : 15 %
TYRain_1677-1886_B_pt2-page-147.jpg : q = 40 :  719277 bytes =>  145350 bytes : 20 %
TYRain_1677-1886_B_pt2-page-147.jpg : q = 50 :  719277 bytes =>  182935 bytes : 25 %
TYRain_1677-1886_B_pt2-page-147.jpg : q = 60 :  719277 bytes =>  215666 bytes : 30 %
TYRain_1677-1886_B_pt2-page-147.jpg : q = 70 :  719277 bytes =>  299512 bytes : 42 %
TYRain_1677-1886_B_pt2-page-147.jpg : q = 80 :  719277 bytes =>  358234 bytes : 50 %
TYRain_1677-1886_B_pt2-page-147.jpg : q = 90 :  719277 bytes =>  637901 bytes : 89 %

Running jpg compression tests using source jpg file TYRain_1900-1909_29_pt1-page-038.jpg

TYRain_1900-1909_29_pt1-page-038.jpg : q =  1 :  984025 bytes =>   33600 bytes : 3 %
TYRain_1900-1909_29_pt1-page-038.jpg : q =  2 :  984025 bytes =>   33639 bytes : 3 %
TYRain_1900-1909_29_pt1-page-038.jpg : q =  5 :  984025 bytes =>   47965 bytes : 5 %
TYRain_1900-1909_29_pt1-page-038.jpg : q = 10 :  984025 bytes =>   71545 bytes : 7 %
TYRain_1900-1909_29_pt1-page-038.jpg : q = 20 :  984025 bytes =>  114401 bytes : 12 %
TYRain_1900-1909_29_pt1-page-038.jpg : q = 30 :  984025 bytes =>  166536 bytes : 17 %
TYRain_1900-1909_29_pt1-page-038.jpg : q = 40 :  984025 bytes =>  215151 bytes : 22 %
TYRain_1900-1909_29_pt1-page-038.jpg : q = 50 :  984025 bytes =>  262481 bytes : 27 %
TYRain_1900-1909_29_pt1-page-038.jpg : q = 60 :  984025 bytes =>  306342 bytes : 31 %
TYRain_1900-1909_29_pt1-page-038.jpg : q = 70 :  984025 bytes =>  414376 bytes : 42 %
TYRain_1900-1909_29_pt1-page-038.jpg : q = 80 :  984025 bytes =>  487165 bytes : 50 %
TYRain_1900-1909_29_pt1-page-038.jpg : q = 90 :  984025 bytes =>  846950 bytes : 86 %

Running jpg compression tests using source jpg file TYRain_1951-1960_28_pt1-page-041.jpg

TYRain_1951-1960_28_pt1-page-041.jpg : q =  1 :  792512 bytes =>   48582 bytes : 6 %
TYRain_1951-1960_28_pt1-page-041.jpg : q =  2 :  792512 bytes =>   48661 bytes : 6 %
TYRain_1951-1960_28_pt1-page-041.jpg : q =  5 :  792512 bytes =>   68589 bytes : 9 %
TYRain_1951-1960_28_pt1-page-041.jpg : q = 10 :  792512 bytes =>  101457 bytes : 13 %
TYRain_1951-1960_28_pt1-page-041.jpg : q = 20 :  792512 bytes =>  148203 bytes : 19 %
TYRain_1951-1960_28_pt1-page-041.jpg : q = 30 :  792512 bytes =>  186887 bytes : 24 %
TYRain_1951-1960_28_pt1-page-041.jpg : q = 40 :  792512 bytes =>  219916 bytes : 28 %
TYRain_1951-1960_28_pt1-page-041.jpg : q = 50 :  792512 bytes =>  248279 bytes : 31 %
TYRain_1951-1960_28_pt1-page-041.jpg : q = 60 :  792512 bytes =>  282498 bytes : 36 %
TYRain_1951-1960_28_pt1-page-041.jpg : q = 70 :  792512 bytes =>  343902 bytes : 43 %
TYRain_1951-1960_28_pt1-page-041.jpg : q = 80 :  792512 bytes =>  404354 bytes : 51 %
TYRain_1951-1960_28_pt1-page-041.jpg : q = 90 :  792512 bytes =>  621687 bytes : 78 %
```
