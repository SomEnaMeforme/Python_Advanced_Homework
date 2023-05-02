select customer.full_name
from customer
left join "order" on customer.customer_id = "order".customer_id
where "order".customer_id is null