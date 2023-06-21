# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from control_msgs/PointHeadGoal.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import geometry_msgs.msg
import std_msgs.msg

class PointHeadGoal(genpy.Message):
  _md5sum = "8b92b1cd5e06c8a94c917dc3209a4c1d"
  _type = "control_msgs/PointHeadGoal"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
geometry_msgs/PointStamped target
geometry_msgs/Vector3 pointing_axis
string pointing_frame
duration min_duration
float64 max_velocity

================================================================================
MSG: geometry_msgs/PointStamped
# This represents a Point with reference coordinate frame and timestamp
Header header
Point point

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
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

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
  __slots__ = ['target','pointing_axis','pointing_frame','min_duration','max_velocity']
  _slot_types = ['geometry_msgs/PointStamped','geometry_msgs/Vector3','string','duration','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       target,pointing_axis,pointing_frame,min_duration,max_velocity

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PointHeadGoal, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.target is None:
        self.target = geometry_msgs.msg.PointStamped()
      if self.pointing_axis is None:
        self.pointing_axis = geometry_msgs.msg.Vector3()
      if self.pointing_frame is None:
        self.pointing_frame = ''
      if self.min_duration is None:
        self.min_duration = genpy.Duration()
      if self.max_velocity is None:
        self.max_velocity = 0.
    else:
      self.target = geometry_msgs.msg.PointStamped()
      self.pointing_axis = geometry_msgs.msg.Vector3()
      self.pointing_frame = ''
      self.min_duration = genpy.Duration()
      self.max_velocity = 0.

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
      buff.write(_get_struct_3I().pack(_x.target.header.seq, _x.target.header.stamp.secs, _x.target.header.stamp.nsecs))
      _x = self.target.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_6d().pack(_x.target.point.x, _x.target.point.y, _x.target.point.z, _x.pointing_axis.x, _x.pointing_axis.y, _x.pointing_axis.z))
      _x = self.pointing_frame
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2id().pack(_x.min_duration.secs, _x.min_duration.nsecs, _x.max_velocity))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.target is None:
        self.target = geometry_msgs.msg.PointStamped()
      if self.pointing_axis is None:
        self.pointing_axis = geometry_msgs.msg.Vector3()
      if self.min_duration is None:
        self.min_duration = genpy.Duration()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.target.header.seq, _x.target.header.stamp.secs, _x.target.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.target.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.target.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.target.point.x, _x.target.point.y, _x.target.point.z, _x.pointing_axis.x, _x.pointing_axis.y, _x.pointing_axis.z,) = _get_struct_6d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pointing_frame = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.pointing_frame = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.min_duration.secs, _x.min_duration.nsecs, _x.max_velocity,) = _get_struct_2id().unpack(str[start:end])
      self.min_duration.canon()
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
      buff.write(_get_struct_3I().pack(_x.target.header.seq, _x.target.header.stamp.secs, _x.target.header.stamp.nsecs))
      _x = self.target.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_6d().pack(_x.target.point.x, _x.target.point.y, _x.target.point.z, _x.pointing_axis.x, _x.pointing_axis.y, _x.pointing_axis.z))
      _x = self.pointing_frame
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2id().pack(_x.min_duration.secs, _x.min_duration.nsecs, _x.max_velocity))
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
      if self.target is None:
        self.target = geometry_msgs.msg.PointStamped()
      if self.pointing_axis is None:
        self.pointing_axis = geometry_msgs.msg.Vector3()
      if self.min_duration is None:
        self.min_duration = genpy.Duration()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.target.header.seq, _x.target.header.stamp.secs, _x.target.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.target.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.target.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 48
      (_x.target.point.x, _x.target.point.y, _x.target.point.z, _x.pointing_axis.x, _x.pointing_axis.y, _x.pointing_axis.z,) = _get_struct_6d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pointing_frame = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.pointing_frame = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.min_duration.secs, _x.min_duration.nsecs, _x.max_velocity,) = _get_struct_2id().unpack(str[start:end])
      self.min_duration.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2id = None
def _get_struct_2id():
    global _struct_2id
    if _struct_2id is None:
        _struct_2id = struct.Struct("<2id")
    return _struct_2id
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_6d = None
def _get_struct_6d():
    global _struct_6d
    if _struct_6d is None:
        _struct_6d = struct.Struct("<6d")
    return _struct_6d
