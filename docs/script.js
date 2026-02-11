let budget = localStorage.getItem("budget") || 0;
let expenses = JSON.parse(localStorage.getItem("expenses")) || [];

function setBudget() {
  budget = parseFloat(document.getElementById("budget").value);
  localStorage.setItem("budget", budget);
  updateSummary();
}

function addExpense() {
  const category = document.getElementById("category").value;
  const amount = parseFloat(document.getElementById("amount").value);

  if (!category || isNaN(amount)) {
    alert("Fill all fields");
    return;
  }

  expenses.push({ category, amount });
  localStorage.setItem("expenses", JSON.stringify(expenses));

  updateSummary();
}

function updateSummary() {
  const totalSpent = expenses.reduce((sum, e) => sum + e.amount, 0);
  const remaining = budget - totalSpent;

  document.getElementById("spent").textContent = totalSpent;
  document.getElementById("remaining").textContent = remaining;

  const categoryTotals = {};
  expenses.forEach(e => {
    categoryTotals[e.category] = (categoryTotals[e.category] || 0) + e.amount;
  });

  const categoryDiv = document.getElementById("categories");
  categoryDiv.innerHTML = "<h3>Category Breakdown</h3>";

  for (let cat in categoryTotals) {
    categoryDiv.innerHTML += `<p>${cat}: ${categoryTotals[cat]}</p>`;
  }
}

updateSummary();
