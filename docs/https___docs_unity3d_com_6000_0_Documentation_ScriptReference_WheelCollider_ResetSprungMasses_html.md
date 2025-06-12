* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.ResetSprungMasses.html

#  [WheelCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.html).ResetSprungMasses
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
## Declaration
public void ResetSprungMasses(); 
### Description
Reset the sprung masses of the vehicle.
Recomputes the sprung masses of all wheels of the vehicle this wheel belongs to. In addition, it clears the internal explicit sprung mass distribution flag if that was raised before by calling [WheelCollider.sprungMass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-sprungMass.html). Note that because this function works with the vehicle itself but not just one wheel, it's enough to call it once for a vehicle, invoked with any wheel. 
* * *
