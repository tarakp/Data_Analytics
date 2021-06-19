// from data.js
var tableData = data;
console.log(tableData)

// Select tbody into a variable
var tbody = d3.select("tbody")



    for (var j=0; j<tableData.length; j++) {
        tableDatas = tableData[j];
        var trow = tbody.append("tr")
        trow.append("td").text(tableDatas.datetime)
        trow.append("td").text(tableDatas.city)
        trow.append("td").text(tableDatas.state)
        trow.append("td").text(tableDatas.country)
        trow.append("td").text(tableDatas.shape)
        trow.append("td").text(tableDatas.durationMinutes)
        trow.append("td").text(tableDatas.comments)
  }


// return(table)
// Select the button
var button = d3.select("#filter-btn");

// Select the form
var form = d3.select("#datetime");

// Create event handlers 
// button.on("click", clear());
button.on("click", runEnter);
form.on("submit",runEnter);

function runEnter() {
    // Then, select the unordered list element by class name
  var list = d3.select("tbody");
  // remove any children from the list to
  list.html("");
  var tbody = d3.select("tbody")
  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputTable = d3.select("#datetime")

  // Get the value property of the input element
  var inputDate = inputTable.property("value");

  console.log("======= Print Filtered Data in console=======")
  // Use the form input to filter the data by blood type
  var filterDate = tableData.filter(tableData => tableData.datetime === inputDate);
  console.log(filterDate);

  for (j=0; j<filterDate.length; j++) {
      filter = filterDate[j];
      var trow = tbody.append("tr")
      trow.append("td").text(filter.datetime)
      trow.append("td").text(filter.city)
      trow.append("td").text(filter.state)
      trow.append("td").text(filter.country)
      trow.append("td").text(filter.shape)
      trow.append("td").text(filter.durationMinutes)
      trow.append("td").text(filter.comments)
  }

//   filterDate.map(filterDate => tbody.append("tr").append("td").text(filterDate.datetime));
  
}



