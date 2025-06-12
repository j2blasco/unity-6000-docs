* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.SetStatic.html

#  [AndroidJavaObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.html).SetStatic
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
public void SetStatic(string fieldName, FieldType val); 
### Parameters
Parameter | Description  
---|---  
fieldName | The name of the field (e.g. _int counter;_ would have fieldName = "counter").  
val | The value to assign to the field. It has to match the field type.  
### Description
Set the value of a static field in an object type.
The generic parameter determines the field type.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Create an object of user provided class org.example.StaticFields,
    // and set the value of field 'globalName'.
    void Start()
    {
        AndroidJavaObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.html) javaObject = new AndroidJavaObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.html)("org.example.StaticFields");
        javaObject.Set<string>("globalName", "this_is_the_name");
    }
}

```

* * *
## Declaration
public void SetStatic(IntPtr fieldID, FieldType val); 
### Parameters
Parameter | Description  
---|---  
fieldID | The ID of the field to set.  
val | The value to assign to the field. It has to match the field type.  
### Description
Set the value of a static field in an object type.
The generic parameter determines the field type.
* * *
