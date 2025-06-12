* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode.Script.html

#  [SimulationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode.html).Script
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
Use this enumeration to instruct Unity to execute the physics simulation manually when you call [Physics.Simulate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Simulate.html).
Executing the physics simulation in a script provides full control over when the simulation runs and the duration of simulation. Use this mode to emulate both [SimulationMode.FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode.FixedUpdate.html) and [SimulationMode.Update](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode.Update.html), and any other custom time interval.  
  
The stability and determinism of the simulation depends on when Unity executes the simulation. If the simulation runs each frame, then it is always synchronized, including contacts between [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)s. This means that [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) interpolation is not required.  
  
Additional resources: [Physics.simulationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-simulationMode.html).
* * *
