* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.TeleportRoot.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).TeleportRoot
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
public void TeleportRoot([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation); 
### Parameters
Parameter | Description  
---|---  
position | The new position of the root articulation body.  
rotation | The new orientation of the root articulation body.  
### Description
Teleport the root body of the articulation to a new pose.
Articulations are immutable once created, so it's not possible to change positions, orientations or velocities of the articulation bodies. However, you can still move the root body of the articulation with this function. To do so, call the function with the root body of the articulation. Assign zero vectors to [ArticulationBody.linearVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-linearVelocity.html) and [ArticulationBody.angularVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-angularVelocity.html) of the root articulation to reset the movement after [ArticulationBody.TeleportRoot](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.TeleportRoot.html).
* * *
