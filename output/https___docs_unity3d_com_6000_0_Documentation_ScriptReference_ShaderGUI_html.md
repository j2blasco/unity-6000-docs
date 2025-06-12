* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.html

# ShaderGUI
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
Abstract class to derive from for defining custom GUI for shader properties and for extending the material preview.
Derive from this class for controlling how shader properties should be presented. For a shader to use this custom GUI use the 'CustomEditor' property in the shader. Note that CustomEditor can also be used for classes deriving from MaterialEditor (search for: Custom Material Editors). Note: Only the ShaderGUI approach works with Substance materials this is therefore the recommended approach to custom gui for shaders. See [ShaderGUI.OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.OnGUI.html), [ShaderGUI.OnMaterialPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.OnMaterialPreviewGUI.html), [ShaderGUI.OnMaterialPreviewSettingsGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.OnMaterialPreviewSettingsGUI.html).  
  

```
using System.Collections.Generic;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System.Linq;  
  
public class CustomShaderGUI : ShaderGUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.html)
{
    override public void OnGUI(MaterialEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialEditor.html) materialEditor, MaterialProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialProperty.html)[] properties)
    {
        // render the shader properties using the default GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html)
        base.OnGUI(materialEditor, properties);  
  
        // get the current keywords from the material
        Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html) targetMat = materialEditor.target as Material[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.html);
        string[] keyWords = targetMat.shaderKeywords;  
  
        // see if redify is set, then show a checkbox
        bool redify = keyWords.Contains("REDIFY_ON");
        EditorGUI.BeginChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.BeginChangeCheck.html)();
        redify = EditorGUILayout.Toggle[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.Toggle.html)("Redify material", redify);
        if (EditorGUI.EndChangeCheck[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EndChangeCheck.html)())
        {
            // if the checkbox is changed, reset the shader keywords
            var keywords = new List<string> { redify ? "REDIFY_ON" : "REDIFY_OFF" };
            targetMat.shaderKeywords = keywords.ToArray();
            EditorUtility.SetDirty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetDirty.html)(targetMat);
        }
    }
}

```

### Public Methods
Method | Description  
---|---  
[AssignNewShaderToMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.AssignNewShaderToMaterial.html) | This method is called when a new shader has been selected for a Material.  
[OnClosed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.OnClosed.html) | This method is called when the ShaderGUI is being closed.  
[OnGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.OnGUI.html) | To define a custom shader GUI use the methods of materialEditor to render controls for the properties array.  
[OnMaterialPreviewGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.OnMaterialPreviewGUI.html) | Override for extending the rendering of the Preview area or completly replace the preview (by not calling base.OnMaterialPreviewGUI).  
[OnMaterialPreviewSettingsGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.OnMaterialPreviewSettingsGUI.html) | Override for extending the functionality of the toolbar of the preview area or completly replace the toolbar by not calling base.OnMaterialPreviewSettingsGUI.  
[ValidateMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.ValidateMaterial.html) | When the user loads a Material using this ShaderGUI into memory or changes a value in the Inspector, the Editor calls this method.  
### Static Methods
Method | Description  
---|---  
[FindProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderGUI.FindProperty.html) | Find shader properties.  
* * *
