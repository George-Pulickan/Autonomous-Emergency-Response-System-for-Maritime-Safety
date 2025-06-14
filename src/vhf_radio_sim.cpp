#include <iostream>
#include <string>

class VHFModule {
public:
    void sendDistressSignal(const std::string& location, const std::string& msgType) {
        std::cout << "[VHF-DSC] Distress Call Sent\n";
        std::cout << "MMSI: " << MMSI << "\n";
        std::cout << "Location: " << location << "\n";
        std::cout << "Message Type: " << msgType << "\n";
    }

private:
    const std::string MMSI = "123456789";
};

int main() {
    VHFModule radio;
    radio.sendDistressSignal("49.2742,-123.1853", "EMERGENCY: Water ingress detected");
    return 0;
}

