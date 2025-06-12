* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.EditorGraphicsSettings.SetRenderPipelineGlobalSettingsAsset.html

#  [EditorGraphicsSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.EditorGraphicsSettings.html).SetRenderPipelineGlobalSettingsAsset
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
public static void SetRenderPipelineGlobalSettingsAsset(Type renderPipelineType, [Rendering.RenderPipelineGlobalSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGlobalSettings.html) newSettings); 
## Declaration
public static void SetRenderPipelineGlobalSettingsAsset([Rendering.RenderPipelineGlobalSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGlobalSettings.html) newSettings); 
### Parameters
Parameter | Description  
---|---  
renderPipelineType | A valid [RenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html) type.  
newSettings | A valid instance of the [RenderPipelineGlobalSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGlobalSettings.html) asset to create the association or null to remove the association.  
### Description
The method sets the association between the given [RenderPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipeline.html) asset and the [RenderPipelineGlobalSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderPipelineGlobalSettings.html) asset.
* * *
