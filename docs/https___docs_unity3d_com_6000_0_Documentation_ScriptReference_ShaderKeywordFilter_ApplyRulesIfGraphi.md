* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.ApplyRulesIfGraphicsAPIAttribute-ctor.html

# ApplyRulesIfGraphicsAPIAttribute Constructor
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
public ApplyRulesIfGraphicsAPIAttribute(params GraphicsDeviceType[] graphicsDeviceTypes); 
### Parameters
Parameter | Description  
---|---  
graphicsDeviceTypes | The array of graphics APIs to match to.  
### Description
Enable or disable shader keyword filter attributes based on the graphics API.
Unity enables filter attributes if the current build target matches any of the `graphicsDeviceTypes`.
* * *
