* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.DeleteArrayElementAtIndex.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).DeleteArrayElementAtIndex
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
public void DeleteArrayElementAtIndex(int index); 
### Description
Delete the element at the specified index in the array.
Additional resources: [isArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-isArray.html), [InsertArrayElementAtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.InsertArrayElementAtIndex.html), [MoveArrayElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.MoveArrayElement.html), [DeleteCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.DeleteCommand.html).
```
using System.Collections.Generic;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class DeleteArrayElementAtIndexExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public List<string> m_Data;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html)/DeleteArrayElementAtIndex Example")]
    static void MenuCallback()
    {
        DeleteArrayElementAtIndexExample obj = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<DeleteArrayElementAtIndexExample>();
        obj.m_Data = new List<string>() { "The", "big", "cat", "jumped." };  
  
        SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(obj);
        SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) arrayProperty = serializedObject.FindProperty("m_Data");  
  
        arrayProperty.DeleteArrayElementAtIndex(1);  
  
        // With previous deletion index 2 now becomes the last element
        arrayProperty.DeleteArrayElementAtIndex(2);  
  
        serializedObject.ApplyModifiedProperties();  
  
        // Outputs "The cat"
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Final array contents: " + string.Join(" ", obj.m_Data));
    }
}

```

```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class DeleteArrayElementAtIndexExample2 : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public int[] m_Array = new int[] { 1, -1, -1, 3, -1, -1, 1, 3, -1 };  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html)/DeleteArrayElementAtIndex Example 2")]
    static void MenuCallback()
    {
        var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<DeleteArrayElementAtIndexExample2>();  
  
        using (var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject))
        {
            SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) arrayProperty = serializedObject.FindProperty("m_Array");  
  
            // Iterate the array removing any negative numbers
            int arraySize = arrayProperty.arraySize;
            for (int index = 0; index < arraySize;)
            {
                var arrayElement = arrayProperty.GetArrayElementAtIndex(index);
                if (arrayElement.intValue < 0)
                {
                    arrayProperty.DeleteArrayElementAtIndex(index);
                    arraySize--;
                }
                else
                {
                    index++;
                }
            }  
  
            serializedObject.ApplyModifiedProperties();
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Cleaned array contents: " + string.Join(" ", scriptableObject.m_Array));
        }
    }
}

```

* * *
