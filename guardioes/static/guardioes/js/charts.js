(function () {
    'use strict';
    window.Ns = window.Ns || {};

    Ns.graphs = {
        /**
         * Creates nvd3 linear graph
         */
        linear: function (selector, data) {
            nv.addGraph(function () {
                var chart = nv.models.lineChart().useInteractiveGuideline(true);
                chart.xAxis
                    .axisLabel('Datetime')
                    .tickFormat(function (date) {
                        return d3.time.format('%d-%m-%Y')(new Date(date));
                    });
                chart.yAxis
                    .axisLabel('Value')
                    .tickFormat(d3.format('.02f'));
                d3.select(selector)
                    .datum(data)
                    .transition().duration(500)
                    .call(chart);
                nv.utils.windowResize(chart.update);
                console.log(data)
                console.log('charteou?')
                return chart;
            });
        },


        createFromJson: function (type, selector, json) {
            Ns.graphs[type](selector, json);
        },

        init: function () {
            $('.ns-chart').each(function (i, el) {
                var chartDiv = $(el),
                    url = chartDiv.attr('data-url'),
                    type = chartDiv.attr('data-type'),
                    width = chartDiv.attr('data-width'),
                    height = chartDiv.attr('data-height');
                // append svg element
                chartDiv.append('<svg style="height:'+height+';width:'+width+';margin:0 auto" id="ns-chart-' + i + '"></svg>');
                // get graph data
                $.getJSON(url).done(function (json) {
                    // create graph
                    Ns.graphs.createFromJson(type, '#ns-chart-' + i, json);
                });
            });
        }
    };
})();

