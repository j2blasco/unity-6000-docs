* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.Unsubscribe.html

#  [GraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings.html).Unsubscribe
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
public static void Unsubscribe(Action<TChild,string> callback); 
### Parameters
Parameter | Description  
---|---  
callback | The callback that is registered to listen to changes.  
### Description
Cancels any subscription to changes of properties of a settings object implemented with the [IRenderPipelineGraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IRenderPipelineGraphicsSettings.html) interface.
* * *
