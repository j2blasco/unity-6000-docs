* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-arraySize.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).arraySize
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
arraySize; 
### Description
The number of elements in the array.
If the SerializedObject contains a single object, this property returns the number of elements in the array.  
  
If the SerializedObject contains multiple objects, this property returns the smallest number of elements. This is done so that iteration of the SerializedObject only exposes properties found in all objects.  
  
If there are multiple objects and the smallest array size is larger than [SerializedObject.maxArraySizeForMultiEditing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-maxArraySizeForMultiEditing.html) then this property returns 0 and the elements cannot be retrieved with [SerializedProperty.GetArrayElementAtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.GetArrayElementAtIndex.html).  
  
Setting this property to a size smaller than the current size discards elements from the end, retaining the existing element content for the remaining elements. Setting this property to a larger size increases the array size by appending new elements at the end. The values of those new elements are undefined until explicitly assigned some desired content, as demonstrated in the second example below.  
  
Additional resources: [isArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-isArray.html), [minArraySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-minArraySize.html), [GetArrayElementAtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.GetArrayElementAtIndex.html), [InsertArrayElementAtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.InsertArrayElementAtIndex.html), [DeleteArrayElementAtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.DeleteArrayElementAtIndex.html), [ClearArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.ClearArray.html), [SerializedObject.targetObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-targetObjects.html).
```
using System.Collections.Generic;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SerializePropertyArraySizeExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public List<string> m_ListOfStrings = new List<string> { "zero", "one", "two" };
    public string m_NotInArray = "blah";  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html)/ArraySize Example")]
    static void ArraySizeExample()
    {
        var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializePropertyArraySizeExample>();  
  
        using (var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject))
        {
            var arrayProperty = serializedObject.FindProperty("m_ListOfStrings");
            var arraySize = arrayProperty.arraySize;
            var arrayElement = arrayProperty.GetArrayElementAtIndex(0);  
  
            var concatenated = "Combined array contents: ";
            for (int i = 0; i < arraySize; i++, arrayElement.Next(false))
            {
                concatenated += arrayElement.stringValue + " ";
            }
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(concatenated);
        }
    }
}

```

```
using System.Collections.Generic;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);  
  
public class SerializePropertyArrayResizeExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public List<string> m_ListOfStrings;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html)/ArraySize Example 2")]
    static void MenuCallback()
    {
        var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<SerializePropertyArrayResizeExample>();  
  
        using (var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject))
        {
            var arrayProperty = serializedObject.FindProperty("m_ListOfStrings");  
  
            // Allocate an initial size of the array
            arrayProperty.arraySize = 2;  
  
            // Set the desired initial content for the new elements
            arrayProperty.GetArrayElementAtIndex(0).stringValue = "zero";
            arrayProperty.GetArrayElementAtIndex(1).stringValue = "one";  
  
            // Append another element
            arrayProperty.arraySize++;
            arrayProperty.GetArrayElementAtIndex(arrayProperty.arraySize - 1).stringValue = "two";  
  
            serializedObject.ApplyModifiedProperties();
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Combined array contents: " + string.Join(" ", scriptableObject.m_ListOfStrings));
        }
    }
}

```

* * *
