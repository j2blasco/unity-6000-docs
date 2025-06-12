* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription-upperLegTwist.html

#  [HumanDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription.html).upperLegTwist
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
upperLegTwist; 
### Description
Defines how the upper leg's roll/twisting is distributed between the thigh and knee joints.
When the upper leg needs to twist or roll based on IK, `upperLegTwist` (a weighted range of 0..1) determines how much rotation is applied to the thigh and knee. When `upperLegTwist` is set to 0, the twist applies entirely to the thigh. When set to 1, the twist applies entirely to the knee. The default value of 0.5 evenly distributes the twist between both the thigh and the knee.  
  
Additional resources: [HumanDescription.lowerArmTwist](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription-lowerArmTwist.html), [HumanDescription.lowerLegTwist](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription-lowerLegTwist.html), [HumanDescription.upperArmTwist](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription-upperArmTwist.html).
* * *
