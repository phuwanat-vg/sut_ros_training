#include <ros.h>
#include <std_msgs/Int16.h>
#include <sensor_msgs/Range.h>

//---------------Ultrasonic------------
const int trig = 3;
const int echo = 11;
float range = 0.0;

ros::NodeHandle nh;

std_msgs::Int16 num_msg;
ros::Publisher int_pub("number", &num_msg);
int i = 0;

sensor_msgs::Range range_msg;
ros::Publisher range_pub("ultrasonic", &range_msg);

void ultrasonic() {
  long duration;
  pinMode(trig, OUTPUT);
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(5);
  digitalWrite(trig, LOW);
  pinMode(echo, INPUT);
  duration = pulseIn(echo, HIGH);
  range = microsecondsToCentimeters(duration);
  Serial.println(range);
  delay(5);
}

float microsecondsToCentimeters(long microseconds)
{
  return microseconds / 29.0 / 2.0;
}

void setup() {
  // put your setup code here, to run once:
  nh.initNode();
  nh.advertise(int_pub);
  nh.advertise(range_pub);
}

void loop() {
  ultrasonic();
  i++;
  delay(10);

  range_msg.range = range;
  num_msg.data = i;
  range_pub.publish(&range_msg);
  int_pub.publish(&num_msg);
  nh.spinOnce();
}
