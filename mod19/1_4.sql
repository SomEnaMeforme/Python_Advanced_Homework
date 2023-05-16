select group_id,
       round(avg(works), 2) as average,
       max(works) as maximum,
       min(works) as minimum
from (
         select count(grade_id) as works, group_id
         from assignments_grades
         inner join students as s on s.student_id = assignments_grades.student_id
         where grade_id in (
             select grade_id
             from assignments_grades
             where assignments_grades.date > (
                 select due_date
                 from assignments
                 where assignments_grades.assisgnment_id = assignments.assisgnment_id
             )
         )
         group by assisgnment_id, group_id
     )
group by group_id