;; Auto-generated. Do not edit!


(when (boundp 'control_msgs::SingleJointPositionResult)
  (if (not (find-package "CONTROL_MSGS"))
    (make-package "CONTROL_MSGS"))
  (shadow 'SingleJointPositionResult (find-package "CONTROL_MSGS")))
(unless (find-package "CONTROL_MSGS::SINGLEJOINTPOSITIONRESULT")
  (make-package "CONTROL_MSGS::SINGLEJOINTPOSITIONRESULT"))

(in-package "ROS")
;;//! \htmlinclude SingleJointPositionResult.msg.html


(defclass control_msgs::SingleJointPositionResult
  :super ros::object
  :slots ())

(defmethod control_msgs::SingleJointPositionResult
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(setf (get control_msgs::SingleJointPositionResult :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get control_msgs::SingleJointPositionResult :datatype-) "control_msgs/SingleJointPositionResult")
(setf (get control_msgs::SingleJointPositionResult :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

")



(provide :control_msgs/SingleJointPositionResult "d41d8cd98f00b204e9800998ecf8427e")

