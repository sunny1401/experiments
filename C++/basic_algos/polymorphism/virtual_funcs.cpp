#include <assert.h>
#include <cmath>

#define PI 3.14159

class VehicleModel{
    public:
    virtual void Move(double v, double phi) = 0;
};

class ParticleModel: public VehicleModel{
    
    public:
    double x = 0.0;
    double y = 0.0;
    double theta = 0.0;
    void Move(double v, double phi) override{
        theta += phi;
        x += v * cos(theta);
        y += v * sin(theta);
    }

};

class BicycleModel: public ParticleModel{
    
    public:
    double L = 1;
    void Move(double v, double phi) override{
        theta +=(v/L) * tan(phi);
        x += v * cos(theta);
        y += v * sin(theta);
    }
    
};

// TODO: Pass the tests
int main() {
  // Test function overriding
  ParticleModel particle;
  BicycleModel bicycle;
  particle.Move(10, PI / 9);
  bicycle.Move(10, PI / 9);
  assert(particle.x != bicycle.x);
  assert(particle.y != bicycle.y);
  assert(particle.theta != bicycle.theta);
}