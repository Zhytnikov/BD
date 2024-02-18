SELECT s.name, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sb ON g.subject_id = sb.subject_id
WHERE sb.name = 'offer'
GROUP BY s.student_id
ORDER BY avg_grade DESC
LIMIT 1;