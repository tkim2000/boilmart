-- Users

/*Insert into Users values (NULL,"test1", "123456", 1, 1, "410 Purdue Mall", 47906);*/

-- Companies 

Insert into company values (1, "Walmart Inc", 75.6);
Insert into company values (2, "Kroger Co", 20.5);

-- Stores 

Insert into stores values(1, "Walmart Supercenter", 1, "South Creasy Lane", 47905);
Insert into stores values(2, "Sams Club South St", 1, "South St", 47905);
Insert into stores values(3, "Pay Less ", 2, "Sagamore Pkwy", 47906);

-- Category 

Insert into category values(NULL, "food");
Insert into category values(NULL, "electronics");
Insert into category values(NULL, "household");
Insert into category values(NULL, "pharmaceutical");
Insert into category values(NULL, "auto-products");


-- Items 

Insert into items values(NULL, 1, "banana", 1.95, 1.04, 1, 50);
Insert into items values(NULL, 1, "apple", 0.95, 1.05, 1, 60);
Insert into items values(NULL, 1, "Playstation 5", 500, 3.05, 2, 0);
Insert into items values(NULL, 2, "croisants", 3.94, 1.25, 1, 6);
Insert into items values(NULL, 3, "croisants", 3.94, 1.25, 1, 7);
Insert into items values(NULL, 1, "Paper Towels", 9.5, 3.5, 3, 80);
Insert into items values(NULL, 1, "Febreze", 45, 1.5, 3, 82);
Insert into items values(NULL, 2, "Rapid-Test", 21, 1.5, 4, 20);
Insert into items values(NULL, 2, "Tires", 50, 20, 5, 50);

-- Discounts 

Insert into discounts values(2, "an apple a day", 0.2);
Insert into discounts values(3, "Christmas Sale", 0.5);
Insert into discounts values(9, "Tire Rebate", 0.4);

