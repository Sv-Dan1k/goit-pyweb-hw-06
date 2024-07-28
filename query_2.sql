SELECT students.name, AVG(grades.grade) as avg_grade
FROM grades
JOIN students ON grades.student_id = students.id
WHERE grades.subject_id = ?
GROUP BY students.id
ORDER BY avg_grade DESC
LIMIT 1;