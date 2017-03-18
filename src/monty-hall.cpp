#include <iostream>
#include <sstream>

#define SIMULATION_ROUNDS 100

int main(int argc, char *argv[]) {
  int sim_rounds = SIMULATION_ROUNDS;
  if(argc > 1) {
    sim_rounds = std::stringstream(argv[1]);
  }
  std::cout << sim_rounds << '\n';
}
