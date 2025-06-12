* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.SetAdditionalBakeDelegate.html

#  [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.html).SetAdditionalBakeDelegate
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
## Declaration
public static void SetAdditionalBakeDelegate([Lightmapping.AdditionalBakeDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.AdditionalBakeDelegate.html) del); 
### Description
Set a delegate that bakes additional data. This delegates must set its done parameter to true once baking is finished to unlock the baking pipeline. Must be reset by calling ResetDelegate again.
* * *
