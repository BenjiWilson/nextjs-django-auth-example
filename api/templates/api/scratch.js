function CommentAggChart(search) {
    var $comment_aggChart = $("#comment_agg-chart");

    $.ajax({

        url: $comment_aggChart.data("url"),
        type: "GET",
        data: { "form_results" : FormResults()},

    

        success: function (data) {



            var ctx = $comment_aggChart[0].getContext('2d');
            if (window.hasOwnProperty("comment_agg_chart")) {
                comment_agg_chart.destroy();
            }

            comment_agg_chart = new Chart(ctx, {
                type: 'horizontalBar',
                data: {
                    labels: JSON.parse(data).labels,
                    datasets: [
                        {
                            label: "Activity",
                            data: JSON.parse(data).data
                        }
                    ]
                },
                options: {

                    plugins: {
                        colorschemes: {
                            scheme: 'brewer.Paired12'
                        }
                    },

                    responsive: true,
                    defaultFontSize: 8,
                    maintainAspectRatio: false,

                    legend: { display: false },
                    title: {
                        display: false,
                        text: 'ACTIVITY'
                    }
                }
            });

        }
    });
