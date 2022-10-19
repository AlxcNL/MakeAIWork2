# Queries vanuit de Command line

### SQLite3 opstarten

```sh
sqlite3 Chinook.db
```

### Database initieren
```sh
.read Chinook_Sqlite.sql
```

**Laat de tabellen zien**
```sh
.tables
```

**Probeer een eenvoudige query**
```sql
select * 
from Artist 
limit 10;
```

### Practice 

<ol>

<li>

**Provide a query showing Customers**
```sql
select customerid, firstname, lastname, country
from customer
```
</li>

<li>

**Provide a query only showing the Customers from Brazil**
```sql
select * 
from customer
where country = 'Brazil'
```

</li>

<li>

**Provide a query showing the Invoices of customers who are from Brazil**

The resultant table should show the customer's full name, Invoice ID, Date of the invoice and billing country.

```sql
select c.firstname, c.lastname, i.invoiceid, i.invoicedate, i.billingcountry
from customer as c, invoice as i
where c.country = 'Brazil' and
c.customerid = i.customerid
```

</li>

<li>

**Provide a query showing only the Employees who are Sales Agents**
```sql
select * 
from employee
where employee.title = 'Sales Support Agent';
```
</li>

<li>

**Provide a query showing the invoices of customers who are from Brazil**
```sql
select *
from customer as c, invoice as i
where c.country = 'Brazil' and
c.customerid = i.customerid;
```
</li>

<li>

**Provide a query that shows the # of customers assigned to each sales agent**
```sql
select e.*, count(c.customerid) as 'TotalCustomers'
from employee as e
join customer as c on e.employeeid = c.supportrepid
group by e.employeeid
```

</li>
	
</ol>	
