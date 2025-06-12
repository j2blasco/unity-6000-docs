* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ColorField.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).ColorField
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
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) ColorField([Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value, params GUILayoutOption[] options); 
## Declaration
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) ColorField(string label, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value, params GUILayoutOption[] options); 
## Declaration
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) ColorField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value, params GUILayoutOption[] options); 
## Declaration
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) ColorField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value, bool showEyedropper, bool showAlpha, bool hdr, params GUILayoutOption[] options); 
**Obsolete** Use EditorGUILayout.ColorField(GUIContent label, Color value, bool showEyedropper, bool showAlpha, bool hdr, params GUILayoutOption[] options).
## Declaration
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) ColorField([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value, bool showEyedropper, bool showAlpha, bool hdr, [ColorPickerHDRConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorPickerHDRConfig.html) hdrConfig, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Optional label to display in front of the field.  
value | The color to edit.  
showEyedropper | If true, the color picker should show the eyedropper control. If false, don't show it.  
showAlpha | If true, allow the user to set an alpha value for the color. If false, hide the alpha component.  
hdr | If true, treat the color as an HDR value. If false, treat it as a standard LDR value.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**Color** The color selected by the user. 
### Description
Make a field for selecting a [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html).
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/MassiveColorChange.png)   
_Change the color of the selected GameObjects._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Change the color of the selected GameObjects.  
  
public class ExampleClass : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) matColor = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Mass Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) Change")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindow(typeof(ExampleClass));
        window.Show();
    }  
  
    void OnGUI()
    {
        matColor = EditorGUILayout.ColorField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.ColorField.html)("New Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)", matColor);  
  
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Change!"))
            ChangeColors();
    }  
  
    private void ChangeColors()
    {
        if (Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html))
            foreach (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) t in Selection.gameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-gameObjects.html))
            {
                Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend = t.GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();  
  
                if (rend != null)
                    rend.sharedMaterial.color = matColor;
            }
    }
}

```

* * *
