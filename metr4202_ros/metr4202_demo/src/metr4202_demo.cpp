#include "ros/ros.h"
#include "std_msgs/Float64.h"

int main(int argc, char** argv) {
    ros::init(argc, argv, "table_demo");
    ros::NodeHandle table_nh;
    ros::Publisher joint1_pub = table_nh.advertise<std_msgs::Float64>("/table/joint1_velocity_controller/command", 1000);
    int count = 0;
    ros::Rate rate(1000);
    ros::Time start_time = ros::Time::now();
    while (ros::ok()) {
        ros::Time current_time = ros::Time::now();
        float t = (current_time - start_time).toSec();
        std_msgs::Float64 msg;
        if (fmod(t, 15.0) <= 8.0) {
            msg.data = 0.0;
        } else {
            msg.data = 1.0;
        }
        joint1_pub.publish(msg);
        ros::spinOnce();
        rate.sleep();
        count++;
    }
    return 0;
}