* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.TexturePropertyWithHDRColor.html

#  [MaterialEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.html).TexturePropertyWithHDRColor
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
public [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) TexturePropertyWithHDRColor([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) textureProp, [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) colorProperty, bool showAlpha); 
**Obsolete** Use TexturePropertyWithHDRColor(GUIContent label, MaterialProperty textureProp, MaterialProperty colorProperty, bool showAlpha).
## Declaration
public [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) TexturePropertyWithHDRColor([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) textureProp, [MaterialProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html) colorProperty, [ColorPickerHDRConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorPickerHDRConfig.html) hdrConfig, bool showAlpha); 
### Parameters
Parameter | Description  
---|---  
label | The label used for the texture property.  
textureProp | The texture property.  
colorProperty | The color property (will be treated as a HDR color).  
showAlpha | If false then the alpha channel information will be hidden in the GUI.  
### Returns
**Rect** Return the Rect used. 
### Description
Method for showing a texture property control with a HDR color field and its color brightness float field.
The texture is shown using the mini thumbnail. Usefull for compact representation of a texture and a HDR color. Additional resources: [TexturePropertySingleLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.TexturePropertySingleLine.html), [ShaderGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.html).
* * *
