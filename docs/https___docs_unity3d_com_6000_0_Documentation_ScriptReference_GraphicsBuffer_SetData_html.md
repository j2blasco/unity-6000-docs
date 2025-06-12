* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.SetData.html

#  [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html).SetData
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
public void SetData(Array data); 
## Declaration
public void SetData(List<T> data); 
## Declaration
public void SetData(NativeArray<T> data); 
### Parameters
Parameter | Description  
---|---  
data | Array of values to fill the buffer.  
### Description
Set the buffer with values from an array.
* * *
## Declaration
public void SetData(Array data, int managedBufferStartIndex, int graphicsBufferStartIndex, int count); 
## Declaration
public void SetData(List<T> data, int managedBufferStartIndex, int graphicsBufferStartIndex, int count); 
## Declaration
public void SetData(NativeArray<T> data, int nativeBufferStartIndex, int graphicsBufferStartIndex, int count); 
### Parameters
Parameter | Description  
---|---  
data | Array of values to fill the buffer.  
managedBufferStartIndex | The first element index in data to copy to the graphics buffer.  
count | The number of elements to copy.  
graphicsBufferStartIndex | The first element index in the graphics buffer to receive the data.  
### Description
Partial copy of data values from an array into the buffer.
* * *
