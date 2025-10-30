-- DATABASE CREATION
CREATE DATABASE covid_business_analysis;
USE covid_business_analysis;

-- REGION TABLE
CREATE TABLE region (
  region_id INT,
  region_name VARCHAR(50),
  country VARCHAR(50),
  manager_name VARCHAR(100),
  population VARCHAR(50),
  avg_income VARCHAR(50),
  stores_count VARCHAR(50),
  established_year VARCHAR(10)
);

INSERT INTO region VALUES
(1, 'north', 'india', 'Rajesh Kumar', '12,000,000', '35,000', '22', '2010'),
(2, 'South', 'INDIA', 'Priya Menon', '9.5M', '37000', '18', '2011'),
(3, 'east', 'India', ' Anil  Das  ', '8,200,000', 'thirty-two thousand', '15', '2012'),
(4, 'WEST', 'india', 'Sneha  Patel', '10,300,000', '36000', 'twenty', '2009'),
(4, 'west', 'India', 'Sneha Patel', '10,300,000', '36000', '20', '2009'), -- duplicate
(5, 'N0rth', 'India', 'Rajesh Kumar', '11,800,000', '34000', '21', '2013'),
(6, 'South', 'indai', NULL, '9,600,000', '37000', '18', '2011');

select * from region;

set sql_safe_updates=0;
delete from region where stores_count='twenty';
update region set region_name='North' where lower(region_name)in('north','N0rth');
update region set region_name='East' where lower(region_name)in('east');
update region set region_name='West' where lower(region_name)in('west');
update region set country='India' where lower(country)in('INDIA','India','indai','india');

update region set manager_name='no manager' where manager_name is null;
update region set avg_income='32000' where avg_income='thirty-two thousand';
update region set population='95,00,000' where population='9.5M';
desc region;

UPDATE region
SET population = REPLACE(population, ',', ''),
    avg_income = REPLACE(avg_income, ',', '');

ALTER TABLE region
MODIFY COLUMN population INT,
MODIFY COLUMN avg_income INT,
MODIFY COLUMN stores_count INT,
MODIFY COLUMN established_year INT;












-- PRODUCT CATEGORY TABLE
CREATE TABLE product_category (
  category_id INT,
  category_name VARCHAR(50),
  avg_price VARCHAR(50),
  supplier VARCHAR(100),
  rating VARCHAR(50),
  return_rate VARCHAR(50),
  online_available VARCHAR(20),
  warranty_years VARCHAR(10)
);

INSERT INTO product_category VALUES
(1, 'electronics', '25,000', 'L.G', '4.6', '2.5', 'yes', '2'),
(2, 'clothng', '3,500', 'Reliance Trendz', '4.2', '3', 'y', '0'),
(3, 'groceries', 'eight hundred', 'Big Basket', '4.5', '1.5%', 'TRUE', '0'),
(4, 'furniture', '12000.00', 'IKEA', '4.3', '02', 'Yes', '3'),
(5, 'sports', '6k', 'Decathalon', '4.7', '1.2', 'YES', '1'),
(6, 'Beauty', '1500', 'Nyka', 'four point four', '2.8', 'yes', ''),
(7, 'electronics', '25000', 'LG', '4.6', '2.5', 'yes', '2'); -- duplicate

select * from product_category;
desc product_category;
-- Remove duplicate rows
DELETE FROM product_category
WHERE category_id NOT IN (
  SELECT MIN(category_id)
  FROM (SELECT * FROM product_category) AS temp
  GROUP BY LOWER(category_name)
);
UPDATE product_category SET avg_price='800' WHERE LOWER(avg_price) LIKE '%eight hundred%';
UPDATE product_category SET avg_price='6000' WHERE LOWER(avg_price) LIKE '%6k%';
UPDATE product_category SET avg_price=REPLACE(avg_price, ',', '');

-- Fix category spelling
UPDATE product_category
SET category_name = 'Clothing'
WHERE LOWER(category_name) IN ('clothng');

-- Convert avg_price to numbers
UPDATE product_category SET avg_price = '800' WHERE avg_price = 'eight hundred';
UPDATE product_category SET avg_price = '6000' WHERE avg_price = '6k';
UPDATE product_category
SET avg_price = REPLACE(avg_price, ',', '');
-- Convert rating text to number
UPDATE product_category SET rating = '4.4' WHERE rating = 'four point four';

