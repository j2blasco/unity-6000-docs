* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-isArray.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).isArray
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
isArray; 
### Description
Is this property an array? (Read Only)
Additional resources: [arraySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-arraySize.html), [GetArrayElementAtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.GetArrayElementAtIndex.html).
```
using System.Text;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
// Example showing the structure of SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) objects that comprise an Array property exposed by SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html).
// Often this structure can be ignored and SerializedProperty.arraySize[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-arraySize.html) and SerializedProperty.GetArrayElementAtIndex[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.GetArrayElementAtIndex.html)(0)
// are convenient to jump straight to the size and data content.
// But, because the specific structure is exposed when using SerializedProperty.Next[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.Next.html) and SerializedProperty.propertyPath[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyPath.html),
// some understanding of this structure can be useful.
public class StructureOfArrayExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    // Serialized array
    // Note: The example would behave the same way if it was List<int>
    public string[] m_Data;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html)/Array Structure Example")]
    static void MenuCallback()
    {
        var log = new StringBuilder();  
  
        StructureOfArrayExample obj = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<StructureOfArrayExample>();
        obj.m_Data = new string[] { "zero", "one" };  
  
        SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(obj);  
  
        // Top level property represents the entire array
        SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) serializedProperty = serializedObject.FindProperty("m_Data");
        ReportPropertyDetails(serializedProperty, log);  
  
        // Next element is a structural element ".Array".
        // This does not take any space in the serialized data, and acts much the same as the top level property
        bool visitChildren = true;
        serializedProperty.Next(visitChildren);
        ReportPropertyDetails(serializedProperty, log);  
  
        // First nested child is ".Array.size", which stores the number of elements of the array
        serializedProperty.Next(visitChildren);
        ReportPropertyDetails(serializedProperty, log);  
  
        // Next comes the first array element, ".Array.data[0]".
        // In this case it is the string "zero".  Strings are also represented as Arrays in SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html).
        serializedProperty.Next(visitChildren);
        ReportPropertyDetails(serializedProperty, log);  
  
        // Skip past the nested content of the first string to get to the next string ("one")
        visitChildren = false;
        serializedProperty.Next(visitChildren);
        ReportPropertyDetails(serializedProperty, log);  
  
        //Will log:
        //Property path: 'm_Data' type: 'Generic' isArray: True depth: 0
        //Property path: 'm_Data.Array' type: 'Generic' isArray: True depth: 0
        //Property path: 'm_Data.Array.size' type: 'ArraySize' isArray: False depth: 1
        //Property path: 'm_Data.Array.data[0]' type: 'String' isArray: True depth: 1
        //Property path: 'm_Data.Array.data[1]' type: 'String' isArray: True depth: 1
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(log.ToString());
    }  
  
    static void ReportPropertyDetails(SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) prop, StringBuilder log)
    {
        log.AppendLine($"Property path: \'{prop.propertyPath}\' type: \'{prop.propertyType}\' isArray: {prop.isArray} depth: {prop.depth}");
    }
}

```

* * *
