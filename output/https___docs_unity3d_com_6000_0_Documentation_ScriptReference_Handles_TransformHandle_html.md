* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.TransformHandle.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).TransformHandle
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
public static void TransformHandle(ref [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, ref [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, ref [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) scale); 
## Declaration
public static void TransformHandle(ref [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, ref [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation, ref float uniformScale); 
## Declaration
public static void TransformHandle(ref [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, ref [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation); 
### Parameters
Parameter | Description  
---|---  
position | Position of the handle.  
rotation | The orientation of the handle in 3D space.  
scale | Scale value to modify.  
uniformScale | Uniform scale value to modify.  
### Description
Creates a transform handle.
This handle behaves like the built-in transform tool in Unity, with the option to display all scale handles, only the non-uniform scale handle, or no scale handles. Different signature variants will only display controls handles for arguments that have the ref modifier, allowing you to opt in to only those control handles you require.
* * *
