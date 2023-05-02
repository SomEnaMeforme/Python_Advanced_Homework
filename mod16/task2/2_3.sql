select "order".order_no, customer.full_name, manager.full_name, "order".purchase_amount
from customer, manager, "order"
on "order".customer_id = customer.customer_id and "order".manager_id = manager.manager_id
where customer.city != manager.city