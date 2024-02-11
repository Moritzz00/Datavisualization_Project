var svg = d3.select("#circle-packingDiagram"),
  margin = 20,
  diameter = +svg.attr("width"),
  g = svg
    .append("g")
    .attr("transform", "translate(" + diameter / 2 + "," + diameter / 2 + ")");

var color = d3
  .scaleLinear()
  .domain([-1])
  .range(["#dadada"])
  .interpolate(d3.interpolateHcl);

var pack = d3
  .pack()
  .size([diameter, diameter])

d3.json("chart_final.json", function (error, root) {
  if (error) throw error;

  root = d3
    .hierarchy(root)
    .sum(function (d) {
      return (d.size);
    })
    .sort(function (a, b) {
      return b.value - a.value;
    });

  var focus = root,
    nodes = pack(root).descendants(),
    view;

  var div = d3.select("body").append("div")
  .attr("class", "tooltip")
  .style("opacity", 0);

  var circle = g
    .selectAll("circle")
    .data(nodes)
    .enter()
    .append("circle")
    .attr("class", function (d) {
      return d.parent
        ? d.children
          ? "node"
          : "node node--leaf"
        : "node node--root";
    })
    .style("fill", function (d) {
      if (d.data.name === "Deutschland") {
        return "#3366CC";
      }
      else if (d.data.name === "Österreich") {
        return "#B82E2E";
      }
      else if (d.data.name === "Schweiz") {
        return "#FF9900";
      }
      else if (d.data.name === "Lichtenstein") {
        return "#109618";
      }
      else if (d.data.name === "Niederlande") {
        return "#990099";
      }
      else if (d.data.tag === 1 || d.data.tag === 11) {
        return "#0099C6";
      }
      else if (d.data.tag === 5 || d.data.tag === 55) {
        return "#DD4477";
      }
      else if (d.data.tag === 4 || d.data.tag === 44) {
        return "#66AA00";
      }
      else if (d.data.tag === 2 || d.data.tag === 22) {
        return "#DC3912";
      }
      else if (d.data.tag === 3 || d.data.tag === 33) {
        return "#FFB647";
      }
       else {
        return d.children ? color(d.depth) : null;
      }
    })
    .on("click", function (d) {
      if (focus !== d) zoom(d), d3.event.stopPropagation();
      div.transition()
      .duration('50')
      .style("opacity", 0);
    })
    .on('mouseover', function (d) {
      //d3.select(this).transition()
      //     .duration('50')
      //     .attr('opacity', '.85');
      //Makes the new div appear on hover:
      div.transition()
      .duration(50)
      .style("opacity", 1);


      let num =d.data.tooltip + '<br>Anzahl an Zeitschriften: ' + d.data.size;
      div.html(num)
     .style("left", (d3.event.pageX + 10) + "px")
     .style("top", (d3.event.pageY - 15) + "px");
    })
    .on('mouseout', function (d) {
      //d3.select(this).transition()
      //     .duration('50')
      //     .attr('opacity', '1');

      //Makes the new div disappear:
      div.transition()
      .duration('50')
      .style("opacity", 0);
    })

  var text = g
    .selectAll("text")
    .data(nodes)
    .enter()
    .append("text")
    .attr("class", "label")
    .style("fill-opacity", function (d) {
      return d.parent === root ? 1 : 0;
    })
    .style("display", function (d) {
      return d.parent === root ? "inline" : "none";
    })
    .style("font-size", function (d) {
      // Passe die Schriftgröße basierend auf der Tiefe der Hierarchie an
      return d.parent === root ? "20px" : "12px"; // Passe die Größen nach Bedarf an
    })
    .text(function (d) {
      return d.data.name;
    });

  var node = g.selectAll("circle,text");

  svg.style("background", color(-1)).on("click", function () {
    zoom(root);
  });

  zoomTo([root.x, root.y, root.r * 2 + margin]);

  function zoom(d) {
    var focus0 = focus;
    focus = d;

    var transition = d3
      .transition()
      .duration(d3.event.altKey ? 7500 : 750)
      .tween("zoom", function (d) {
        var i = d3.interpolateZoom(view, [
          focus.x,
          focus.y,
          focus.r * 2 + margin
        ]);
        return function (t) {
          zoomTo(i(t));
        };
      });

    transition
      .selectAll("text")
      .filter(function (d) {
        return d.parent === focus || this.style.display === "inline";
      })
      .style("fill-opacity", function (d) {
        return d.parent === focus ? 1 : 0;
      })
      .on("start", function (d) {
        if (d.parent === focus) this.style.display = "inline";
      })
      .on("end", function (d) {
        if (d.parent !== focus) this.style.display = "none";
      });
  }

  function zoomTo(v) {
    var k = diameter / v[2];
    view = v;
    node.attr("transform", function (d) {
      return "translate(" + (d.x - v[0]) * k + "," + (d.y - v[1]) * k + ")";
    });
    circle.attr("r", function (d) {
      return d.r * k;
    });
  }
});
