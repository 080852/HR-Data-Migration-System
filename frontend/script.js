const API_URL = "https://hr-backend-o0ga.onrender.com/api/employees";

async function loadEmployees() {
  try {
    const response = await fetch(API_URL);
    const data = await response.json();

    const tableHead = document.getElementById("tableHead");
    const tableBody = document.getElementById("tableBody");

    // Reset
    tableHead.innerHTML = "";
    tableBody.innerHTML = "";

    if (data.length === 0) {
      tableBody.innerHTML = "<tr><td colspan='100%'>No employees found</td></tr>";
      return;
    }

    // Table Headers
    const headers = Object.keys(data[0]);
    headers.forEach((key) => {
      const th = document.createElement("th");
      th.textContent = key.toUpperCase();
      tableHead.appendChild(th);
    });

    // Table Rows
    data.forEach((employee) => {
      const row = document.createElement("tr");
      headers.forEach((key) => {
        const cell = document.createElement("td");
        cell.textContent = employee[key];
        row.appendChild(cell);
      });
      tableBody.appendChild(row);
    });

  } catch (error) {
    console.error("Error fetching employees:", error);
  }
}

window.onload = loadEmployees;
