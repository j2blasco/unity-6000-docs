* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RecreatePipelineOnChangeAttribute.html

# RecreatePipelineOnChangeAttribute
class in UnityEngine.Rendering
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
This attribute is used on field of a [IRenderPipelineGraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.IRenderPipelineGraphicsSettings.html) to ensure pipeline would be recreated if the value is changed.
If the settings change through the default inspector or through the Reset or through SetValueAndNotify, RenderPipelineEditorUtility.RecreateRenderPipelineMatchingSettings is called onto the settings.
* * *
