* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.GetSubArray.html

#  [NativeArray<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.html).GetSubArray
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
public NativeArray<T> GetSubArray(int start, int length); 
### Parameters
Parameter | Description  
---|---  
start | The start index of the sub array.  
length | The length of the sub array.  
### Returns
**NativeArray <T>** A view into the array that aliases the original array, which can't be disposed. 
### Description
Gets a view into an array starting at the specified index.
* * *
