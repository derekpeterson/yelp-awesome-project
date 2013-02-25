var fill = d3.scale.category20(),
data;

d3.json('totalwordcounts.json', function(response) {
	data = response;
	d3.layout.cloud().size([1200, 600])
	.words(d3.entries(data).map(function(d) {
			return {text: d["key"], size: d["value"] / 30};
		}))
	.rotate(function() { return ~~(Math.random() * 2) * 90; })
	.font("Impact")
	.fontSize(function(d) { return d.size; })
	.on("end", draw)
	.start();
});

function draw(words) {
	d3.select(".cloud").append("svg")
	.attr("width", 1200)
	.attr("height", 600)
	.append("g")
	.attr("transform", "translate(570,300)")
	.selectAll("text")
	.data(words)
	.enter().append("text")
	.style("font-size", function(d) { return d.size + "px"; })
	.style("font-family", "Helvetica")
	.style("fill", function(d, i) { return fill(i); })
	.attr("text-anchor", "middle")
	.attr("transform", function(d) {
		return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
	})
	.text(function(d) { return d.text; });
}
