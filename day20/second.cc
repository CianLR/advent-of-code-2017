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

void tick(vector<Particle> &parts) {
  for (int i = 0; i < parts.size(); ++i) {
    parts[i].vx += parts[i].ax;
    parts[i].vy += parts[i].ay;
    parts[i].vz += parts[i].az;

    parts[i].x += parts[i].vx;
    parts[i].y += parts[i].vy;
    parts[i].z += parts[i].vz;
  }
}

vector<Particle> rm_collision(const vector<Particle> &parts) {
  unordered_set<int> collide;
  for (int i = 0; i < parts.size(); ++i) {
    for (int j = i + 1; j < parts.size(); ++j) {
      if (parts[i] == parts[j]) {
        collide.insert(i);
        collide.insert(j);
      }
    }
  }
  vector<Particle> new_parts;
  for (int i = 0; i < parts.size(); ++i) {
    if (collide.find(i) != collide.end()) continue;
    new_parts.push_back(parts[i]);
  }
  return new_parts;
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

unsigned int simulate(int iters, vector<Particle> parts) {
  for (int i = 0; i < iters; ++i) {
    tick(parts);
    parts = rm_collision(parts);
  }
  return parts.size();
}

int main() {
  vector<Particle> parts;
  read_particles(parts);
  printf("%u\n", simulate(10000, parts));
}

