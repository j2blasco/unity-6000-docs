* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.FindPropertyRelative.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).FindPropertyRelative
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
public [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) FindPropertyRelative(string relativePropertyPath); 
### Description
Retrieves the SerializedProperty at a relative path to the current property.
When the SerializedProperty references a compound type, such as a struct, class or array, then this method can be used to lookup a child property by name.
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SerializePropertyFindPropertyRelative : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    [System.Serializable]
    public struct NestedData
    {
        public int x;
        public int y;
    };
    public NestedData m_data;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) FindPropertyRelative Example")]
    static void FindPropertyRelativeExample()
    {
        var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializePropertyFindPropertyRelative>();  
  
        // Change the values of the struct using SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)
        using (var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject))
        {
            var data = serializedObject.FindProperty("m_data");  
  
            SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) x = data.FindPropertyRelative("x");
            x.intValue = 1;  
  
            SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) y = data.FindPropertyRelative("y");
            y.intValue = 2;  
  
            serializedObject.ApplyModifiedProperties();
        }  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Value of data after update: {scriptableObject.m_data.x}, {scriptableObject.m_data.y}");
    }
}

```

* * *
