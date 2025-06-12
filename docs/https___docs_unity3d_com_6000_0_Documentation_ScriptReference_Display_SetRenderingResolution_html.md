* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.SetRenderingResolution.html

#  [Display](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html).SetRenderingResolution
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
public void SetRenderingResolution(int w, int h); 
### Parameters
Parameter | Description  
---|---  
w | The rendering width in pixels.  
h | The rendering height in pixels.  
### Description
Sets rendering resolution for the display.
This method is only supported on Android and iOS platforms. On Windows platforms, you can use [Display.Activate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.Activate.html) or [Display.SetParams](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.SetParams.html) instead.  
  
You can set the rendering resolution as different to the native display resolution. Refer to [systemWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-systemWidth.html) and [systemHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display-systemHeight.html).
* * *
