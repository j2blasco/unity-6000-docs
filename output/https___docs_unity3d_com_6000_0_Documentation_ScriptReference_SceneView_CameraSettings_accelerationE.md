* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraSettings-accelerationEnabled.html

#  [SceneView.CameraSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraSettings.html).accelerationEnabled
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
accelerationEnabled; 
### Description
Enables Camera movement acceleration in the [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html). This makes the Camera accelerate for the duration of movement.
When acceleration is disabled, the camera moves at a constant speed based on the [speed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraSettings-speed.html) value. When acceleration is enabled, the camera initially moves at a speed based on the [speed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraSettings-speed.html) value, and continuously increases speed until movement stops. In both cases, if [easingEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraSettings-easingEnabled.html) is enabled, the speed will ease in when the camera starts moving, and ease out when it stops.  
  
With acceleration enabled, you may find it easier to move both short and long distances without needing to frequently change the [speed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraSettings-speed.html) value.
* * *
