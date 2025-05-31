#include <iostream>
#include <cstdlib>
#include <ctime>

class EnvironmentSensor {
public:
    void read() {
        std::srand(std::time(nullptr));
        double temperature = 15.0 + (std::rand() % 1000) / 100.0;
        double pressure = 1000.0 + (std::rand() % 500) / 10.0;

        std::cout << "[EnvSensor] Temp: " << temperature << " °C, Pressure: " << pressure << " hPa" << std::endl;
    }
};

int main() {
    EnvironmentSensor sensor;
    sensor.read();
    return 0;
}
