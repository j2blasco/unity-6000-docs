* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.Get.html

#  [AndroidJavaObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.html).Get
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
public FieldType Get(string fieldName); 
### Parameters
Parameter | Description  
---|---  
fieldName | The name of the field (e.g. _int counter;_ would have fieldName = "counter").  
### Description
Get the value of a field in an object (non-static).
The generic parameter determines the field type.
* * *
## Declaration
public FieldType Get(IntPtr fieldID); 
### Parameters
Parameter | Description  
---|---  
fieldID | The ID of the field to get.  
### Description
Get the value of a field in an object (non-static).
The generic parameter determines the field type.
* * *
