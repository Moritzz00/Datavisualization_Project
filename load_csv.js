
// Use D3.js to load the CSV file
d3.csv("modifizierter_Datensatz.csv").then(function(data) {
  // 'data' is an array containing the contents of the CSV file

  // Process the data and aggregate counts by journal
  var nestedData = d3.rollup(
    data,
    // Aggregation function: Count the number of titles for each journal
    v => ({ count: v.length }),
    // Group by the 'journal' column
    d => d.Zeitschriftkürzel
  );

  // Display the aggregated counts in small boxes
  var sortedData = Array.from(nestedData, ([key, value]) => ({ key, value }));  

  sortedData.sort((a, b) => b.value.count - a.value.count);

  var boxContainer = d3.select("#box-container");

  sortedData.forEach(entry => {
    
    var box = boxContainer
      .append("div")
      .classed("box", true);

    box
      .append("div")
      .classed("journal", true)
      .text(`${entry.key}`);
    
    box
      .append("div")
      .classed(`count`, true)
      .text(`${entry.value.count}`);
    });

  // Display the general information 
  var totalCount = data.length;
  
  var uniqueJournalCount = nestedData.size;
  
  var generalInforamtion = d3.select("#general-information");
  
  generalInforamtion
    .append("p")
    .classed("paragraph", true)
    .text(`Es gibt insgesamt ${totalCount} Artikel von ${uniqueJournalCount} Zeitschriften in dem Datensatz.`)
});