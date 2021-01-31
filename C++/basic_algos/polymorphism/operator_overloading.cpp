#include <assert.h>

// TODO: Define Point class
class Point{
    public:
    Point(int x, int y): x(x), y(y){}
    int x{0};
    int y{0};
};

Point operator+(const Point& P1, const Point& P2){
    int x = P1.x + P2.x;
    int y = P1.y + P2.y;
    Point ps(x, y);
    return ps;
}

// Test in main()
int main() {
  Point p1(10, 5), p2(2, 4);
  Point p3 = p1 + p2; // An example call to "operator +";
  assert(p3.x == p1.x + p2.x);
  assert(p3.y == p1.y + p2.y);
}