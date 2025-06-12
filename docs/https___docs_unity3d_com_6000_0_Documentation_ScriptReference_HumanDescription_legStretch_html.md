* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription-legStretch.html

#  [HumanDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription.html).legStretch
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
legStretch; 
### Description
Amount by which the leg's length is allowed to stretch when using IK.
Inverse Kinematics (IK) can often be handled more smoothly if a small amount of "slack" is allowed in the positions of bones relative to each other. This property controls how much slack is available in the leg joints.  
  
The value is given in world distance units in the range 0..1. For example, with the default setting of 0.05, the leg will begin to stretch when the IK goal is at 95% of the target and will stretch by 5%. The stretch is carried out by translating both the knee and ankle transforms.  
  
The ideal value will depend on the rig and the animation but in general, a larger value will make for a smoother IK computation at the expense of more unrealistic stretching of the leg.  
  
Additional resources: [HumanDescription.armStretch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription-armStretch.html).
* * *
