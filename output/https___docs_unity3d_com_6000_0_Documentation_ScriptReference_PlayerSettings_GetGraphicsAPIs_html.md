* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetGraphicsAPIs.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).GetGraphicsAPIs
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
## Declaration
public static GraphicsDeviceType[] GetGraphicsAPIs([BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) platform); 
### Parameters
Parameter | Description  
---|---  
platform | Platform to get APIs for.  
### Returns
**GraphicsDeviceType[]** Array of graphics APIs. 
### Description
Get graphics APIs to be used on a build platform.
By default each platform is using "automatic" graphics API detection and picks the best available one (see [GetUseDefaultGraphicsAPIs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetUseDefaultGraphicsAPIs.html)). However it is possible to change that to explicitly limit the graphics APIs used via [SetGraphicsAPIs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetGraphicsAPIs.html).  
  
Additional resources: [SetGraphicsAPIs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetGraphicsAPIs.html), [SetUseDefaultGraphicsAPIs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetUseDefaultGraphicsAPIs.html), [GetUseDefaultGraphicsAPIs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetUseDefaultGraphicsAPIs.html).
* * *
