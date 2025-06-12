* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.TexturePropertyTwoLines.html

#  [MaterialEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.html).TexturePropertyTwoLines
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
public [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) TexturePropertyTwoLines([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) textureProp, [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) extraProperty1, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label2, [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) extraProperty2); 
### Parameters
Parameter | Description  
---|---  
label | The label used for the texture property.  
textureProp | The texture property.  
extraProperty1 | First extra property inlined after the texture property.  
label2 | Label for the second extra property (on a new line and indented).  
extraProperty2 | Second property on a new line below the texture.  
### Returns
**Rect** Returns the Rect used. 
### Description
Method for showing a compact layout of properties.
The texture is shown using the mini thumbnail that fits on a single line. The first extra property is shown inlined after the texture property and the second extra property is shown below on a new line with it's own label. Additional resources: [TexturePropertySingleLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.TexturePropertySingleLine.html), [ShaderGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.html).
* * *
