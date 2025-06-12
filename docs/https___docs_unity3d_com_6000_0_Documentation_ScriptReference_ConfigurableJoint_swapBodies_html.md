* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConfigurableJoint-swapBodies.html

#  [ConfigurableJoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ConfigurableJoint.html).swapBodies
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ConfigurableJoint.html "Go to ConfigurableJoint Component in the Manual")
swapBodies; 
### Description
Enable this property to swap the order in which the physics engine processes the Rigidbodies involved in the joint. This results in different joint motion but has no impact on Rigidbodies and anchors.
Prior to Unity 3.4, this was wrongfully applied to all ConfigurableJoints with the `configuredInWorldSpace/` property set. If you want to restore the behaviour of older Unity versions and you are using `configuredInWorldSpace`, enable this property.
* * *
