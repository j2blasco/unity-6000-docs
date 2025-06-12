* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.SetErrorMaterial.html

#  [BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html).SetErrorMaterial
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
public void SetErrorMaterial([Material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) material); 
### Parameters
Parameter | Description  
---|---  
material | The material to display when there is a problem with a shader or material. If this value is `null`, Unity does not display anything.  
### Description
Set the error material for the `BatchRendererGroup`. This material will be used internally by Unity to render the draw commands referring to erroneous shaders. You can also pass 'null' to this method to unset the material.
When you render with a `BatchRendererGroup` and there is a problem with the shader or material, Unity doesn't display the default [error shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-error.html). Use this function to display a given material instead. **Note:** For performance reasons, Unity only displays this material in the Editor and in development builds. Unity does not display this material in release builds.
* * *
