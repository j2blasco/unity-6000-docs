* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.InstanceIDsToValidArray.html

#  [Resources](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Resources.html).InstanceIDsToValidArray
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
public static void InstanceIDsToValidArray(NativeArray<int> instanceIDs, NativeArray<bool> validArray); 
## Declaration
public static void InstanceIDsToValidArray(ReadOnlySpan<int> instanceIDs, Span<bool> validArray); 
### Parameters
Parameter | Description  
---|---  
instanceIDs | IDs of Object instances.  
validArray | Array of bools indicating whether a given instance ID corresponds to a valid Object.  
### Description
Translates an array of instance IDs to an array of bools indicating whether a given instance ID from **instanceIDs** corresponds to a valid Object in memory. The Object could have been deleted or not loaded into memory yet.
**instanceIDs** and **validArray** must be of the same length. The value at each index in **validArray** corresponds with the instance ID at the same index in **instanceIDs**.
* * *