-- Normalize online_available values
UPDATE product_category
SET online_available = 'Yes'
WHERE LOWER(online_available) IN ('y', 'true', 'yes');

-- Fill blank warranty_years with 0
UPDATE product_category
SET warranty_years = '0'
WHERE warranty_years = '' OR warranty_years IS NULL;

-- Remove commas and convert datatypes
UPDATE product_category
SET avg_price = REPLACE(avg_price, ',', ''),
    return_rate = REPLACE(return_rate, '%', '');

ALTER TABLE product_category
MODIFY COLUMN avg_price INT,
MODIFY COLUMN rating DECIMAL(3,1),
MODIFY COLUMN return_rate DECIMAL(4,2),
MODIFY COLUMN warranty_years INT;

















-- TIME PERIOD TABLE
CREATE TABLE time_period (
  time_id INT,
  year VARCHAR(10),
  month VARCHAR(20),
  quarter VARCHAR(10),
  lockdown_phase VARCHAR(20),
  covid_wave VARCHAR(20),
  working_days VARCHAR(20),
  holidays VARCHAR(20)
);

INSERT INTO time_period VALUES
(1, '2019', 'jan', 'q1', 'none', '0', '26', '5'),
(2, '2019', 'feb', 'Q1', '-', '0', '24', '4'),
(3, '2019', 'march', '', '', '0', '25', 'six'),
(4, '2020', 'jan', 'Q1', 'none', 'none', '25', '6'),
(5, '2020', 'Mar', 'phase-1', '1st', '10', '21', ''),
(6, '2020', 'may', 'q2', 'phase2', '1', 'fifteen', 'sixteen'),
(7, '2020', 'sept', 'Q3', 'Unlock', '1', '22', 'eight'),
(8, '2021', 'jan', 'Q1', '', '2', '25', '6'),
(9, '2021', 'apr', 'Q2', 'lockdown', 'wave2', '12', '19'),
(10, '2021', 'october', 'Q4', 'None', '2', '25', '6'),
(11, '2022', 'mar', 'Q1', 'none', '3', '26', '5'),
(12, '2022', 'Sept', 'q3', 'none', '3', '25', '5'),
(13, '2022', 'dec', 'Q4', 'none', '3', '25', NULL);

select * from time_period;

UPDATE time_period SET month='January'   WHERE LOWER(month) IN ('jan');
UPDATE time_period SET month='February'  WHERE LOWER(month) IN ('feb');
UPDATE time_period SET month='March'     WHERE LOWER(month) IN ('mar','march');
UPDATE time_period SET month='May'       WHERE LOWER(month)='may';
UPDATE time_period SET month='September' WHERE LOWER(month) IN ('sept');
UPDATE time_period SET month='April'     WHERE LOWER(month)='apr';
UPDATE time_period SET month='October'   WHERE LOWER(month)='october';
UPDATE time_period SET month='December'  WHERE LOWER(month)='dec';

UPDATE time_period SET quarter='Q1' WHERE LOWER(quarter) LIKE 'q1%';
UPDATE time_period SET quarter='Q2' WHERE LOWER(quarter) LIKE 'q2%';
UPDATE time_period SET quarter='Q3' WHERE LOWER(quarter) LIKE 'q3%';
UPDATE time_period SET quarter='Q4' WHERE LOWER(quarter) LIKE 'q4%';

UPDATE time_period SET lockdown_phase='None' WHERE lockdown_phase IN ('', '-', 'none', 'unlock');
UPDATE time_period SET covid_wave='0' WHERE covid_wave IN ('none', '', '0');
UPDATE time_period SET covid_wave='1' WHERE covid_wave LIKE '%1%';
UPDATE time_period SET covid_wave='2' WHERE covid_wave LIKE '%2%';
UPDATE time_period SET covid_wave='3' WHERE covid_wave LIKE '%3%';

