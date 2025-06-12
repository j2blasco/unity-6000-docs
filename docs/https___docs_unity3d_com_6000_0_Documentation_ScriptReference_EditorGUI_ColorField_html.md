* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ColorField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).ColorField
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
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) ColorField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value); 
## Declaration
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) ColorField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value); 
## Declaration
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) ColorField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value); 
## Declaration
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) ColorField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value, bool showEyedropper, bool showAlpha, bool hdr); 
**Obsolete** Use EditorGUI.ColorField(Rect position, GUIContent label, Color value, bool showEyedropper, bool showAlpha, bool hdr).
## Declaration
public static [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) ColorField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) value, bool showEyedropper, bool showAlpha, bool hdr, [ColorPickerHDRConfig](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColorPickerHDRConfig.html) hdrConfig); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the field.  
label | Optional label to display in front of the field.  
value | The color to edit.  
showEyedropper | If true, the color picker should show the eyedropper control. If false, don't show it.  
showAlpha | If true, allow the user to set an alpha value for the color. If false, hide the alpha component.  
hdr | If true, treat the color as an HDR value. If false, treat it as a standard LDR value.  
### Returns
**Color** The color selected by the user. 
### Description
Makes a field for selecting a [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html).
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIColorField.png)   
_Color field in an Editor Window._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Change The color of the selected Game Objects
class EditorGUIColorField : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) matColor  = Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html);  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Mass Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) Change")]  
  
    static void Init()
    {
        var window = GetWindow<EditorGUIColorField>();
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 170, 60);
        window.Show();
    }  
  
    void OnGUI()
    {
        matColor = EditorGUI.ColorField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.ColorField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, position.width - 6, 15),
            "New Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html):",
            matColor);
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 25, position.width - 6, 30), "Change!"))
        {
            ChangeColors();
        }
    }  
  
    void ChangeColors()
    {
        if (Selection.activeGameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeGameObject.html))
        {
            foreach (GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) obj in Selection.gameObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-gameObjects.html))
            {
                Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend = obj.GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();  
  
                if (rend != null)
                {
                    rend.sharedMaterial.color = matColor;
                }
            }
        }
    }
}

```

* * *
