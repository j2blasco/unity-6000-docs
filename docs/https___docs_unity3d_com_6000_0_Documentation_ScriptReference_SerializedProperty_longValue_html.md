* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-longValue.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).longValue
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
longValue; 
### Description
Value of an integer property as a long.
Contains a valid value when [propertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyType.html) is [SerializedPropertyType.Integer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Integer.html). Most appropriate for long properties ([SerializedPropertyNumericType.Int64](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyNumericType.Int64.html)), but can be used with all integer types of 64 bits or less, although [ulongValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-ulongValue.html) is recommended for [SerializedPropertyNumericType.UInt64](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyNumericType.UInt64.html).   
  
When assigning a value to [longValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-longValue.html), the value is clamped in the range of the property's declared type. For example, a property that is declared as a ushort is clamped between 0 and 65,535.  
  
Additional resources: [intValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-intValue.html), [ulongValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-ulongValue.html), [propertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyType.html), [SerializedPropertyType.Integer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Integer.html).
* * *
