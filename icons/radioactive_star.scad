$fn=512;


difference() {
	circle(r = 100);
	circle(r = 95.0000000000);
}
$fn=512;


union() {
	difference() {
		union() {
			rotate(a = [0, 0, 0.0000000000]) {
				intersection() {
					circle(r = 90.0000000000);
					intersection() {
						square(size = 200);
						rotate(a = [0, 0, -54.0000000000]) {
							square(size = 200);
						}
					}
				}
			}
			rotate(a = [0, 0, 72.0000000000]) {
				intersection() {
					circle(r = 90.0000000000);
					intersection() {
						square(size = 200);
						rotate(a = [0, 0, -54.0000000000]) {
							square(size = 200);
						}
					}
				}
			}
			rotate(a = [0, 0, 144.0000000000]) {
				intersection() {
					circle(r = 90.0000000000);
					intersection() {
						square(size = 200);
						rotate(a = [0, 0, -54.0000000000]) {
							square(size = 200);
						}
					}
				}
			}
			rotate(a = [0, 0, 216.0000000000]) {
				intersection() {
					circle(r = 90.0000000000);
					intersection() {
						square(size = 200);
						rotate(a = [0, 0, -54.0000000000]) {
							square(size = 200);
						}
					}
				}
			}
			rotate(a = [0, 0, 288.0000000000]) {
				intersection() {
					circle(r = 90.0000000000);
					intersection() {
						square(size = 200);
						rotate(a = [0, 0, -54.0000000000]) {
							square(size = 200);
						}
					}
				}
			}
		}
		circle(r = 25.0000000000);
	}
	circle(r = 20.0000000000);
}
