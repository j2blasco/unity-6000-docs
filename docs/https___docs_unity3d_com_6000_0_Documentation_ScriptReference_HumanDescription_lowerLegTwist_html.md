* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription-lowerLegTwist.html

#  [HumanDescription](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription.html).lowerLegTwist
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
lowerLegTwist; 
### Description
Defines how the lower leg's roll/twisting is distributed between the knee and ankle.
When the lower leg needs to twist or roll based on IK, `lowerLegTwist` (a weighted range of 0..1) determines how much rotation is applied to the knee and ankle. When `lowerLegTwist` is set to 0, the twist applies entirely to the knee. When set to 1, the twist applies entirely to the ankle. The default value of 0.5 evenly distributes the twist between both the knee and the ankle.  
  
Additional resources: [HumanDescription.upperArmTwist](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription-upperArmTwist.html), [HumanDescription.lowerArmTwist](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription-lowerArmTwist.html), [HumanDescription.upperLegTwist](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HumanDescription-upperLegTwist.html).
* * *
