// from data.js
var tableData = data;
console.log(tableData)

// Select tbody into a variable
var tbody = d3.select("tbody")

// Load the data from Data File on the Web Page

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


//  Create a Function that runs when Button is clicked
function runEnter() {
  // Then, select the Table Body list element by class name
  var list = d3.select("tbody");
  // clear any Data from the list to
  list.html("");

  var tbody = d3.select("tbody")

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select (DateTime) the input element and get the raw HTML node
  var inputTable = d3.select("#datetime")
  // Get the value property of the input element
  var inputDate = inputTable.property("value");

   // Select (City) the input element and get the raw HTML node
  var inputTableCity = d3.select("#city")
   // Get the value property of the input element
  var inputCity = inputTableCity.property("value");

   // Select (State) the input element and get the raw HTML node
    var inputTableState = d3.select("#state")
     // Get the value property of the input element
    var inputState = inputTableState.property("value");

    // Select (Country) the input element and get the raw HTML node
    var inputTableCountry = d3.select("#country")
     // Get the value property of the input element
    var inputCountry = inputTableCountry.property("value");

    // Select (Shape) the input element and get the raw HTML node
    var inputTableShape = d3.select("#shape")
     // Get the value property of the input element
    var inputShape = inputTableShape.property("value");

  console.log("======= Print Filtered Data in console=======")
    // Use the form input to filter the data by Date
    var filterDate = tableData.filter(tableData => tableData.datetime === inputDate);
    // Use the form input to filter the data by City
    var filterCity = filterDate.filter(filterDate => filterDate.city === inputCity);
    // Use the form input to filter the data by State
    var filterState = filterCity.filter(filterCity => filterCity.state === inputState);
    // Use the form input to filter the data by Country
    var filterCountry = filterState.filter(filterState => filterState.country === inputCountry);
    // Use the form input to filter the data by Shape
    var filterShape = filterCountry.filter(filterCountry => filterCountry.shape === inputShape);
  
  
// Display data - Filtering it by Date

if (inputCity === "") {
  for (j=0; j<filterDate.length; j++) {
      filter = filterDate[j];
      var trow = tbody.append("tr");
      trow.append("td").text(filter.datetime);
      trow.append("td").text(filter.city);
      trow.append("td").text(filter.state);
      trow.append("td").text(filter.country);
      trow.append("td").text(filter.shape);
      trow.append("td").text(filter.durationMinutes);
      trow.append("td").text(filter.comments);
  }
}

// Display data - Filtering it by City
else if (inputState === "") {
      // Then, select the Table Body list element by class name
      var list = d3.select("tbody");
      // clear any Data from the list to
      list.html("");
      

  for (i=0; i<filterCity.length; i++) {
      filter1 = filterCity[i];
      var trow = tbody.append("tr");
      trow.append("td").text(filter1.datetime);
      trow.append("td").text(filter1.city);
      trow.append("td").text(filter1.state);
      trow.append("td").text(filter1.country);
      trow.append("td").text(filter1.shape);
      trow.append("td").text(filter1.durationMinutes);
      trow.append("td").text(filter1.comments);
  }
}

// Display data - Filtering it by State
else if (inputCountry === "") {
  // Then, select the Table Body list element by class name
  var list = d3.select("tbody");
  // clear any Data from the list to
  list.html("");
  

for (i=0; i<filterState.length; i++) {
  filter2 = filterState[i];
  var trow = tbody.append("tr");
  trow.append("td").text(filter2.datetime);
  trow.append("td").text(filter2.city);
  trow.append("td").text(filter2.state);
  trow.append("td").text(filter2.country);
  trow.append("td").text(filter2.shape);
  trow.append("td").text(filter2.durationMinutes);
  trow.append("td").text(filter2.comments);
  }
}

// Display data - Filtering it by Country
else if (inputShape === "") {
  // Then, select the Table Body list element by class name
  var list = d3.select("tbody");
  // clear any Data from the list to
  list.html("");
  

for (i=0; i<filterCountry.length; i++) {
  filter3 = filterCountry[i];
  var trow = tbody.append("tr");
  trow.append("td").text(filter3.datetime);
  trow.append("td").text(filter3.city);
  trow.append("td").text(filter3.state);
  trow.append("td").text(filter3.country);
  trow.append("td").text(filter3.shape);
  trow.append("td").text(filter3.durationMinutes);
  trow.append("td").text(filter3.comments);
  }
}

// Display data - Filtering it by Shape
else  {
  // Then, select the Table Body list element by class name
  var list = d3.select("tbody");
  // clear any Data from the list to
  list.html("");
  

for (i=0; i<filterShape.length; i++) {
  filter4 = filterShape[i];
  var trow = tbody.append("tr");
  trow.append("td").text(filter4.datetime);
  trow.append("td").text(filter4.city);
  trow.append("td").text(filter4.state);
  trow.append("td").text(filter4.country);
  trow.append("td").text(filter4.shape);
  trow.append("td").text(filter4.durationMinutes);
  trow.append("td").text(filter4.comments);
  }
}


}


