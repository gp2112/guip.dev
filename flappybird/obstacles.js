class Obstacle {

	constructor(x, y, width, height, upsideDown) {
		let img = new Image();
		if (upsideDown) {
			img.src = "obstacles/pipdown.png";

		} else {
			img.src = "obstacles/pipe.png";
		}
		
		this.img = img;  
		this.x = x;
		this.y = y;
		this.width = width;
		this.height = height;
		this.upsideDown = upsideDown;
	}

	colide(player) {
		if (this.upsideDown) {
			return (this.x <= 65 && this.x >= 65-this.width) && (player.y <= this.height-5);
		}
		return (this.x <= 65 && this.x >= 65-this.width) && (player.y >= this.y-13);

	}
	passed(player) {
		
		return (this.x <= 65 && this.x >= 65-this.width && !this.colide(player));
	}
}

let obstacles = [];

function genObstacle() {
	let width = 50;
	let height = randInt(50, cvs.height-40);
	let upsideDown = parseInt(Math.random() * 10 % 2);
	let y = upsideDown ? 0 : cvs.height-height;
	let obs = new Obstacle(cvs.width, y, width, height, upsideDown);
	obstacles.push(obs);
}
