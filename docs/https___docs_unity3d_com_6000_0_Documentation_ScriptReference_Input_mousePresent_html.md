* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input-mousePresent.html

#  [Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Input.html).mousePresent
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
mousePresent; 
### Description
Indicates if a mouse device is detected.
**Note** : This API is part of the legacy Input Manager. The recommended best practice is that you don't use this API in new projects. For new projects, use the Input System package. To learn more about input, refer to [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/Input.html).  
  
On Windows, Android and Metro platforms, this function does actual mouse presence detection, so may return true or false. On Linux, Mac, WebGL, this function will always return true. On iOS and console platforms, this function will always return false.
* * *
