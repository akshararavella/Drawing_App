import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Drawing App", layout="wide")

st.title("🎨 My Drawing App")

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    canvas {
      border: 2px solid #333;
      background: white;
      cursor: crosshair;
    }
    .toolbar {
      margin: 10px 0;
    }
  </style>
</head>
<body>
  <div class="toolbar">
    <label>Brush Size: <input type="range" id="size" min="1" max="50" value="5"></label>
    <input type="color" id="color" value="#000000">
    <button id="clear">Clear</button>
    <button id="save">Save</button>
  </div>

  <canvas id="canvas" width="800" height="500"></canvas>

  <script>
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");

    let painting = false;
    let brushColor = document.getElementById("color").value;
    let brushSize = document.getElementById("size").value;

    canvas.addEventListener("mousedown", startPosition);
    canvas.addEventListener("mouseup", endPosition);
    canvas.addEventListener("mousemove", draw);

    document.getElementById("color").addEventListener("change", e => brushColor = e.target.value);
    document.getElementById("size").addEventListener("change", e => brushSize = e.target.value);
    document.getElementById("clear").addEventListener("click", clearCanvas);
    document.getElementById("save").addEventListener("click", saveCanvas);

    function startPosition(e) {
      painting = true;
      draw(e);
    }

    function endPosition() {
      painting = false;
      ctx.beginPath();
    }

    function draw(e) {
      if (!painting) return;
      ctx.lineWidth = brushSize;
      ctx.lineCap = "round";
      ctx.strokeStyle = brushColor;

      ctx.lineTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop);
    }

    function clearCanvas() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    function saveCanvas() {
      const link = document.createElement("a");
      link.download = "drawing.png";
      link.href = canvas.toDataURL();
      link.click();
    }
  </script>
</body>
</html>
"""

html(html_code, height=600)
