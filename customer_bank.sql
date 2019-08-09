select 
  *
from
    DBScsfsm.AR.csf_customer a
    inner join DBScsfsm.AR.csf_customer_bank b
    on b.Company = 4000 and b.Customer = a.Customer
where
  a.Customer = 98
