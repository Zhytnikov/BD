SELECT s.name AS student_name, g.grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sb ON g.subject_id = sb.subject_id
WHERE sb.name = 'offer' AND s.group_id = 1;