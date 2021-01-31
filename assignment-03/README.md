## Assignment 3
### For Loops

Create a program that calculates the number of days between two dates.  You program should prompt the user to enter 2 dates as shown in the attachment in a loop.

It will be helpful if you break down the problem into smaller problems:

1.  define a function that computes if a year is leap year or not. 
    (leap year logic:  https://keisan.casio.com/exec/system/1532572418)
    `def is_leap_year(year)`
2.  define a function that computes the number of days in a month of a year (hint: use a list to store days of the month)
    `def get_num_of_days_in_month(year, month)`
3.  define a function that computes the remainder of the days in a specified month of a year, incorporate previous function(s)
    `def get_remainder_of_days_in_month(year, month, day)`
4.  define a function that computes the number of days in a year, incorporate previous function(s)
    `def get_num_of_days_in_year(year)`
5. define a function that computes the remainder of the days in the year, incorporate previous function(s)
   `def get_remainder_of_days_in_year(year, month, day)`
6. define function that computes the previous days of the year, incorporate previous function(s)
   `def get_past_days_in_year(year, month, day)`
7. define the final function, that incorporate previous function(s) to accomplish the final task of calculating the number of days between two dates
    `def calc_num_of_days_in_between(from_year, from_month, from_day, to_year, to_month, to_day)`

### Visual Representation of possible solution

![algorithm visualization](images/algo.png)

### User interaction

![screenshot](images/screenshot.png)