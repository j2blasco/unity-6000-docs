* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-arrayElementType.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).arrayElementType
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
arrayElementType; 
### Description
Type name of the element in an array property. (Read Only)
Returns the C# type name of the element in an array property. In the case of [SerializedPropertyType.ObjectReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.ObjectReference.html) and other internal values of SerializedPropertyType, the internal serialization type name is returned.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SerializePropertyArrayElementTypeExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    // Various kinds of lists/arrays
    public List<string> m_strings;
    public int[] m_ints;
    public List<Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html)> m_vectors;
    public GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html)[] m_gameObjects;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) arrayElementType Example")]
    static void ArrayElementTypeExample()
    {
        var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializePropertyArrayElementTypeExample>();  
  
        using (var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject))
        {
            LogType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html)(serializedObject, "m_strings");
            LogType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html)(serializedObject, "m_ints");
            LogType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html)(serializedObject, "m_vectors");
            LogType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html)(serializedObject, "m_gameObjects");
        }
    }  
  
    static void LogType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.html)(SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject, string arrayFieldName)
    {
        var arrayType = serializedObject.FindProperty(arrayFieldName).arrayElementType;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"{arrayFieldName} array type: {arrayType}");
    }
}

```

* * *
