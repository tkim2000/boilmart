
CREATE TABLE stores(
  store_id integer PRIMARY KEY,
  store_name varchar(50),
  company_id integer,
  address varchar(50),
  zipcode integer
); 

-- changed to autoincrement
CREATE TABLE items( 
  item_id integer Not NULL AUTO_INCREMENT,
  store_id integer,
  name varchar(50),
  price decimal(10,2),
  weight decimal(5,2),
  category varchar(50),
  stock integer,
  PRIMARY KEY (item_id)
);

CREATE TABLE discounts(
  item_id integer,
  sale_name varchar(50),
  percentage decimal(2,2)
); 

CREATE TABLE company(
  company_id integer,
  name text,
  sales integer,
  PRIMARY KEY (company_id)
);

CREATE TABLE category(
  category_id integer Not NULL AUTO_INCREMENT,
  name text,
  PRIMARY Key (category_id)
);

CREATE TABLE reviews(
  review_id integer Not NULL AUTO_INCREMENT,
  store_name text,
  content text,
  rating integer,
  PRIMARY Key(review_id)
);
/*CREATE TABLE Users(
  User_id integer NOT NULL AUTO_INCREMENT,
  Username varchar(50),
  Password text,
  Last_Frequented_Store int, 
  Last_Item int,
  address text,
  zipcode integer,
  PRIMARY Key (User_id)
);*/

