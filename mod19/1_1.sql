select teacher, min(t1) as minimum_grade from (
select teacher_id as teacher, avg(grade) as t1 from
assignments
inner join assignments_grades
on assignments.assisgnment_id=assignments_grades.assisgnment_id
group by teacher_id)