* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.GetArrayElementAtIndex.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).GetArrayElementAtIndex
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
public [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) GetArrayElementAtIndex(int index); 
### Description
Returns the element at the specified index in the array.
Additional resources: [isArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-isArray.html), [arraySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-arraySize.html), [Next](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.Next.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public class ArrayExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public int[] m_data;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) GetArrayElementAtIndex Example")]
    static void Example()
    {
        ArrayExample obj = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<ArrayExample>();
        obj.m_data = new int[] { 3, 2, 1 };  
  
        SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(obj);
        SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) property = serializedObject.FindProperty("m_data");  
  
        for (int i = 0; i < property.arraySize; i++)
        {
            SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) element = property.GetArrayElementAtIndex(i);  
  
            //Will print
            //m_data.Array.data[0] : 3
            //m_data.Array.data[1] : 2
            //m_data.Array.data[2] : 1
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(element.propertyPath + " : " + element.intValue);
        }
    }
}

```

* * *
