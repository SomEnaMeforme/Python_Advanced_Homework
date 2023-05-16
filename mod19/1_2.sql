select student_id as student, avg(grade) as t1
from assignments_grades
group by student_id
order by t1 desc
limit 10