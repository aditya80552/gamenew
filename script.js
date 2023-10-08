var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

var paddle1 = {
  x: 10,
  y: 100,
  width: 10,
  height: 50
};

var paddle2 = {
  x: 480,
  y: 100,
  width: 10,
  height: 50
};

var ball = {
  x: 250,
  y: 150,
  radius: 5,
  dx: 5,
  dy: -5
};

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  ctx.fillRect(paddle1.x, paddle1.y, paddle1.width, paddle1.height);
  ctx.fillRect(paddle2.x, paddle2.y, paddle2.width, paddle2.height);

  ctx.fillStyle = "red";
  ctx.fillRect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2);
}

function update() {
  // Move the ball
  ball.x += ball.dx;
  ball.y += ball.dy;

  // Check for collisions with the paddles
  if (ball.x - ball.radius < paddle1.x + paddle1.width && ball.y - ball.radius < paddle1.y + paddle1.height && ball.y + ball.radius > paddle1.y) {
    ball.dx = -ball.dx;
  }

  if (ball.x + ball.radius > paddle2.x && ball.y - ball.radius < paddle2.y + paddle2.height && ball.y + ball.radius > paddle2.y) {
    ball.dx = -ball.dx;
  }

  // Check if the ball has hit the top or bottom of the screen
  if (ball.y - ball.radius < 0 || ball.y + ball.radius > canvas.height) {
    ball.dy = -ball.dy;
  }

  // Check if the ball has gone past a paddle
  if (ball.x < 0 || ball.x > canvas.width) {
    // Game over
    alert("Game over!");
    return;
  }
}

function gameloop() {
  update();
  draw();

  requestAnimationFrame(gameloop);
}

gameloop();
