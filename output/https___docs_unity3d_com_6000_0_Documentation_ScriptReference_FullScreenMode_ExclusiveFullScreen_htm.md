* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMode.ExclusiveFullScreen.html

#  [FullScreenMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMode.html).ExclusiveFullScreen
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
### Description
Windows platforms only. Sets your application so it has sole full-screen use of a display. 
Unlike [FullScreenMode.FullScreenWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMode.FullScreenWindow.html), this mode changes the operating system resolution of the display to match the application's chosen resolution. On platforms other than Windows, this mode falls back to [FullScreenMode.FullScreenWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMode.FullScreenWindow.html).  
  
**Notes** : 
  * This mode isn't supported in applications that use Vulkan graphics API.
  * Using this mode might negatively affect performance of your application. Consider using other full-screen modes, such as [FullScreenMode.FullScreenWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMode.FullScreenWindow.html).
  * DirectX 11 doesn't support [HDR Output](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-output.html) in this mode. For HDR Output on DirectX 11, use [FullScreenMode.FullScreenWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/FullScreenMode.FullScreenWindow.html) instead.


* * *
