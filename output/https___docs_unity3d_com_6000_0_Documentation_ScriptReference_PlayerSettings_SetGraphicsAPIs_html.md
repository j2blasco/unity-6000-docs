* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetGraphicsAPIs.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).SetGraphicsAPIs
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
public static void SetGraphicsAPIs([BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) platform, GraphicsDeviceType[] apis); 
### Parameters
Parameter | Description  
---|---  
platform | Platform to set APIs for.  
apis | Array of graphics APIs.  
### Description
Sets the graphics APIs used on a build platform.
By default each platform is using "automatic" graphics API detection and picks the best available one (see [SetUseDefaultGraphicsAPIs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetUseDefaultGraphicsAPIs.html)). However it is possible to change that to explicitly limit the graphics APIs used. The passed APIs will be tried in the order they are given, and first available one will be used.  
  
Additional resources: [GetGraphicsAPIs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetGraphicsAPIs.html), [SetUseDefaultGraphicsAPIs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetUseDefaultGraphicsAPIs.html), [GetUseDefaultGraphicsAPIs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetUseDefaultGraphicsAPIs.html).
* * *
