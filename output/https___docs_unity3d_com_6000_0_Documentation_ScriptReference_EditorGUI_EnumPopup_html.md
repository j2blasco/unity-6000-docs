* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EnumPopup.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).EnumPopup
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
public static Enum EnumPopup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, Enum selected, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
## Declaration
public static Enum EnumPopup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, Enum selected, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
## Declaration
public static Enum EnumPopup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, Enum selected, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
## Declaration
public static Enum EnumPopup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, Enum selected, Func<Enum,bool> checkEnabled = null, bool includeObsolete = false, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = null); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the field.  
label | Optional label in front of the field.  
selected | The enum option the field shows.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
includeObsolete | Set to true to include Enum values with ObsoleteAttribute. Set to false to exclude Enum values with ObsoleteAttribute.  
checkEnabled | Method called for each Enum value displayed. The specified method should return true if the option can be selected, false otherwise.  
### Returns
**Enum** The enum option that has been selected by the user. 
### Description
Makes an enum popup selection field.
Takes the currently selected enum value as a parameter and returns the enum value selected by the user. ![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIEnumPopup.png)  
_Enum Popup in an Editor Window._
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  

// Shows info of a GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) depending on the selected option  
  
public enum OPTIONS
{
    Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html) = 0,
    Rotation = 1,
    Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html) = 2,
}  
  

public class EditorGUIEnumPopup : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    OPTIONS display = OPTIONS.Position;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) Enum Popup usage")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindow(typeof(EditorGUIEnumPopup));
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 220, 80);
        window.Show();
    }  
  
    void OnGUI()
    {
        Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) selectedObj = Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html);  
  
        display = (OPTIONS)EditorGUI.EnumPopup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.EnumPopup.html)(
            new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, position.width - 6, 15),
            "Show:",
            display);  
  
        EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 20, position.width, 15),
            "Name:",
            selectedObj ? selectedObj.name : "Select an Object");
        if (selectedObj)
        {
            switch (display)
            {
                case OPTIONS.Position:
                    EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 40, position.width, 15),
                        "Position[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.html):",
                        selectedObj.position.ToString());
                    break;  
  
                case OPTIONS.Rotation:
                    EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 40, position.width, 15),
                        "Rotation:",
                        selectedObj.rotation.ToString());
                    break;  
  
                case OPTIONS.Scale:
                    EditorGUI.LabelField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.LabelField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 40, position.width, 15),
                        "Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html):",
                        selectedObj.localScale.ToString());
                    break;  
  
                default:
                    Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("Unrecognized Option");
                    break;
            }
        }  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, position.height - 25, position.width - 6, 24), "Close"))
            this.Close();
    }
}

```

* * *
