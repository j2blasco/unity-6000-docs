* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.GetData.html

#  [TextAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset.html).GetData
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextAsset.html "Go to TextAsset Component in the Manual")
## Declaration
public NativeArray<T> GetData(); 
### Returns
**NativeArray <T>** A reference to an array in native code that provides access to the raw asset data. 
### Description
Gets raw text asset data.
It works similarly to the [bytes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-bytes.html) property, but TextAsset.GetData doesn't allocate any memory; the `NativeArray` the function returns points directly to the asset data buffer.  
  
Because this array doesn't represent a new allocation, you don't need to call `Dispose` on it and the TextAsset.GetData function is the fastest way to access raw asset bytes as a result.  
  
If the text asset is modified or destroyed, the array becomes invalid since it now points to invalid memory.  
  
If the asset data size (see [dataSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-dataSize.html)) isn't a multiple of the size of the `T` struct, Unity throws an exception.  
  
Additional resources: [bytes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-bytes.html), [text](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-text.html), [dataSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextAsset-dataSize.html), [Text Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextAsset.html).
* * *
