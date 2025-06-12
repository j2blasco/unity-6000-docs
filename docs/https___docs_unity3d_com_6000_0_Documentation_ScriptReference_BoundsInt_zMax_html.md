* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-zMax.html

#  [BoundsInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.html).zMax
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
zMax; 
### Description
The maximal z point of the box.
Only points with a z component less than this value are contained in the box.
Sets the maximum value of [BoundsInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.html)'s z point. If you enter a maximum value that is less than the current minimum value, then the entered value becomes the new minimum value and the previous minimum value becomes the new maximum value. The position and size of the [BoundsInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.html) is then adjusted based on the new minimum and maximum values.
* * *
