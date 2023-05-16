oбщее количество учеников:
select sg.group_id, count(*) AS students_count from students
inner join students_groups sg on sg.group_id = students.group_id
group by sg.group_id

средняя оценка
select sg.group_id, round(avg(ag.grade),2) as students_count
from students
inner join students_groups sg on sg.group_id = students.group_id
inner join assignments_grades ag on students.student_id = ag.student_id
group by sg.group_id
order by students_count

количество учеников, которые не сдали работы
select sg.group_id, count(ag.student_id)
from students
inner join students_groups as sg on sg.group_id = students.group_id
inner join (
    select distinct student_id from (
    select sum(grade) as sum_grade, student_id
    from assignments_grades
    group by assisgnment_id, student_id
    having sum_grade > 0)) as ag on students.student_id = ag.student_id
group by sg.group_id

количество учеников, которые просрочили дедлайн
select sg.group_id, count(ag.student_id)
from students
inner join students_groups as sg on sg.group_id = students.group_id
inner join
    (select distinct student_id
    from
       (select student_id
        from assignments_grades
       inner join assignments as a on assignments_grades.assisgnment_id = a.assisgnment_id
        where a.due_date < assignments_grades.date)) as ag on students.student_id = ag.student_id
group by sg.group_id;

количество повторных попыток сдать работу
select sg.group_id,
      count(ag.student_id) as students_count,
      sum(ag.count - 1) as additional_attempts_count
from students
inner join students_groups sg on sg.group_id = students.group_id
inner join
    (select student_id, assisgnment_id, sum(grade), count(*) AS count
    from assignments_grades
   group by student_id, assisgnment_id
    having count > 1) as ag on students.student_id = ag.student_id
group by sg.group_id;