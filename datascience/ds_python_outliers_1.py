# removing outliers
# if value is greater than (mean - 2* standard deviation) OR
# less than (mean + 2* standard deviation)

>>> import numpy

>>> arr = [10, 386, 479, 627, 20, 523, 482, 483, 542, 699, 535, 617, 577, 
           471, 615, 583, 441, 562, 563, 527, 453, 530, 433, 541, 585, 704, 
           443, 569, 430, 637, 331, 511, 552, 496, 484, 566, 554, 472, 335, 
           440, 579, 341, 545, 615, 548, 604, 439, 556, 442, 461, 624, 611, 
           444, 578, 405, 487, 490, 496, 398, 512, 422, 455, 449, 432, 607, 
           679, 434, 597, 639, 565, 415, 486, 668, 414, 665, 763, 557, 304, 
           404, 454, 689, 610, 483, 441, 657, 590, 492, 476, 437, 483, 529, 
           363, 711, 543]

>>> elements = numpy.array(arr)
[ 10 386 479 627  20 523 482 483 542 699 535 617 577 471 615 583 441 562
 563 527 453 530 433 541 585 704 443 569 430 637 331 511 552 496 484 566
 554 472 335 440 579 341 545 615 548 604 439 556 442 461 624 611 444 578
 405 487 490 496 398 512 422 455 449 432 607 679 434 597 639 565 415 486
 668 414 665 763 557 304 404 454 689 610 483 441 657 590 492 476 437 483
 529 363 711 543]
 
 >>> elements.shape
 (94,)
 
>>> mean = numpy.mean(elements, axis=0)
509.531914893617

>>> sd = numpy.std(elements, axis=0)
118.51857760182034

>>> final_list = [x for x in arr if (x > mean - 2 * sd)]
>>> final_list = [x for x in final_list if (x < mean + 2 * sd)]
[386, 479, 627, 523, 482, 483, 542, 699, 535, 617, 577, 471, 615, 583, 441, 562, 563, 527,
 453, 530, 433, 541, 585, 704, 443, 569, 430, 637, 331, 511, 552, 496, 484, 566, 554, 472,
 335, 440, 579, 341, 545, 615, 548, 604, 439, 556, 442, 461, 624, 611, 444, 578, 405, 487,
 490, 496, 398, 512, 422, 455, 449, 432, 607, 679, 434, 597, 639, 565, 415, 486, 668, 414,
 665, 557, 304, 404, 454, 689, 610, 483, 441, 657, 590, 492, 476, 437, 483, 529, 363, 711,
 543]

>>> elements = numpy.array(final_list)
>>> elements.shape
 (91,)

>>> list(set(arr) - set(final_list))
[10, 763, 20]

# 3 outliers has been removed (10, 20 and 763)
# As an astute commenter on CrossValidated put it: “Sometimes outliers are bad data, and should be excluded, such as typos. 
# Sometimes they are Wayne Gretzky or Michael Jordan, and should be kept.” 
# Domain knowledge and practical wisdom are the only ways to tell the difference.
