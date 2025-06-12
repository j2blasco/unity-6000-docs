* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.EraseSwapBack.html

#  [CullingGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.html).EraseSwapBack
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
public void EraseSwapBack(int index); 
### Parameters
Parameter | Description  
---|---  
index | The index of the entry to erase.  
### Description
Erase a given bounding sphere by moving the final sphere on top of it.
This method also keeps the visibility information correctly synchronized, such that the correct onBecameVisible/onBecameInvisible callbacks will still be sent.
* * *
## Declaration
public static void EraseSwapBack(int index, T[] myArray, ref int size); 
### Parameters
Parameter | Description  
---|---  
index | The index of the entry to erase.  
myArray | An array of entries.  
size | The number of entries in the array that are actually used.  
### Description
Erase a given entry in an arbitrary array by copying the final entry on top of it, then decrementing the number of entries used by one.
This method is designed to be used in conjunction with the other overload, for updating your own data arrays when an entry is deleted.
* * *
