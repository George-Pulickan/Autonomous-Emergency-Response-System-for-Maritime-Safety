#include <iostream>
#include <string>
#include <sstream>
#include <vector>

class GPSModule {
public:
    void parseNMEA(const std::string& nmea) {
        std::vector<std::string> parts = split(nmea, ',');
        if (parts[0] == "$GPGGA") {
            std::string time = parts[1];
            std::string latitude = convertToDecimal(parts[2], parts[3]);
            std::string longitude = convertToDecimal(parts[4], parts[5]);

            std::cout << "[GPS] Time: " << time
                      << ", Lat: " << latitude
                      << ", Long: " << longitude << std::endl;
        }
    }

private:
    std::vector<std::string> split(const std::string& str, char delimiter) {
        std::vector<std::string> tokens;
        std::stringstream ss(str);
        std::string temp;
        while (std::getline(ss, temp, delimiter)) {
            tokens.push_back(temp);
        }
        return tokens;
    }

    std::string convertToDecimal(const std::string& raw, const std::string& dir) {
        if (raw.empty()) return "0.0";
        double degrees = std::stod(raw.substr(0, 2));
        double minutes = std::stod(raw.substr(2));
        double decimal = degrees + (minutes / 60.0);
        return (dir == "S" || dir == "W" ? "-" : "") + std::to_string(decimal);
    }
};

int main() {
    GPSModule gps;
    gps.parseNMEA("$GPGGA,123456,4916.45,N,12311.12,W,1,08,0.9,545.4,M,46.9,M,,*47");
    return 0;
}
