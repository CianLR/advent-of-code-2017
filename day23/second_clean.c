int main() {
long a = 1, b = 0, c = 0, d = 0, e = 0, f = 0, g = 0, h = 0;
line5: b = 108400;
line6: c = 125400;
line8: f = 1;
line10: e = 2;  // Outer loop
line11: if ((b % e) == 0) goto line25;  // Start inner, maybe break
line16: e += 1;
line19: if (e != b) goto line11; // Repeat inner
line24: if (f != 0) goto line28;
line25: h += 1;
line28: if (b == c) goto lineend;
line30: b += 17;
line31: goto line8;
lineend:
printf("%ld\n", h);
}