UPDATE time_period SET working_days='15' WHERE LOWER(working_days)='fifteen';
UPDATE time_period SET working_days='10' WHERE LOWER(working_days)='ten';
UPDATE time_period SET working_days='21' WHERE LOWER(working_days)='twenty-one';
UPDATE time_period SET working_days='22' WHERE LOWER(working_days)='twenty-two';
UPDATE time_period SET holidays='6' WHERE LOWER(holidays)='six';
UPDATE time_period SET holidays='8' WHERE LOWER(holidays)='eight';
UPDATE time_period SET holidays='16' WHERE LOWER(holidays)='sixteen';
UPDATE time_period SET holidays='5' WHERE LOWER(holidays)='' OR holidays IS NULL;

UPDATE time_period
SET working_days = REPLACE(working_days, ',', ''),
    holidays = REPLACE(holidays, ',', '');

ALTER TABLE time_period
MODIFY COLUMN year INT,
MODIFY COLUMN covid_wave INT,
MODIFY COLUMN working_days INT,
MODIFY COLUMN holidays INT;

UPDATE time_period SET quarter='Q1' WHERE year=2019 AND month='March';
UPDATE time_period SET quarter='Q1' WHERE year=2020 AND month='March';

UPDATE time_period SET lockdown_phase='phase1' WHERE year=2020 AND month='March';











-- SALES FACT TABLE
CREATE TABLE sales_fact (
  sale_id INT,
  time_id INT,
  region_id INT,
  category_id INT,
  sales_revenue VARCHAR(50),
  expense VARCHAR(50),
  profit VARCHAR(50),
  customer_count VARCHAR(50),
  online_sales_pct VARCHAR(50)
);

INSERT INTO sales_fact VALUES
(1, 1, 1, 1, '145000', '98000', '47000', '420', '40%'),
(2, 1, 2, 2, 'ninety five thousand', '67000', '28000', '315', '55'),
(3, 2, 3, 3, '88,000', 'sixty two thousand', '26000', '350', 'seventy'),
(4, 3, 4, 4, '112000', '79000', '33k', '375', '45'),
(5, 4, 1, 5, '134000', '93000', '41000', '400', '60'),
(6, 5, 2, 2, '54000', '50000', '4000', 'two hundred ten', '80'),
(7, 6, 3, 3, '60000', '52000', '8000', '240', '85'),
(8, 6, 4, 4, 'sixty-nine thousand', '60000', 'nine thousand', '250', 'seventy'),
(9, 7, 1, 1, '85,000', '72000', '13,000', '280', '75'),
(10, 8, 2, 5, '91,000', '74,000', '17000', '310', 'seventy-two'),
(11, 8, 3, 6, '93,000', '69,000', 'twenty four thousand', '325', '68'),
(12, 8, 4, 4, '102000', '76000', '26000', 'missing', '66'),
(13, 9, 1, 2, 'seventy-seven thousand', '64,000', '13000', '285', '81'),
(14, 9, 2, 3, '83000', '69000', '14000', 'three hundred', '77'),
(15, 10, 3, 1, '118000', '88000', '30000', '410', '58'),
(16, 10, 4, 4, 'one hundred eight thousand', '79000', '29000', '380', 'sixty-three'),
(17, 11, 1, 1, '155000', '110000', '45000', '450', '55'),
(18, 11, 2, 2, '118000', '83000', NULL, '380', '59'),
(19, 11, 3, 3, '106000', '74000', '32000', '390', 'sixty-six'),
(20, 11, 4, 4, '124000', '91000', '33000', '420', '64'),
(21, 12, 1, 5, '136000', '95000', '41000', '400', '67'),
(22, 12, 2, 6, '121000', '85000', '36000', '370', '72'),
(23, 12, 3, 2, '114000', 'eighty-two thousand', '32000', '360', 'sixty-nine'),
(24, 12, 4, 4, '126000', '92000', '34000', '415', 'sixty-two'),
(25, 12, 1, 1, '162000', '117000', '45000', '460', '60'),
(26, 12, 2, 3, '132000', '97000', '35000', '395', '68'),
(27, 12, 3, 4, '124000', '88000', '36000', '410', '64'),
(28, 12, 4, 5, '138000', '98000', '40000', '430', '70');

select * from sales_fact;
desc sales_fact;

UPDATE sales_fact

