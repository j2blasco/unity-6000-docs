* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.GetValidMethodInfo.html

#  [UnityEventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Events.UnityEventBase.html).GetValidMethodInfo
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
public static [Profiling.FrameDataView.MethodInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.MethodInfo.html) GetValidMethodInfo(object obj, string functionName, Type[] argumentTypes); 
### Parameters
Parameter | Description  
---|---  
obj | Object to search for the method.  
functionName | Function name to search for.  
argumentTypes | Argument types for the function.  
### Description
Given an object, function name, and a list of argument types; find the method that matches.
* * *
## Declaration
public static [Profiling.FrameDataView.MethodInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Profiling.FrameDataView.MethodInfo.html) GetValidMethodInfo(Type objectType, string functionName, Type[] argumentTypes); 
### Parameters
Parameter | Description  
---|---  
objectType | Object type to search for the method.  
functionName | Function name to search for.  
argumentTypes | Argument types for the function.  
### Description
Given an object type, function name, and a list of argument types; find the method that matches.
* * *
