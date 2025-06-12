* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetJointPositions.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).GetJointPositions
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
public int GetJointPositions(List<float> positions); 
### Parameters
Parameter | Description  
---|---  
positions | Supplied list of floats to read back and store the joint positions data.   
### Returns
**int** Total degrees of freedom for the entire hierarchy of articulation bodies. 
### Description
Reads back articulation body joint positions of the entire hierarchy to the supplied list of floats .
This returns joint positions in the reduced coordinate space for the entire articulation hierarchy starting from root to the supplied list of floats. Every joint position DOF is represented by one float value, however depending on the type of the articulation joint there might be zero, one or 3 DOFs per joint. The exact location of the data in resulting list for the specific articulation body can be found by calling [ArticulationBody.GetDofStartIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetDofStartIndices.html) and indexing returned dofStartIndices list by the particular body index via [ArticulationBody.index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-index.html). Number of degrees of freedom for the articulation body can be found using [ArticulationBody.dofCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-dofCount.html).  
  
Units of measurement - meters for linear and radians for angular motion.  
  
Additional resources: [index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-index.html), [GetDofStartIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetDofStartIndices.html), [dofCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-dofCount.html), [SetJointPositions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.SetJointPositions.html). 
* * *
