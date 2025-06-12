* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntPopup.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).IntPopup
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
public static int IntPopup(int selectedValue, string[] displayedOptions, int[] optionValues, params GUILayoutOption[] options); 
## Declaration
public static int IntPopup(int selectedValue, string[] displayedOptions, int[] optionValues, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static int IntPopup(int selectedValue, GUIContent[] displayedOptions, int[] optionValues, params GUILayoutOption[] options); 
## Declaration
public static int IntPopup(int selectedValue, GUIContent[] displayedOptions, int[] optionValues, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static int IntPopup(string label, int selectedValue, string[] displayedOptions, int[] optionValues, params GUILayoutOption[] options); 
## Declaration
public static int IntPopup(string label, int selectedValue, string[] displayedOptions, int[] optionValues, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static int IntPopup([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, int selectedValue, GUIContent[] displayedOptions, int[] optionValues, params GUILayoutOption[] options); 
## Declaration
public static int IntPopup([GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, int selectedValue, GUIContent[] displayedOptions, int[] optionValues, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
label | Optional label in front of the field.  
selectedValue | The value of the option the field shows.  
displayedOptions | An array with the displayed options the user can choose from.  
optionValues | An array with the values for each option.  
style | Optional [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html).  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**int** The value of the option that has been selected by the user. 
### Description
Make an integer popup selection field.
Takes the currently selected integer as a parameter and returns the integer selected by the user.  
  
![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/EditorGUILayoutIntPopup.png)  
_Rescales the current selected GameObject._
```
// Simple Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) Script that lets you rescale the current selected GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html).
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class IntPopupExample : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    int   selectedSize = 1;
    string[] names = new string[] {"Normal", "Double", "Quadruple"};
    int[] sizes = {1, 2, 4};  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/Int Popup usage")]
    static void Init()
    {
        EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html) window = GetWindow(typeof(IntPopupExample));
        window.Show();
    }  
  
    void OnGUI()
    {
        selectedSize = EditorGUILayout.IntPopup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.IntPopup.html)("Resize Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html): ", selectedSize, names, sizes);
        if (GUILayout.Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Button.html)("Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html)"))
            ReScale();
    }  
  
    void ReScale()
    {
        if (Selection.activeTransform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Selection-activeTransform.html))
            Selection.activeTransform.localScale =
                new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(selectedSize, selectedSize, selectedSize);
        else
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("No Object selected, please select an object to scale.");
    }
}

```

* * *
**Obsolete** This function is obsolete and the style is not used.
## Declaration
public static void IntPopup([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, GUIContent[] displayedOptions, int[] optionValues, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, [GUIStyle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIStyle.html) style, params GUILayoutOption[] options); 
## Declaration
public static void IntPopup([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, GUIContent[] displayedOptions, int[] optionValues, params GUILayoutOption[] options); 
## Declaration
public static void IntPopup([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, GUIContent[] displayedOptions, int[] optionValues, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
property | The value of the option the field shows.  
displayedOptions | An array with the displayed options the user can choose from.  
optionValues | An array with the values for each option.  
label | Optional label in front of the field.  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Description
Make an integer popup selection field.
* * *
