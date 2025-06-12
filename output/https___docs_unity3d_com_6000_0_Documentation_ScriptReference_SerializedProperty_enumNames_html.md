* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-enumNames.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).enumNames
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
enumNames; 
### Description
Names of enumeration of an enum property.
Additional resources: [enumDisplayNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-enumDisplayNames.html), [propertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyType.html), [SerializedPropertyType.Enum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Enum.html), [enumValueIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-enumValueIndex.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public enum ExampleEnum
{
    ValueFirst = 1,
    ValueSecond = 2,
    ValueThird = 3,
}  
  
public class EnumExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public ExampleEnum MyEnum = ExampleEnum.ValueSecond;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) Enum API")]
    static void Example()
    {
        EnumExample obj = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<EnumExample>();
        SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(obj);
        SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) enumProperty = serializedObject.FindProperty("MyEnum");  
  
        //MyEnum value: 2
        //Name of current value: ValueSecond
        //DisplayName: Value Second
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("MyEnum value: " + enumProperty.intValue +
            "\nName of current value: " + enumProperty.enumNames[enumProperty.enumValueIndex] +
            "\nDisplayName: " + enumProperty.enumDisplayNames[enumProperty.enumValueIndex]);
    }
}

```

* * *
