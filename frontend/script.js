fetch('http://localhost:8000/api/employees')
  .then(res => res.json())
  .then(data => {
    const table = document.querySelector('#employeeTable tbody');
    data.forEach(emp => {
      const row = `<tr>
        <td>${emp.emp_id}</td>
        <td>${emp.first_name} ${emp.last_name}</td>
        <td>${emp.dob}</td>
        <td>${emp.department}</td>
        <td>${emp.email}</td>
        <td>${emp.salary}</td>
        <td>${emp.gender}</td>
      </tr>`;
      table.innerHTML += row;
    });
  });
