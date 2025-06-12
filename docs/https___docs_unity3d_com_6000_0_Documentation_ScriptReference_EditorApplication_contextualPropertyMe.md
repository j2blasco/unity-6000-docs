* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-contextualPropertyMenu.html

#  [EditorApplication](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.html).contextualPropertyMenu
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
[EditorApplication.SerializedPropertyCallbackFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication.SerializedPropertyCallbackFunction.html) contextualPropertyMenu; 
### Description
Callback raised whenever the user context-clicks on a property in an Inspector.
This callback is useful to add custom contextual menu items which can perform operations on a particular property.
```
//This script creates a new menu item named "Example" in the **Window** dropdown menu. Press this to create the Example window.  
  
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System.Collections;  
  
public class Example : EditorWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.html)
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Window/Example")]  
  
    public static void  ShowWindow()
    {
        EditorWindow.GetWindow[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorWindow.GetWindow.html)(typeof(Example));
    }  
  
    void OnEnable()
    {
        EditorApplication.contextualPropertyMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-contextualPropertyMenu.html) += OnPropertyContextMenu;
    }  
  
    void OnDestroy()
    {
        EditorApplication.contextualPropertyMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorApplication-contextualPropertyMenu.html) -= OnPropertyContextMenu;
    }  
  
    void OnPropertyContextMenu(GenericMenu[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GenericMenu.html) menu, SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property)
    {
        // show a custom menu item only for Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) properties
        if (property.propertyType != SerializedPropertyType.Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Vector3.html))
            return;  
  
        // and only when called on a Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) component
        if (property.serializedObject.targetObject.GetType() != typeof(Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html)))
            return;  
  
        var propertyCopy = property.Copy();
        menu.AddItem(new GUIContent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GUIContent.html)("Randomize Vector"), false, () =>
        {
            propertyCopy.vector3Value = Random.insideUnitSphere[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random-insideUnitSphere.html) * 5;
            propertyCopy.serializedObject.ApplyModifiedProperties();
        });
    }
}

```

* * *
