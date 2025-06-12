* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetJointForcesForAcceleration.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).GetJointForcesForAcceleration
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ArticulationBody.html "Go to ArticulationBody Component in the Manual")
## Declaration
public [ArticulationReducedSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationReducedSpace.html) GetJointForcesForAcceleration([ArticulationReducedSpace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationReducedSpace.html) acceleration); 
### Parameters
Parameter | Description  
---|---  
acceleration | The desired acceleration in reduced space.  
### Returns
**ArticulationReducedSpace** The forces needed for the body to reach the desired acceleration in reduced space. 
### Description
Returns the forces required for the body to reach the provided acceleration in reduced space.
The number of DOF in the provided acceleration must match the DOF count of the inbound joint. The calculation does **not** consider gravity and therefore gravity must be counteracted with [ArticulationBody.GetJointGravityForces](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetJointGravityForces.html). ArticulationDrives and potential damping terms are not considered in the computation (for example, linear/angular damping or joint friction).   
The returned forces can then be applied with [ArticulationBody.jointForce](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-jointForce.html).  
  
Units of measurement - N (newtons) for linear and Nm (newton-meters) for angular motion.
* * *
