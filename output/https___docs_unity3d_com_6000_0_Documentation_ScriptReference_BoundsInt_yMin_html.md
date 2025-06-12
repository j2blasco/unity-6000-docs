* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt-yMin.html

#  [BoundsInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.html).yMin
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
yMin; 
### Description
The minimal y point of the box.
Only points with a y component greater than or equal to this value are contained in the box.
Sets the minimum value of [BoundsInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.html)'s y point. If you enter a minimum value that is greater than the current maximum value, then the entered value becomes the new maximum value and the previous maximum value becomes the new minimum value. The position and size of the [BoundsInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BoundsInt.html) is then adjusted based on the new minimum and maximum values.
* * *
