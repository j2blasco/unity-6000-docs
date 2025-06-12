* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-managedReferenceFullTypename.html

#  [SerializedProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty.html).managedReferenceFullTypename
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
managedReferenceFullTypename; 
### Description
String corresponding to the value of the managed reference object (dynamic) full type string.
Contains a valid value when [propertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyType.html) is [SerializedPropertyType.ManagedReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.ManagedReference.html). This property is Read Only (you cannot write to it).   
  
  
  
The full type name string returned has the following format: "[assembly-name] [namespace.][parent-class-names][classname]" where:   
- `[assembly-name]` is the name of the assembly that contains the target type   
- `[namespace.]` is an optional (if empty) namespace followed by a '.'   
- `[parent-class-names]` is a '/' separated list of optional parent class names (in the case of nested class definitions)   
- `[classname]` is the actual dynamic type name of the managed object class.   
  
  
  
'null' references return an empty type string.  
  
Additional resources: [propertyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-propertyType.html), [SerializedPropertyType.ManagedReference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedPropertyType.ManagedReference.html).
* * *
