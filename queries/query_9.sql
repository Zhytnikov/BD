SELECT s.name AS subject_name
FROM students st
JOIN grades g ON st.student_id = g.student_id
JOIN subjects s ON g.subject_id = s.subject_id
WHERE st.name = 'Brooke Lopez';