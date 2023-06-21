# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from mavros_msgs/HilSensor.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class HilSensor(genpy.Message):
  _md5sum = "2a892891e5c40d6dd1066bf1f394b5dc"
  _type = "mavros_msgs/HilSensor"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# HilSensor.msg
#
# ROS representation of MAVLink HIL_SENSOR
# See mavlink message documentation here:
# https://mavlink.io/en/messages/common.html#HIL_SENSOR

std_msgs/Header header

geometry_msgs/Vector3 acc
geometry_msgs/Vector3 gyro
geometry_msgs/Vector3 mag
float32 abs_pressure
float32 diff_pressure
float32 pressure_alt
float32 temperature
uint32 fields_updated

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['header','acc','gyro','mag','abs_pressure','diff_pressure','pressure_alt','temperature','fields_updated']
  _slot_types = ['std_msgs/Header','geometry_msgs/Vector3','geometry_msgs/Vector3','geometry_msgs/Vector3','float32','float32','float32','float32','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,acc,gyro,mag,abs_pressure,diff_pressure,pressure_alt,temperature,fields_updated

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(HilSensor, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.acc is None:
        self.acc = geometry_msgs.msg.Vector3()
      if self.gyro is None:
        self.gyro = geometry_msgs.msg.Vector3()
      if self.mag is None:
        self.mag = geometry_msgs.msg.Vector3()
      if self.abs_pressure is None:
        self.abs_pressure = 0.
      if self.diff_pressure is None:
        self.diff_pressure = 0.
      if self.pressure_alt is None:
        self.pressure_alt = 0.
      if self.temperature is None:
        self.temperature = 0.
      if self.fields_updated is None:
        self.fields_updated = 0
    else:
      self.header = std_msgs.msg.Header()
      self.acc = geometry_msgs.msg.Vector3()
      self.gyro = geometry_msgs.msg.Vector3()
      self.mag = geometry_msgs.msg.Vector3()
      self.abs_pressure = 0.
      self.diff_pressure = 0.
      self.pressure_alt = 0.
      self.temperature = 0.
      self.fields_updated = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_9d4fI().pack(_x.acc.x, _x.acc.y, _x.acc.z, _x.gyro.x, _x.gyro.y, _x.gyro.z, _x.mag.x, _x.mag.y, _x.mag.z, _x.abs_pressure, _x.diff_pressure, _x.pressure_alt, _x.temperature, _x.fields_updated))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.acc is None:
        self.acc = geometry_msgs.msg.Vector3()
      if self.gyro is None:
        self.gyro = geometry_msgs.msg.Vector3()
      if self.mag is None:
        self.mag = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 92
      (_x.acc.x, _x.acc.y, _x.acc.z, _x.gyro.x, _x.gyro.y, _x.gyro.z, _x.mag.x, _x.mag.y, _x.mag.z, _x.abs_pressure, _x.diff_pressure, _x.pressure_alt, _x.temperature, _x.fields_updated,) = _get_struct_9d4fI().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_9d4fI().pack(_x.acc.x, _x.acc.y, _x.acc.z, _x.gyro.x, _x.gyro.y, _x.gyro.z, _x.mag.x, _x.mag.y, _x.mag.z, _x.abs_pressure, _x.diff_pressure, _x.pressure_alt, _x.temperature, _x.fields_updated))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.acc is None:
        self.acc = geometry_msgs.msg.Vector3()
      if self.gyro is None:
        self.gyro = geometry_msgs.msg.Vector3()
      if self.mag is None:
        self.mag = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 92
      (_x.acc.x, _x.acc.y, _x.acc.z, _x.gyro.x, _x.gyro.y, _x.gyro.z, _x.mag.x, _x.mag.y, _x.mag.z, _x.abs_pressure, _x.diff_pressure, _x.pressure_alt, _x.temperature, _x.fields_updated,) = _get_struct_9d4fI().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_9d4fI = None
def _get_struct_9d4fI():
    global _struct_9d4fI
    if _struct_9d4fI is None:
        _struct_9d4fI = struct.Struct("<9d4fI")
    return _struct_9d4fI
