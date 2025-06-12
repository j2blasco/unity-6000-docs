* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.Call.html

#  [AndroidJavaObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AndroidJavaObject.html).Call
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
public void Call(string methodName, params object[] args); 
## Declaration
public void Call(string methodName, T[] args); 
### Parameters
Parameter | Description  
---|---  
methodName | Specifies which method to call.  
args | An array of parameters passed to the method.  
### Description
Calls a Java method on an object (non-static).
To call a method with return type 'void', use the regular version.
* * *
## Declaration
public ReturnType Call(string methodName, params object[] args); 
## Declaration
public ReturnType Call(string methodName, T[] args); 
### Parameters
Parameter | Description  
---|---  
methodName | Specifies which method to call.  
args | An array of parameters passed to the method.  
### Description
Call a Java method on an object.
To call a Java method with a non-void return type, use the generic version.
* * *
## Declaration
public void Call(IntPtr methodID, params object[] args); 
## Declaration
public void Call(IntPtr methodID, T[] args); 
### Parameters
Parameter | Description  
---|---  
args | An array of parameters passed to the method.  
methodID | The ID of the method to call.  
### Description
Calls a Java method on an object (non-static).
To call a method with return type 'void', use the regular version.
* * *
## Declaration
public ReturnType Call(IntPtr methodID, params object[] args); 
## Declaration
public ReturnType Call(IntPtr methodID, T[] args); 
### Parameters
Parameter | Description  
---|---  
args | An array of parameters passed to the method.  
methodID | The ID of the method to call.  
### Description
Calls a Java method on an object (non-static).
To call a Java method with a non-void return type, use the generic version.
* * *
