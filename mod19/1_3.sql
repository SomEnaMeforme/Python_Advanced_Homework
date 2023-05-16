select distinct full_name
from students
         inner join students_groups
                    on students.group_id = students_groups.group_id
         inner join assignments
                    on students_groups.teacher_id = assignments.teacher_id
         inner join assignments_grades
                    on assignments.assisgnment_id = assignments_grades.assisgnment_id
where assignments_grades.assisgnment_id = (
    select assisgnment_id
    from assignments_grades
    group by assisgnment_id
    order by avg(grade) desc
    limit 1)