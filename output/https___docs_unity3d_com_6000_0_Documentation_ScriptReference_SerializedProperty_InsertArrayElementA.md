* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.InsertArrayElementAtIndex.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).InsertArrayElementAtIndex
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
public void InsertArrayElementAtIndex(int index); 
### Description
Insert an new element at the specified index in the array.
The value of the inserted element is undefined and should be explicitly set after calling this function.   
Additional resources: [isArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-isArray.html), [arraySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-arraySize.html), [GetArrayElementAtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.GetArrayElementAtIndex.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class InsertArrayElementAtIndexExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public string[] m_Data;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html)/InsertArrayElementAtIndex Example")]
    static void MenuCallback()
    {
        InsertArrayElementAtIndexExample obj = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<InsertArrayElementAtIndexExample>();
        obj.m_Data = new string[] { "The", "cat" };  
  
        SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(obj);
        SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) arrayProperty = serializedObject.FindProperty("m_Data");  
  
        arrayProperty.InsertArrayElementAtIndex(1);
        arrayProperty.GetArrayElementAtIndex(1).stringValue = "big";  
  
        arrayProperty.InsertArrayElementAtIndex(arrayProperty.arraySize);
        arrayProperty.GetArrayElementAtIndex(arrayProperty.arraySize - 1).stringValue = "jumped.";  
  
        serializedObject.ApplyModifiedProperties();  
  
        // Outputs "The big cat jumped."
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Final array contents: " + string.Join(" ", obj.m_Data));
    }
}

```

* * *
