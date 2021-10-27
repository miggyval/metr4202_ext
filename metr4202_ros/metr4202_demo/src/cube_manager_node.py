import rospy
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Transform
from metr4202_msgs.msg import CubeData, DemoData
from std_msgs.msg import Int64

class CubeManager:
    def __init__(self):
        rospy.init_node("cube_manager")
        rate = rospy.Rate(100)
        self.sub = rospy.Subscriber("/gazebo/model_states", ModelStates, self.model_state_cb)
        self.pub = rospy.Publisher("/cube_camera", DemoData, queue_size=10)
        

    def model_state_cb(self, msg):
        demo_data = DemoData()
        demo_data.cubes = []
        for i in range(len(msg.name)):
            name = msg.name[i]
            pose = msg.pose[i]
            if name in ['cube_red', 'cube_green', 'cube_blue', 'cube_yellow']:                
                tf = Transform()
                tf.translation.x = pose.position.x
                tf.translation.y = pose.position.y
                tf.translation.z = pose.position.z
                tf.rotation = pose.orientation
                msg_cube = CubeData()
                if name == 'cube_red':
                    n = 0
                if name == 'cube_green':
                    n = 1
                if name == 'cube_blue':
                    n = 2
                if name == 'cube_yellow':
                    n = 3
                msg_cube.id = Int64(n)
                msg_cube.color = Int64(n + 1)
                msg_cube.cube_camera = tf
                demo_data.cubes.append(msg_cube)
        self.pub.publish(demo_data)

if __name__ == "__main__":
    try:
        cube_manager = CubeManager()
        rospy.spin()
    except rospy.ROSInterruptException:
        print("Exiting!")