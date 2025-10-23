const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

let painting = false;
let brushColor = document.getElementById("color").value;
let brushSize = document.getElementById("size").value;

// Start drawing
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
  link.download = "my_drawing.png";
  link.href = canvas.toDataURL();
  link.click();
}
