* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.ShaderProperty.html

#  [MaterialEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.html).ShaderProperty
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
public void ShaderProperty([MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) prop, string label); 
## Declaration
public void ShaderProperty([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) prop, string label); 
### Description
Handes UI for one shader property.
This function will draw appropriate UI for the given shader property, depending on its type.  
  
Any custom [MaterialPropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyDrawer.html) objects defined for this property in the shader will also be applied. If you want to draw the "default" UI without any custom drawers, use [DefaultShaderProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.DefaultShaderProperty.html) function.  
  
Additional resources: [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html), [MaterialPropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyDrawer.html).
* * *
