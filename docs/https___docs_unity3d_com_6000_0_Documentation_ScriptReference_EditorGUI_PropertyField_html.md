* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PropertyField.html

#  [EditorGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.html).PropertyField
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
public static bool PropertyField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, bool includeChildren = false); 
## Declaration
public static bool PropertyField([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) position, [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, bool includeChildren = false); 
### Parameters
Parameter | Description  
---|---  
position | Rectangle on the screen to use for the property field.  
property | The SerializedProperty to make a field for.  
label | Optional label to use. If not specified the label of the property itself is used. Use GUIContent.none to not display a label at all.  
includeChildren | If `true` the property including children is drawn; otherwise only the control itself (such as only a foldout but nothing below it).  
### Returns
**bool** True if the property has children and is expanded and includeChildren was set to false; otherwise false. 
### Description
Use this to make a field for a [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) in the Editor.
Additional resources: [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html), [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html).
```
//Attach a script like this to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) you would like to have a custom Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) window.  
  
using UnityEngine;  
  
public class MyScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int myInt = 90;
}

```

```
//Create a folder and name it “Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)” and place this second script within it. To do this right click within the Assets directory and go to Create>Folder[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WSA.Folder.html)
//Ensure you insert your first script’s name as a parameter in the CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html) e.g. [CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(MyScript))]  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Custom Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) using SerializedProperties.
// Make sure to put the name of the script on your GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) in here
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(MyScript))]
// Automatic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGame.Automatic.html) handling of multi-object editing, undo, and Prefab overrides.
[CanEditMultipleObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html)]  
  
public class EditorGUIPropertyField : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) m_IntProperty;  
  
    void OnEnable()
    {
        // Fetch the objects from the MyScript script to display in the inspector
        m_IntProperty = serializedObject.FindProperty("myInt");
    }  
  
    public override void OnInspectorGUI()
    {
        //The variables and GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) script are displayed in the Inspector and have the appropriate label
        EditorGUI.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUI.PropertyField.html)(new Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)(0, 300, 500, 30), m_IntProperty, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Int : "));  
  
        // Apply changes to the serializedProperty - always do this in the end of OnInspectorGUI.
        serializedObject.ApplyModifiedProperties();
    }
}

```

* * *
