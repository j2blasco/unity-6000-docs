* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.TexturePropertySingleLine.html

#  [MaterialEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.html).TexturePropertySingleLine
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
public [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) TexturePropertySingleLine([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) textureProp); 
## Declaration
public [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) TexturePropertySingleLine([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) textureProp, [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) extraProperty1); 
## Declaration
public [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) TexturePropertySingleLine([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) textureProp, [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) extraProperty1, [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) extraProperty2); 
### Parameters
Parameter | Description  
---|---  
label | The label used for the texture property.  
textureProp | The texture property.  
extraProperty1 | First optional property inlined after the texture property.  
extraProperty2 | Second optional property inlined after the extraProperty1.  
### Returns
**Rect** Returns the Rect used. 
### Description
Method for showing a texture property control with additional inlined properites.
This method can be used if multiple controls is wanted on the same line. The texture is shown using the mini thumbnail. Usefull for compact representation of properties of up to three material properties. Additional resources: [TexturePropertyTwoLines](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.TexturePropertyTwoLines.html), [ShaderGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.html).
* * *