SET 

    sales_revenue = TRIM(REPLACE(REPLACE(REPLACE(sales_revenue, ',', ''), '%', ''), ' ', '')),

    expense = TRIM(REPLACE(REPLACE(REPLACE(expense, ',', ''), '%', ''), ' ', '')),

    profit = TRIM(REPLACE(REPLACE(REPLACE(profit, ',', ''), '%', ''), ' ', '')),

    customer_count = TRIM(REPLACE(REPLACE(REPLACE(customer_count, ',', ''), '%', ''), ' ', '')),

    online_sales_pct = TRIM(REPLACE(REPLACE(REPLACE(online_sales_pct, ',', ''), '%', ''), ' ', ''));

-- sales_revenue corrections
UPDATE sales_fact
SET sales_revenue = CASE
    WHEN LOWER(sales_revenue) LIKE 'ninetyfivethousand%' THEN '95000'
    WHEN LOWER(sales_revenue) LIKE 'sixtyninethousand%' THEN '69000'
    WHEN LOWER(sales_revenue) LIKE 'seventyseventhousand%' THEN '77000'
    ELSE sales_revenue
END;

-- expense corrections
UPDATE sales_fact
SET expense = CASE
    WHEN LOWER(expense) LIKE 'sixtytwothousand%' THEN '62000'
    ELSE expense
END;

-- profit corrections
UPDATE sales_fact
SET profit = CASE
    WHEN LOWER(profit) LIKE '33k%' THEN '33000'
    WHEN LOWER(profit) LIKE 'ninethousand%' THEN '9000'
    WHEN LOWER(profit) LIKE 'twentyfourt%' THEN '24000'
    ELSE profit
END;

-- customer_count corrections
UPDATE sales_fact
SET customer_count = CASE
    WHEN LOWER(customer_count) LIKE 'twohundredten%' THEN '210'
    WHEN LOWER(customer_count) LIKE 'threehundred%' THEN '300'
    WHEN LOWER(customer_count) LIKE 'missing%' THEN NULL
    ELSE customer_count
END;

-- online_sales_pct corrections
UPDATE sales_fact
SET online_sales_pct = CASE
    WHEN LOWER(online_sales_pct) LIKE 'seventy%' THEN '70'
    WHEN LOWER(online_sales_pct) LIKE 'seventytwo%' THEN '72'
    ELSE online_sales_pct
END;

UPDATE sales_fact
SET 
    sales_revenue = COALESCE(sales_revenue, 0),
    expense = COALESCE(expense, 0),
    profit = COALESCE(profit, 0),
    customer_count = COALESCE(customer_count, 0),
    online_sales_pct = COALESCE(online_sales_pct, 0);

set sql_safe_updates=0;
update sales_fact set expense='82000' where expense='eighty-two';

UPDATE sales_fact SET expense = '62' WHERE expense = 'sixtytwo';
UPDATE sales_fact SET profit = '9' WHERE profit = 'nine';
UPDATE sales_fact SET profit = '20' WHERE profit LIKE 'twenty%';

UPDATE sales_fact SET online_sales_pct = '70' WHERE LOWER(online_sales_pct) = 'seventy';
UPDATE sales_fact SET online_sales_pct = '50' WHERE LOWER(online_sales_pct) = 'fifty';
UPDATE sales_fact SET online_sales_pct = '80' WHERE LOWER(online_sales_pct) = 'eighty';
UPDATE sales_fact SET online_sales_pct = '85' WHERE LOWER(online_sales_pct) IN ('eightyfive', 'eighty five');
UPDATE sales_fact SET online_sales_pct = '63' WHERE LOWER(online_sales_pct) = 'sixty-three';
UPDATE sales_fact SET online_sales_pct = '66' WHERE LOWER(online_sales_pct) = 'sixty-six';
UPDATE sales_fact SET online_sales_pct = '69' WHERE LOWER(online_sales_pct) = 'sixty-nine';
UPDATE sales_fact SET online_sales_pct = '62' WHERE LOWER(online_sales_pct) IN ('sixty-two');

alter table sales_fact modify customer_count int;
desc sales_fact;
alter table sales_fact modify sales_revenue int;
alter table sales_fact modify expense int;
alter table sales_fact modify profit int;
alter table sales_fact modify online_sales_pct int;


