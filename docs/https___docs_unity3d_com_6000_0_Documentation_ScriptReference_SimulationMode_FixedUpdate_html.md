* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode.FixedUpdate.html

#  [SimulationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SimulationMode.html).FixedUpdate
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
Use this enumeration to instruct Unity to execute the physics simulation immediately after the [MonoBehaviour.FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html).
Executing the physics simulation during [MonoBehaviour.FixedUpdate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.FixedUpdate.html) provides the most stable physics simulation, however Unity might render multiple frames between simulation updates. This might prevent synchronization of changes made per frame, including contacts between [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html)s, with the physics simulation. This mode requires [Rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody.html) interpolation to provide smoother movement per frame where appropriate.  
  
Additional resources: [Physics.simulationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-simulationMode.html).
* * *
