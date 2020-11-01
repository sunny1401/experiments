#include "route_planner.h"
#include <algorithm>


// function copied from code developed during Udacity C++ Nanodegree foundation course
bool Compare(const RouteModel::Node *current_node, const RouteModel::Node *next_node) {
  float f1 = current_node->g_value + current_node->h_value; // f1 = g1 + h1
  float f2 = next_node->g_value + next_node->h_value; // f2 = g2 + h2
  return f1 > f2; 
}

RoutePlanner::RoutePlanner(RouteModel &model, float start_x, float start_y, float end_x, float end_y): m_Model(model) {
    // Convert inputs to percentage:
    start_x *= 0.01;
    start_y *= 0.01;
    end_x *= 0.01;
    end_y *= 0.01;

    start_node = &m_Model.FindClosestNode(start_x, start_y);
    end_node = &m_Model.FindClosestNode(end_x, end_y);
}


float RoutePlanner::CalculateHValue(RouteModel::Node const *node) {
  return node->distance(*end_node);

}

void RoutePlanner::AddNeighbors(RouteModel::Node *current_node) {
  current_node->FindNeighbors();
    for (auto& cnode: current_node->neighbors){
      cnode->parent = current_node;
        cnode->g_value = current_node->g_value + current_node->distance(*cnode);
        cnode->h_value = RoutePlanner::CalculateHValue(cnode);
      if (cnode->visited == false){
        open_list.push_back(cnode);
        cnode->visited = true;
      }
    };
}


RouteModel::Node *RoutePlanner::NextNode() {
  sort(open_list.begin(), open_list.end(), Compare);
    auto current = open_list.back();
    open_list.pop_back();
    return current;
}


std::vector<RouteModel::Node> RoutePlanner::ConstructFinalPath(RouteModel::Node *current_node) {
    // Create path_found vector
    distance = 0.0f;
    std::vector<RouteModel::Node> path_found;

  while(current_node != start_node){
      auto temp = current_node->parent;
      distance = distance + current_node->distance(*temp);
      path_found.push_back(*current_node);
      current_node = temp;
  }
  if (current_node == start_node){
    path_found.push_back(*current_node);
  }
  std::reverse(path_found.begin(), path_found.end());


  distance *= m_Model.MetricScale(); // Multiply the distance by the scale of the map to get meters.
    return path_found;

}


void RoutePlanner::AStarSearch() {
    RouteModel::Node *current_node = nullptr;
  current_node = start_node;
    current_node->g_value = 0.0f;
    current_node->h_value = CalculateHValue(start_node);
    open_list.push_back(current_node);
    current_node->visited = true;
    while(open_list.size() and current_node != end_node){
      
        current_node = NextNode();
        if (current_node == end_node){
            break;
        }
        AddNeighbors(current_node);
        
    } 
    m_Model.path = ConstructFinalPath(current_node);
    

}
