function init() {

    var dropdownMenu = d3.select("#selDataset");

    d3.json(url).then (function (data){
        console.log(data);

        var sampleData = data.names;
        console.log(sampleData);
        
        for (var i=0; i < 156; i++) {
        toption = dropdownMenu.append("option");
        toption.text(sampleData[i])
        toption.property("value", sampleData[i]);
        };
    });
};

   
function optionChanged(newSample) {
    buildtable(newSample);
    plotbar(newSample);
    plotbubble(newSample);
    // buildGaugeChart(newSample);
}

// Call updatePlotly() when a change takes place to the DOM
d3.selectAll("#selDataset").on("change", init);

// Since the data is a Json Data we have to get the URL
url = "samples.json"

function buildtable(sample) {
    
    d3.json(url).then(function(data) {
      console.log(data);


      // Grab values from the response json object to build the plots
      var metadata = data.metadata;
      console.log(metadata);

      //  filtering Meta data and setting it to a new variable
      var metaFilter = metadata.filter(row => row.id == sample);
      console.log(metaFilter)
      
      var finaldata = metaFilter[0];
      console.log(finaldata)

      var list1 = d3.selectAll("#sample-metadata");
      //   Clear the HTML List so it dont show up multiple time
      list1.html("");
      
      Object.entries(finaldata).forEach(([key, value]) => {
        list1.append("h6").text(key + ': ' + value); 
      })
    
   });

};
buildtable();

/////////////////////////////////////////////////////////////////////////////////

// Create a function to plot the data (Bar Chart and Bubble Chart)
function plotbar(sample) {
d3.json(url).then (function (data){
    var sampledata = data.samples;
    console.log(sampledata)

    var sampleFilter = sampledata.filter(row => row.id == sample);
    console.log(sampleFilter);

    var finalsample = sampleFilter[0];
    console.log(finalsample);

    var sampleValues = finalsample.sample_values.slice(0, 10).reverse();
    console.log(sampleValues);
    // var sampleValue1 = sampleValues.reverse();

    var otuIDs = finalsample.otu_ids.slice(0, 10).reverse();
    console.log(otuIDs);
    // var outid = otuIDs.reverse();
    var outid1 = otuIDs.map(row => "OTU" + row)

    var otuLabels = finalsample.otu_labels.slice(0, 10).reverse();
    console.log(otuLabels.reverse());
    // var outLabels1 = otuLabels.reverse();

    var sampleID = finalsample.id.slice(0, 10);
    console.log(sampleID);


    // Create Bar Chart //////

    var trace1 = {
        
        x: sampleValues,
        y: outid1,
        text: otuLabels,
        type: "bar",
        orientation: "h"
    }
    var data = [trace1];
    
    var layout = {
        title: "OTU - Top 10",
        yaxis:{
            tickmode:"linear",
        },
        margin: {
            l: 100,
            r: 100,
            t: 100,
            b: 30
        }
    };

    Plotly.newPlot("bar", data, layout);
});
};

function plotbubble(sample) {
  d3.json(url).then (function (data){ 
    
    var sampledata = data.samples;
    console.log(sampledata)

    var filterdata = sampledata.filter(row => row.id == sample);
    console.log(filterdata);

    var finalfilterdata = filterdata[0];
    console.log(finalfilterdata);

    //////// Create Bubble Chart /////////
    
    // pull all sample values
    var sampleValue2 = finalfilterdata.sample_values;
    console.log(sampleValue2);
    
    // pull all otuIDs
    var OtuIDs = finalfilterdata.otu_ids;
    console.log(OtuIDs);

    var otulabels = finalfilterdata.otu_labels;
    console.log(otulabels)


    trace2 = {
        x: OtuIDs,
        y:sampleValue2,
        mode: "markers",
        
        marker: {
            size: sampleValue2,
            color: OtuIDs
        },
        text:otulabels
    };

    data1 = [trace2];

    // set the layout for the bubble plot
    var layout1 = {
        xaxis:{title: "OTU ID"},
                height: 600,
                width: 1000
        };

    Plotly.newPlot("bubble", data1, layout1)
  });  
    
};

init();





