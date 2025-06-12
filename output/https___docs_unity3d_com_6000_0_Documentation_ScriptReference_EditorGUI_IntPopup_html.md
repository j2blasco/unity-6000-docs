* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntPopup.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).IntPopup
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
public static int IntPopup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, int selectedValue, string[] displayedOptions, int[] optionValues, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
## Declaration
public static int IntPopup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, int selectedValue, GUIContent[] displayedOptions, int[] optionValues, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
## Declaration
public static int IntPopup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, string label, int selectedValue, string[] displayedOptions, int[] optionValues, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
## Declaration
public static int IntPopup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, int selectedValue, GUIContent[] displayedOptions, int[] optionValues, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style = EditorStyles.popup); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the field.  
label | Optional label in front of the field.  
selectedValue | The value of the option the field shows.  
displayedOptions | An array with the displayed options the user can choose from.  
optionValues | An array with the values for each option. If optionValues a direct mapping of selectedValue to displayedOptions is assumed.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
### Returns
**int** The value of the option that has been selected by the user. 
### Description
Makes an integer popup selection field.
Takes the currently selected integer as a parameter and returns the integer selected by the user.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUIIntPopup.png)  
_Int Popup in an Editor Window._
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  

// Multiplies the scale of the selected transform.  
  
class EditorGUIIntPopup : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    int selectedSize = 1;
    string[] names = { "Double", "Triple", "Quadruple" };
    int[] sizes = { 2, 3, 4 };  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) GUI[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.html) Int Popup usage")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindow<EditorGUIIntPopup>();
        window.position = new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 0, 180, 60);
        window.Show();
    }  
  
    void OnGUI()
    {
        selectedSize = EditorGUI.IntPopup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.IntPopup.html)(
            new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(3, 3, position.width - 6, 20),
            "Size:",
            selectedSize,
            names,
            sizes);  
  
        if (GUI.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUI.Button.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 25, position.width, position.height - 27), "Modify"))
        {
            Rescale();
        }
    }  
  
    void Rescale()
    {
        if (Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html))
        {
            Selection.activeTransform.localScale *= selectedSize;
        }
        else
        {
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("No Object selected, please select an object to scale.");
        }
    }
}

```

* * *
## Declaration
public static void IntPopup([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, GUIContent[] displayedOptions, int[] optionValues, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label = null); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the field.  
property | The SerializedProperty to use for the control.  
displayedOptions | An array with the displayed options the user can choose from.  
optionValues | An array with the values for each option. If optionValues a direct mapping of selectedValue to displayedOptions is assumed.  
label | Optional label in front of the field.  
### Description
* * *
