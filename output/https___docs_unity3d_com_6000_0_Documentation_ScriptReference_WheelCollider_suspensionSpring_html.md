* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-suspensionSpring.html

#  [WheelCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.html).suspensionSpring
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-WheelCollider.html "Go to WheelCollider Component in the Manual")
[JointSpring](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSpring.html) suspensionSpring; 
### Description
The parameters of wheel's suspension. The suspension attempts to reach a target position by applying a linear force and a damping force.
The value [suspensionSpring.spring](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSpring-spring.html) describes the stiffness of the spring. It is expressed in Newtons per metre. The spring strength has a profound influence on handling by modulating the time it takes for the vehicle to respond to bumps in the road and on the amount of load experienced by the tire. Larger values make the suspension reach the target position faster but at the cost of increased load and handling variability. Smaller values provide a smoother but less responsive ride.  
  
The value [suspensionSpring.damper](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSpring-spring.html) describes the rate at which the spring dissipates the energy stored in the spring. It is expressed in Newtons seconds per metre (equivalent to Newtons per unit speed). Larger values make the suspension reach the target position slower, while lower values make the car appear more bouncy. Vehicle suspensions typically have a response close to critical damping.  
  
The rest coordinate of the wheel is specified by [suspensionSpring.targetPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/JointSpring-targetPosition.html). This value describes the rest coordinate of the wheel as a fraction in range (0, 1) along the `suspensionDistance`. Zero value maps to full extension along the suspension travel, while a value of one maps to fully compressed suspension. Default value is 0.5, which sets the rest coordinate of the wheel to the mid-point between the suspension at maximum elongation and maximum compression. Typical values would be in range (0.3, 0.7).
* * *
