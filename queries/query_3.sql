SELECT s.group_id, AVG(g.grade) AS avg_grade
FROM grades g
JOIN subjects sb ON g.subject_id = sb.subject_id
JOIN students s ON g.student_id = s.student_id
WHERE sb.name = 'offer'
GROUP BY s.group_id;