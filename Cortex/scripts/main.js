let generateSimulation = () => {
    fetch('http://localhost:5000/fakesimulation').then(response => response.json()).then(data => {
        console.log(data.invested);
        var options = {
            chart: {
                type: 'line'
            },
            series: [
                {
                    name: 'Net Assets',
                    data: data.net
                },
                {
                    name: 'Invested Assets',
                    data: data.invested
                },
                {
                    name: 'Pocketed Assets',
                    data: data.pocket
                },
                {
                    name: 'Ethereum Price',
                    data: data.real
                },
                {
                    name: 'Predicted Price',
                    data: data.fake
                },
                {
                    name: 'Model Confidence',
                    data: data.confidence
                }
            ],
            xaxis: {
                show: false
            },
            yaxis: {
                labels: {
                  formatter: function (value) {
                    return value.toFixed(0); // Change the number inside to set the desired decimal places
                  }
                }
            }
        }
        var loader = document.getElementById('loader');
        loader.style.opacity = 0;
        loader.style.transition = "0.5s";
        loader.style.transitionDelay = "0s";
        var chart = new ApexCharts(document.querySelector('#chart'), options);
        var chartStyle = document.getElementById('chart').style;
        chartStyle.opacity = 1;
        chartStyle.transition = '1.5s';
        chartStyle.position = 'fixed';
        chartStyle.display = 'block';
        chartStyle.transitionDelay = '3.5s';
        chart.render()
    }).catch(error => {
        console.error(error);
    });
}

let fadeOutAndMoveUp = () => {
    var button = document.getElementById('startbtn');
    var title = document.getElementById('title');
    var loader = document.getElementById('loader');
    loader.style.opacity = 1;
    loader.style.transition = '0.5s';
    loader.style.transitionDelay = '1s';
    button.style.animation = 'fadeAndMoveUp 1s forwards';
    title.style.animation = 'fadeAndMoveUp 1s forwards';
    button.addEventListener('animationend', function() {
      button.style.display = 'none';
    });
    title.addEventListener('animationend', function() {
        title.style.display = 'none';
    });
    generateSimulation();
}