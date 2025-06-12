* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html

#  [EditorGUILayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.html).PropertyField
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
public static bool PropertyField([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, params GUILayoutOption[] options); 
## Declaration
public static bool PropertyField([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, params GUILayoutOption[] options); 
## Declaration
public static bool PropertyField([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, bool includeChildren, params GUILayoutOption[] options); 
## Declaration
public static bool PropertyField([SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property, [GUIContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html) label, bool includeChildren, params GUILayoutOption[] options); 
### Parameters
Parameter | Description  
---|---  
property | The SerializedProperty to make a field for.  
label | Optional label to use. If not specified the label of the property itself is used. Use GUIContent.none to not display a label at all.  
includeChildren | If `true` the property including children is drawn; otherwise only the control itself (such as only a foldout but nothing below it).  
options | An optional list of layout options that specify extra layout properties. Any values passed in here will override settings defined by the `style`.  
Additional resources: [GUILayout.Width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Width.html), [GUILayout.Height](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html), [GUILayout.MinWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinWidth.html), [GUILayout.MaxWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxWidth.html), [GUILayout.MinHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MinHeight.html), [GUILayout.MaxHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.MaxHeight.html), [GUILayout.ExpandWidth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandWidth.html), [GUILayout.ExpandHeight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.ExpandHeight.html).  
### Returns
**bool** True if the property has children, is expanded, and `includeChildren` is set to false; otherwise false. You can use it to determine the `isExpanded` state of the property and customize the rendering of children if necessary. 
### Description
Make a field for [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).
Use this when you want to customise the look of the options for a GameObject in the Inspector. Use this to create fields for Serialized Properties. More information on changing the Editor is available in the [Editor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) section.  
  
Additional resources: [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html), [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html).
```
//The scripts below show how to use a propertyField to change your editor.
//Attach this first script to the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) that you would like to control. Add code in this script for any of the actions you require.  
  
using UnityEngine;  
  
public class MyGameObjectScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public int m_MyInt = 75;
    public Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) m_MyVector = new Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)(20, 1, 0);
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) m_MyGameObject;
}

```

```
//This next script shows how to call upon variables from the "MyGameObject" Script (the first script) to make custom fields in the Inspector for these variables.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
// Custom Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html) using SerializedProperties.
// Automatic[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidGame.Automatic.html) handling of multi-object editing, undo, and Prefab overrides.
[CustomEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomEditor.html)(typeof(MyGameObjectScript))]
[CanEditMultipleObjects[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CanEditMultipleObjects.html)]
public class EditorGUILayoutPropertyField : Editor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Editor.html)
{
    SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) m_IntProp;
    SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) m_VectorProp;
    SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) m_GameObjectProp;  
  
    void OnEnable()
    {
        // Fetch the objects from the GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) script to display in the inspector
        m_IntProp = serializedObject.FindProperty("m_MyInt");
        m_VectorProp = serializedObject.FindProperty("m_MyVector");
        m_GameObjectProp = serializedObject.FindProperty("m_MyGameObject");
    }  
  
    public override void OnInspectorGUI()
    {
        //The variables and GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) from the MyGameObject script are displayed in the Inspector with appropriate labels
        EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)(m_IntProp, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Int Field"), GUILayout.Height[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUILayout.Height.html)(20));
        EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)(m_VectorProp, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Vector Object"));
        EditorGUILayout.PropertyField[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUILayout.PropertyField.html)(m_GameObjectProp, new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Game Object"));  
  
        // Apply changes to the serializedProperty - always do this at the end of OnInspectorGUI.
        serializedObject.ApplyModifiedProperties();
    }
}

```

* * *
