* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-sprungMass.html

#  [WheelCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.html).sprungMass
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
sprungMass; 
### Description
The mass supported by this WheelCollider.
Vehicle simulation uses the sprung mass model that assumes each wheel supports a particular portion of the vehicle's total mass at rest. By default, the sprung mass distribution is computed automatically based on the positions of the wheels relative to the vehicle's center of mass. However, it's also possible to set the masses explicitly. In this case, the whole vehicle is marked as having an explicit mass distribution and no sprung masses will ever be computed for it until the explicit flag is reset by calling [WheelCollider.ResetSprungMasses](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.ResetSprungMasses.html). Note that the sum of all the sprung masses should be equivalent to the total mass of the vehicle. Because of that, adjusting a wheel's sprung mass will naturally require updating the sprung masses for the other wheels of the vehicle in order to match the vehicle's mass.
* * *
