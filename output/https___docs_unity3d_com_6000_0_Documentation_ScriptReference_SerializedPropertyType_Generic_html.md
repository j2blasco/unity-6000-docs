* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Generic.html

#  [SerializedPropertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.html).Generic
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
### Description
Represents an array, list, struct or class.
The Generic type is used for compound types that are serialized in-line:   
- Arrays and lists.   
- Structs that are user defined (e.g. not a built in Unity type).   
- Classes that are serialized 'by value' (e.g. referenced without the [SerializeReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html) attribute).   
- Certain built in Unity structs, when they do not have dedicated SerializedPropertyType enum value. For example [RectOffset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RectOffset.html) is Generic, but [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) is [SerializedPropertyType.Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Vector3.html).   
  
  
Note: The term Generic, when used as a SerializedProperty type, should not be confused with the unrelated C# feature of Generic classes and methods.  
  
Additional resources: [SerializedProperty.isArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-isArray.html), [SerializedPropertyType.ManagedReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.ManagedReference.html), [SerializedPropertyType.ObjectReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.ObjectReference.html)
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Text;
using UnityEngine;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using System.Collections.Generic;  
  
namespace GenericObjectTypeExample
{
    [Serializable]
    public struct ExampleStruct
    {
        public int m_Field;
    };  
  
    [Serializable]
    public class ExampleClass
    {
        public int m_Field;
    };  
  
    public class GenericTypeExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
    {
        // All these fields will be serialized
        public int[] m_ArrayOfInt;
        public List<int> m_ListOfInt;
        public ExampleStruct m_ExampleStruct = new ExampleStruct() { m_Field = 1 };
        public ExampleClass m_ExampleClass = new ExampleClass() { m_Field = 2 };  
  
        [SerializeReference[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializeReference.html)]
        public ExampleClass m_ManagedClass = new ExampleClass() { m_Field = 3 };  
  
        [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedPropertyType[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.html) Generic Example")]
        static void GenericExample()
        {
            var scriptableObject = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<GenericTypeExample>();
            using (var serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(scriptableObject))
            {
                var report = new StringBuilder();  
  
                // Generic
                ReportType(report, serializedObject, "m_ArrayOfInt");
                ReportType(report, serializedObject, "m_ListOfInt");
                ReportType(report, serializedObject, "m_ExampleStruct");
                ReportType(report, serializedObject, "m_ExampleClass");  
  
                // Not Generic
                ReportType(report, serializedObject, "m_ManagedClass");  
  
                Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)(report.ToString());  
  
                AccessGenericValues(serializedObject);
            }
        }  
  
        static void AccessGenericValues(SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject)
        {
            // "generic" type struct and objects can be retrieved directly with boxedValue
            ExampleStruct structValues = (ExampleStruct)serializedObject.FindProperty("m_ExampleStruct").boxedValue;  
  
            // Alternatively individual fields can be read
            int fieldInStruct = serializedObject.FindProperty("m_ExampleStruct.m_Field").intValue;  
  
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Value of field in struct: {structValues.m_Field}, Value of field direct read: {fieldInStruct}");  
  
            // Similarly boxedValue supports writing to an inline class
            SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) inlineClass = serializedObject.FindProperty("m_ExampleClass");  
  
            // Serialize new state in a single call
            inlineClass.boxedValue = new ExampleClass() { m_Field = 4 };  
  
            // Individual fields can also be accessed
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Value of field in class after write: {inlineClass.FindPropertyRelative("m_Field").intValue}");  
  
            serializedObject.ApplyModifiedProperties();
        }  
  
        static void ReportType(StringBuilder report, SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject, string propertyPath)
        {
            var serializedProperty = serializedObject.FindProperty(propertyPath);
            report.AppendLine($"{propertyPath} has type {serializedProperty.propertyType}");
        }
    }
}

```

* * *
