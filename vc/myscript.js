'use strict';

var lastTime = -1;
var tsArray = [];

function forward1sec() {
    var curTime = document.getElementById("myVideo").currentTime;
    document.getElementById("myVideo").currentTime = parseFloat(curTime) + 1.0;
}
function forward0_1sec() {
    var curTime = document.getElementById("myVideo").currentTime;
    document.getElementById("myVideo").currentTime = parseFloat(curTime) + 0.1;
}
function back1sec() {
    var curTime = parseFloat(document.getElementById("myVideo").currentTime);
    while (lastTime > curTime - 1.0) {
        document.getElementById("mytable").deleteRow(0);
        var x = tsArray.pop();
        if (document.getElementById("mytable").rows.length > 0) {
            lastTime = parseFloat((document.getElementById("mytable").rows[0].cells)[0].innerHTML);
        } else {
            lastTime = -1;
        }
    }
    document.getElementById("myVideo").currentTime = parseFloat(curTime) - 1.0;
}
function back0_1sec() {
    var curTime = parseFloat(document.getElementById("myVideo").currentTime);
    while (lastTime > curTime - 0.1) {
        document.getElementById("mytable").deleteRow(0);
        var x = tsArray.pop();
        if (document.getElementById("mytable").rows.length > 0) {
            lastTime = parseFloat((document.getElementById("mytable").rows[0].cells)[0].innerHTML);
        } else {
            lastTime = -1;
        }
    }
    document.getElementById("myVideo").currentTime = parseFloat(curTime) - 0.1;
}
function play_pause() {
    var v = document.getElementById("myVideo");
    if (v.paused) {
        v.play();
        document.getElementById("play-pause").innerHTML = "Pause";
    } else {
        v.pause();
        document.getElementById("play-pause").innerHTML = "Play ";
    }
}
function slow_fast() {
    var v = document.getElementById("myVideo");
    if(v.playbackRate == 1.0) {
        v.playbackRate = 0.5;
        document.getElementById("slow-fast").innerHTML = "Fast";
    } else {
        v.playbackRate = 1.0;
        document.getElementById("slow-fast").innerHTML = "Slow";
    }
}

function exportToCsv(filename, rows) {
    var processRow = function (row) {
        var finalVal = '';
        for (var j = 0; j < row.length; j++) {
            var innerValue = row[j] === null ? '' : row[j].toString();
            if (row[j] instanceof Date) {
                innerValue = row[j].toLocaleString();
            };
            var result = innerValue.replace(/"/g, '""');
            if (result.search(/("|,|\n)/g) >= 0)
                result = '"' + result + '"';
            if (j > 0)
                finalVal += ',';
            finalVal += result;
        }
        return finalVal + '\n';
    };

    var csvFile = '';
    for (var i = 0; i < rows.length; i++) {
        csvFile += processRow(rows[i]);
    }

    var blob = new Blob([csvFile], { type: 'text/csv;charset=utf-8;' });
    if (navigator.msSaveBlob) { // IE 10+
        navigator.msSaveBlob(blob, filename);
    } else {
        var link = document.createElement("a");
        if (link.download !== undefined) { // feature detection
            // Browsers that support HTML5 download attribute
            var url = URL.createObjectURL(blob);
            link.setAttribute("href", url);
            link.setAttribute("download", filename);
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }
    }
}

