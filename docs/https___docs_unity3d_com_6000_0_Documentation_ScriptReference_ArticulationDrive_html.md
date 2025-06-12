* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationDrive.html

# ArticulationDrive
struct in UnityEngine
/
Implemented in:[UnityEngine.PhysicsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.PhysicsModule.html)
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
### Description
Drive applies forces and torques to the connected bodies.
Drive moves the body along one degree of freedom, be it a linear motion along a particular axis or a rotational motion around a particular axis. The drive will apply force to the body that is calculated from the current value of the drive, using this formula: F = stiffness * (currentPosition - target) - damping * (currentVelocity - targetVelocity). In this formula, currentPosition and currentVelocity are linear position and linear velocity in case of the linear drive. In case of the rotational drive, currentPosition and currentVelocity correspond to the angle and angular velocity respectively.
### Properties
Property | Description  
---|---  
[damping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationDrive-damping.html) | The damping of the spring attached to this drive.  
[driveType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationDrive-driveType.html) | Specifies which drive type to use for this drive.  
[forceLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationDrive-forceLimit.html) | The maximum force this drive can apply to a body.  
[lowerLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationDrive-lowerLimit.html) | The lower limit of motion for a particular degree of freedom.  
[stiffness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationDrive-stiffness.html) | The stiffness of the spring connected to this drive.  
[target](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationDrive-target.html) | The target value the drive will try to reach.  
[targetVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationDrive-targetVelocity.html) | The velocity of the body this drive will try to reach.  
[upperLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationDrive-upperLimit.html) | The upper limit of motion for a particular degree of freedom.  
* * *
