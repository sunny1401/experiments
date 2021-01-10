#include <cassert>
#include <cmath>
#include <stdexcept>

// TODO: Define class Sphere
class Sphere {
 public:
  Sphere(float _radius): radius(_radius), volume(4/3 * pow(radius,3) * _pi){
      Validate();
  }

  float Radius() const {return radius;}
  float Volume() const {return volume;}

 private:
    float _pi{3.14159};
    float radius;
    float volume;
    void Validate(){
        if (radius < 0){
            throw std::invalid_argument("radius cannot be negative");
        }
    }
};

// Test
int main(void) {
  Sphere sphere(5);
  assert(sphere.Radius() == 5);
  assert(abs(sphere.Volume() - 523.6) < 1);
  }
}