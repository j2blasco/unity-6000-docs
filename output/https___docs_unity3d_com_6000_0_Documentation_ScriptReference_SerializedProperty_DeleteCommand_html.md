* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.DeleteCommand.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).DeleteCommand
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
public bool DeleteCommand(); 
### Description
Deletes the array element referenced by the SerializedProperty.
The serialized property can't be used anymore after calling this function. A new iterator must be created in that case.  
  
Additional resources: [DeleteArrayElementAtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.DeleteArrayElementAtIndex.html)
```
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SerializePropertyDeleteCommandExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public int[] m_Array = new int[] { 1, -1, -1, 3, -1, -1, 1, 3, -1 };  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html)/DeleteCommand Example")]
    static void MenuCallback()
    {
        var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializePropertyDeleteCommandExample>();  
  
        using (var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject))
        {
            SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) arrayProperty = serializedObject.FindProperty("m_Array");  
  
            int remaining = arrayProperty.arraySize;
            var arrayElement = remaining > 0 ? arrayProperty.GetArrayElementAtIndex(0) : null;
            while (remaining > 0)
            {
                if (arrayElement.intValue < 0)
                {
                    // Use a copy of the SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) because it cannot be used after DeleteCommand is invoked.
                    var elementToDelete = arrayElement.Copy();
                    elementToDelete.DeleteCommand();  
  
                    // The next element, if any, is now at the index of the deleted item, and arrayElement
                    // automatically points at it, hence we don't have to move ahead
                }
                else
                {
                    arrayElement.Next(false);
                }
                --remaining;
            }  
  
            serializedObject.ApplyModifiedProperties();
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Cleaned array contents: " + string.Join(" ", scriptableObject.m_Array));
        }
    }
}

```

* * *
