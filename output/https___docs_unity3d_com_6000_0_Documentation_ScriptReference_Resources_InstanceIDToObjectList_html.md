* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.InstanceIDToObjectList.html

#  [Resources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html).InstanceIDToObjectList
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
public static void InstanceIDToObjectList(NativeArray<int> instanceIDs, List<Object> objects); 
### Parameters
Parameter | Description  
---|---  
instanceIDs | IDs of Object instances.  
objects | List of resoved object references, **instanceIDs** and **objects** will be of the same length and in the same order, the list will be resized if needed. Missing objects will be null.  
### Description
Translates an array of instance IDs to a list of Object references.
This is similar to [InstanceIDToObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.InstanceIDToObject.html) but resolves several IDs at once.
* * *
