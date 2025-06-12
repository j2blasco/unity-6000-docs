* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html

# CustomEditor
class in UnityEditor
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
Tells an [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) class which run-time type it's an editor for.
When you make a custom editor for a component, put this attribute on the editor class.  
  
To set which `Editor` classes are active for the current Render Pipeline Asset, add a [SupportedOnRenderPipelineAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedOnRenderPipelineAttribute.html) underneath the attribute.  
  
Additional resources: [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) class, [SupportedOnRenderPipelineAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SupportedOnRenderPipelineAttribute.html).
### Properties
Property | Description  
---|---  
[isFallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor-isFallback.html) | If true, match this editor only if all non-fallback editors do not match. Defaults to false.  
### Constructors
Constructor | Description  
---|---  
[CustomEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor-ctor.html) | Defines which object type the custom editor class can edit.  
* * *
