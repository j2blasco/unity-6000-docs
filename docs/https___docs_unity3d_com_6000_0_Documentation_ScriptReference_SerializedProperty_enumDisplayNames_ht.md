* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-enumDisplayNames.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).enumDisplayNames
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
enumDisplayNames; 
### Description
Display-friendly names of enumeration of an enum property.
Similar to enumNames, but formatted with spaces and capitalization.  
  
Additional resources: [enumNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-enumNames.html), [propertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyType.html), [SerializedPropertyType.Enum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Enum.html), [enumValueIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-enumValueIndex.html), [InspectorNameAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/InspectorNameAttribute.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public enum OptionEnum
{
    ValueFirst = 1,
    ValueSecond = 2,
    ValueThird = 3,  
  
    [InspectorName("Value 4 - Best choice")]
    ValueForth = 4,  
  
    [InspectorName("Value 5 - Avoid")]
    ValueFifth = 5,  
  
    None = 0
}  
  
public class EnumDisplayNameExample : ScriptableObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.html)
{
    public OptionEnum MyEnum = OptionEnum.ValueForth;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Example/SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) enumDisplayName Example")]
    static void MenuCallbackup()
    {
        EnumDisplayNameExample obj = ScriptableObject.CreateInstance[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptableObject.CreateInstance.html)<EnumDisplayNameExample>();
        SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html) serializedObject = new SerializedObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html)(obj);
        SerializedProperty[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html) enumProperty = serializedObject.FindProperty("MyEnum");  
  
        // Print the members of the enum, sorted by value
        // Will output:
        // Names: None,ValueFirst,ValueSecond,ValueThird,ValueForth,ValueFifth
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Names: " + string.Join(",", enumProperty.enumNames));  
  
        //The display names show the InspectorName string when specified,
        //otherwise a more human readable version of the enum member name
        //Will output:
        //Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) names: None,Value First,Value Second,Value Third,Value 4 - Best choice,Value 5 - Avoid
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Display[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Display.html) names: " + string.Join(",", enumProperty.enumDisplayNames));  
  
        //Will output:
        //Current value: Value 4 - Best choice
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Current value: " + enumProperty.enumDisplayNames[enumProperty.enumValueIndex]);
    }
}

```

* * *
