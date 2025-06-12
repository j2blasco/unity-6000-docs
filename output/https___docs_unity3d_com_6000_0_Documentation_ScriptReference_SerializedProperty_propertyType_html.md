* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyType.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).propertyType
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
[SerializedPropertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.html) propertyType; 
### Description
Type of this property (Read Only).
Property type determines which of the "value" variable accessors are valid. For example, only [boolValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-boolValue.html) is valid for [SerializedPropertyType.Boolean](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Boolean.html)   
  
For numeric types [SerializedPropertyType.Float](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Float.html) and [SerializedPropertyType.Integer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.Integer.html), the best accessor can be determined with [numericType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-numericType.html), for example [floatValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-floatValue.html) should be used for [SerializedPropertyNumericType.Float](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyNumericType.Float.html) and [doubleValue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-doubleValue.html) should be used for [SerializedPropertyNumericType.Double](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyNumericType.Double.html).  
  
Additional resources: [SerializedPropertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.html), [numericType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-numericType.html).
* * *
