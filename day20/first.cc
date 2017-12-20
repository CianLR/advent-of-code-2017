#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <unordered_set>

using namespace std;

struct Particle {
  Particle(int x_, int y_, int z_,
           int vx_, int vy_, int vz_,
           int ax_, int ay_, int az_)
    : x(x_), y(y_), z(z_), vx(vx_), vy(vy_), vz(vz_), ax(ax_), ay(ay_), az(az_) {}

  int x, y, z, vx, vy, vz, ax, ay, az;

  bool operator==(const Particle &oth) const {
    return x == oth.x && y == oth.y && z == oth.z;
  }
};

void read_particles(vector<Particle> &parts) {
  int x, y, z, vx, vy, vz, ax, ay, az;
  while (scanf("p=<%d,%d,%d>, v=<%d,%d,%d>, a=<%d,%d,%d>\n",
               &x, &y, &z, &vx, &vy, &vz, &ax, &ay, &az) == 9) {
    parts.emplace_back(x, y, z, vx, vy, vz, ax, ay, az);
  }
}

int min_accel(const vector<Particle> &parts) {
  int min_a = 100000000;
  int min_i = -1;
  for (int i = 0; i < parts.size(); ++i) {
    int v = abs(parts[i].ax) + abs(parts[i].ay) + abs(parts[i].az);
    if (v < min_a) {
      min_a = v;
      min_i = i;
    }
  }
  return min_i;
}

int main() {
  vector<Particle> parts;
  read_particles(parts);
  printf("%d\n", min_accel(parts));
}

