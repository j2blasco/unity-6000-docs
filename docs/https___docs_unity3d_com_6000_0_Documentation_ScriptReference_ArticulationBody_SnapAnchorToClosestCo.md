* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.SnapAnchorToClosestContact.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).SnapAnchorToClosestContact
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
public void SnapAnchorToClosestContact(); 
### Description
Snap the anchor to the closest contact between the connected bodies.
Computes the point on the surface of this body closest to the center of mass of the parent body and sets the anchor to it. If ArticulationBody.computeParentAnchor is set, the parent anchor will be updated accordingly too.  
  
Note that, usually, local zero is not a great default position of the anchor in case the connected bodies have colliders attached, because the joint is likely to be trying to push the bodies into each other then. To address that, this function picks a reasonable default location of the anchors that will work with many articulations.
* * *
