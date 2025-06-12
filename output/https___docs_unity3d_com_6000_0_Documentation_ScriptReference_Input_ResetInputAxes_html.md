* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.ResetInputAxes.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).ResetInputAxes
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
public static void ResetInputAxes(); 
### Description
Resets all input. After ResetInputAxes all axes return to 0 and all buttons return to 0 for one frame.
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
This can be useful when respawning the player and you don't want any input from keys that might still be held down.
* * *
