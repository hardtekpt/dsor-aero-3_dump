// Generated by gencpp from file mavros_msgs/RTKBaseline.msg
// DO NOT EDIT!


#ifndef MAVROS_MSGS_MESSAGE_RTKBASELINE_H
#define MAVROS_MSGS_MESSAGE_RTKBASELINE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace mavros_msgs
{
template <class ContainerAllocator>
struct RTKBaseline_
{
  typedef RTKBaseline_<ContainerAllocator> Type;

  RTKBaseline_()
    : header()
    , time_last_baseline_ms(0)
    , rtk_receiver_id(0)
    , wn(0)
    , tow(0)
    , rtk_health(0)
    , rtk_rate(0)
    , nsats(0)
    , baseline_coords_type(0)
    , baseline_a_mm(0)
    , baseline_b_mm(0)
    , baseline_c_mm(0)
    , accuracy(0)
    , iar_num_hypotheses(0)  {
    }
  RTKBaseline_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , time_last_baseline_ms(0)
    , rtk_receiver_id(0)
    , wn(0)
    , tow(0)
    , rtk_health(0)
    , rtk_rate(0)
    , nsats(0)
    , baseline_coords_type(0)
    , baseline_a_mm(0)
    , baseline_b_mm(0)
    , baseline_c_mm(0)
    , accuracy(0)
    , iar_num_hypotheses(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef uint32_t _time_last_baseline_ms_type;
  _time_last_baseline_ms_type time_last_baseline_ms;

   typedef uint8_t _rtk_receiver_id_type;
  _rtk_receiver_id_type rtk_receiver_id;

   typedef uint16_t _wn_type;
  _wn_type wn;

   typedef uint32_t _tow_type;
  _tow_type tow;

   typedef uint8_t _rtk_health_type;
  _rtk_health_type rtk_health;

   typedef uint8_t _rtk_rate_type;
  _rtk_rate_type rtk_rate;

   typedef uint8_t _nsats_type;
  _nsats_type nsats;

   typedef uint8_t _baseline_coords_type_type;
  _baseline_coords_type_type baseline_coords_type;

   typedef int32_t _baseline_a_mm_type;
  _baseline_a_mm_type baseline_a_mm;

   typedef int32_t _baseline_b_mm_type;
  _baseline_b_mm_type baseline_b_mm;

   typedef int32_t _baseline_c_mm_type;
  _baseline_c_mm_type baseline_c_mm;

   typedef uint32_t _accuracy_type;
  _accuracy_type accuracy;

   typedef int32_t _iar_num_hypotheses_type;
  _iar_num_hypotheses_type iar_num_hypotheses;



  enum {
    RTK_BASELINE_COORDINATE_SYSTEM_ECEF = 0u,
    RTK_BASELINE_COORDINATE_SYSTEM_NED = 1u,
  };


  typedef boost::shared_ptr< ::mavros_msgs::RTKBaseline_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mavros_msgs::RTKBaseline_<ContainerAllocator> const> ConstPtr;

}; // struct RTKBaseline_

typedef ::mavros_msgs::RTKBaseline_<std::allocator<void> > RTKBaseline;

typedef boost::shared_ptr< ::mavros_msgs::RTKBaseline > RTKBaselinePtr;
typedef boost::shared_ptr< ::mavros_msgs::RTKBaseline const> RTKBaselineConstPtr;

// constants requiring out of line definition

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mavros_msgs::RTKBaseline_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mavros_msgs::RTKBaseline_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace mavros_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'geographic_msgs': ['/opt/ros/kinetic/share/geographic_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'mavros_msgs': ['/tmp/binarydeb/ros-kinetic-mavros-msgs-1.6.0/msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'uuid_msgs': ['/opt/ros/kinetic/share/uuid_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::mavros_msgs::RTKBaseline_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mavros_msgs::RTKBaseline_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mavros_msgs::RTKBaseline_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mavros_msgs::RTKBaseline_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mavros_msgs::RTKBaseline_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mavros_msgs::RTKBaseline_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mavros_msgs::RTKBaseline_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bd5852b76aa13136cec34a65089dfdb2";
  }

  static const char* value(const ::mavros_msgs::RTKBaseline_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbd5852b76aa13136ULL;
  static const uint64_t static_value2 = 0xcec34a65089dfdb2ULL;
};

template<class ContainerAllocator>
struct DataType< ::mavros_msgs::RTKBaseline_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mavros_msgs/RTKBaseline";
  }

  static const char* value(const ::mavros_msgs::RTKBaseline_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mavros_msgs::RTKBaseline_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# RTKBaseline received from the FCU.\n\
# Full description: https://mavlink.io/en/messages/common.html#GPS_RTK\n\
# Mavlink Common, #127and #128\n\
\n\
std_msgs/Header header\n\
\n\
uint32 time_last_baseline_ms\n\
uint8 rtk_receiver_id\n\
uint16 wn\n\
uint32 tow\n\
uint8 rtk_health\n\
uint8 rtk_rate\n\
uint8 nsats\n\
\n\
uint8 baseline_coords_type \n\
uint8 RTK_BASELINE_COORDINATE_SYSTEM_ECEF = 0   # Earth-centered, earth-fixed\n\
uint8 RTK_BASELINE_COORDINATE_SYSTEM_NED = 1    # RTK basestation centered, north, east, down\n\
\n\
int32 baseline_a_mm\n\
int32 baseline_b_mm\n\
int32 baseline_c_mm\n\
uint32 accuracy\n\
int32 iar_num_hypotheses\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::mavros_msgs::RTKBaseline_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mavros_msgs::RTKBaseline_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.time_last_baseline_ms);
      stream.next(m.rtk_receiver_id);
      stream.next(m.wn);
      stream.next(m.tow);
      stream.next(m.rtk_health);
      stream.next(m.rtk_rate);
      stream.next(m.nsats);
      stream.next(m.baseline_coords_type);
      stream.next(m.baseline_a_mm);
      stream.next(m.baseline_b_mm);
      stream.next(m.baseline_c_mm);
      stream.next(m.accuracy);
      stream.next(m.iar_num_hypotheses);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RTKBaseline_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mavros_msgs::RTKBaseline_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mavros_msgs::RTKBaseline_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "time_last_baseline_ms: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.time_last_baseline_ms);
    s << indent << "rtk_receiver_id: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.rtk_receiver_id);
    s << indent << "wn: ";
    Printer<uint16_t>::stream(s, indent + "  ", v.wn);
    s << indent << "tow: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.tow);
    s << indent << "rtk_health: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.rtk_health);
    s << indent << "rtk_rate: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.rtk_rate);
    s << indent << "nsats: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.nsats);
    s << indent << "baseline_coords_type: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.baseline_coords_type);
    s << indent << "baseline_a_mm: ";
    Printer<int32_t>::stream(s, indent + "  ", v.baseline_a_mm);
    s << indent << "baseline_b_mm: ";
    Printer<int32_t>::stream(s, indent + "  ", v.baseline_b_mm);
    s << indent << "baseline_c_mm: ";
    Printer<int32_t>::stream(s, indent + "  ", v.baseline_c_mm);
    s << indent << "accuracy: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.accuracy);
    s << indent << "iar_num_hypotheses: ";
    Printer<int32_t>::stream(s, indent + "  ", v.iar_num_hypotheses);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MAVROS_MSGS_MESSAGE_RTKBASELINE_H
