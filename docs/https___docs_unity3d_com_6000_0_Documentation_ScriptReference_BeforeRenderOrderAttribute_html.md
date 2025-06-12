* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BeforeRenderOrderAttribute.html

# BeforeRenderOrderAttribute
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Use this BeforeRenderOrderAttribute when you need to specify a custom callback order for Application.onBeforeRender.
[Application.onBeforeRender](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-onBeforeRender.html) will reorder all registered events recievers and call them in order, from lowest to highest, based on this attribute. No attribute represents an order of 0.
### Properties
Property | Description  
---|---  
[order](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BeforeRenderOrderAttribute-order.html) | The order, lowest to highest, that the Application.onBeforeRender event recievers will be called in.  
### Constructors
Constructor | Description  
---|---  
[BeforeRenderOrderAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BeforeRenderOrderAttribute-ctor.html) | When applied to methods, specifies the order called during Application.onBeforeRender events.  
* * *
