* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.GetNativeBufferPtr.html

#  [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html).GetNativeBufferPtr
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
public IntPtr GetNativeBufferPtr(); 
### Returns
**IntPtr** Pointer to the underlying graphics API buffer. 
### Description
Retrieve a native (underlying graphics API) pointer to the buffer.
Use this function to retrieve a pointer/handle corresponding to the graphics buffer, as it is represented in the native graphics API. This can be used to enable graphics buffer data manipulation from [native code plugins](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html).  
  
Note: When you use the Unity APIs to modify the buffer data, it changes the underlying graphics API native pointer. Call GetNativeBufferPtr to get the new native pointer.  
  
The type of data returned depends on the underlying graphics API: ID3D11Buffer on D3D11, ID3D12Resource on D3D12, buffer "name" (as GLuint) on OpenGL/ES, MTLBuffer on Metal.  
  
Note that calling this function when using multi-threaded rendering will synchronize with the rendering thread (a slow operation), so best practice is to set up the necessary buffer pointer only at initialization time.  
  
Additional resources: [Native code plugins](https://docs.unity3d.com/6000.0/Documentation/Manual/native-plugin-interface.html).
* * *
