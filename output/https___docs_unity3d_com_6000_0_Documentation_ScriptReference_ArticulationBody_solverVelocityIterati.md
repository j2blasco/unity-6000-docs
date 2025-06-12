* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-solverVelocityIterations.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).solverVelocityIterations
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
solverVelocityIterations; 
### Description
The solverVelocityIterations affects how accurately articulation body joints and collision contacts are resolved during bounce.
Increasing this value will result in higher accuracy of the resulting exit velocity after an articulation body bounce. You can try to increase this value if you are experiencing issues with jointed articulation bodies moving too much after collisions. Overrides [Physics.defaultSolverVelocityIterations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics-defaultSolverVelocityIterations.html). Must be positive.  
  
Additional resources: [ArticulationBody.solverIterations](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-solverIterations.html).
* * *
