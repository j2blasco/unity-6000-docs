* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-minArraySize.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).minArraySize
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
minArraySize; 
### Description
The smallest number of elements in the array across all target objects. (Read Only)
If the SerializedObject contains multiple objects, this property returns the smallest number of elements. Unlike [SerializedProperty.arraySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-arraySize.html) the minimum size is returned even if it is larger than [SerializedObject.maxArraySizeForMultiEditing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-maxArraySizeForMultiEditing.html). In that case SerializedObject.maxArraySizeForMultiEditing could be increased to permit access to the array contents.  
  
When the SerializedObject contains only a single object, this property behaves in the same way as [SerializedProperty.arraySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-arraySize.html) and returns the true array size.  
  
Additional resources: [arraySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-arraySize.html), [isArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-isArray.html), [SerializedObject.targetObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-targetObjects.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class MinArraySizeExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public int[] m_data;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) MinArraySize Example")]
    static void TestMethod()
    {
        const int largeArraySize = 100; // Larger than the default maxArraySizeForMultiEditing value of 64  
  
        MinArraySizeExample obj1 = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<MinArraySizeExample>();
        obj1.m_data = new int[largeArraySize];  
  
        for (int i = 0; i < largeArraySize; i++)
            obj1.m_data[i] = i;  
  
        // Second object with its own copy of the large array
        MinArraySizeExample obj2 = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<MinArraySizeExample>();
        obj2.m_data = obj1.m_data;  
  
        // Create serialized object for manipulating both objects
        SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(new Object[] { obj1, obj2 });
        SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property = serializedObject.FindProperty("m_data");  
  
        // arraySize returns 0 but minArraySize returns largeArraySize
        Debug.LogFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html)("Array Size: {0}\nMin Array Size: {1}\nMax Array Size: {2}",
            property.arraySize, property.minArraySize, serializedObject.maxArraySizeForMultiEditing);  
  
        // Any call to GetArrayElementAtIndex() at this point would fail  
  
        // Extend the max permitted array size
        serializedObject.maxArraySizeForMultiEditing = property.minArraySize;  
  
        // Now arraySize returns largeArraySize, and the elements can be retrieved
        Debug.LogFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html)("New Array Size: {0}, Last element: {1}", property.arraySize, property.GetArrayElementAtIndex(largeArraySize - 1).intValue);
    }
}

```

* * *
